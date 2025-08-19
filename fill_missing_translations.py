"""
Compares two JSON translation files in /locales (e.g., en.json and ar.json).
Finds keys missing in the target file, translates their values using Google Translate API (googletrans 4.0.2),
and inserts the translations. Runs in parallel for speed and creates a backup of the target file.
"""
import json
import sys
import os
from pathlib import Path
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
import time
import shutil
import asyncio

# Import googletrans with error handling
try:
    from googletrans import Translator as GoogleTranslator
    GOOGLETRANS_AVAILABLE = True
    print(f"{Fore.GREEN}Using googletrans for translation.{Style.RESET_ALL}")
except ImportError:
    GOOGLETRANS_AVAILABLE = False
    print(f"{Fore.YELLOW}googletrans library not found. Will use web scraping fallback method.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}To install googletrans: pip install googletrans==4.0.2{Style.RESET_ALL}")
    import requests

init(autoreset=True)

# Language code mapping to Google Translate language codes
LANGUAGE_MAPPING = {
    "zh_cn": "zh-CN",  # Simplified Chinese
    "zh_tw": "zh-TW",  # Traditional Chinese
    "ar": "ar",        # Arabic
    "bg": "bg",        # Bulgarian
    "de": "de",        # German
    "en": "en",        # English
    "es": "es",        # Spanish
    "fr": "fr",        # French
    "it": "it",        # Italian
    "ja": "ja",        # Japanese
    "ko": "ko",        # Korean
    "nl": "nl",        # Dutch
    "pt": "pt",        # Portuguese
    "ru": "ru",        # Russian
    "tr": "tr",        # Turkish
    "vi": "vi",        # Vietnamese
    # Add more mappings as needed
}

# Recursively get all keys in the JSON as dot-separated paths
def get_keys(d, prefix=''):
    keys = set()
    for k, v in d.items():
        full_key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            keys |= get_keys(v, full_key)
        else:
            keys.add(full_key)
    return keys

# Get value from nested dict by dot-separated path
def get_by_path(d, path):
    for p in path.split('.'):
        d = d[p]
    return d

# Set value in nested dict by dot-separated path
def set_by_path(d, path, value):
    parts = path.split('.')
    for p in parts[:-1]:
        if p not in d:
            d[p] = {}
        d = d[p]
    d[parts[-1]] = value

# Get Google Translate language code from file name
def get_google_lang_code(file_lang):
    # Remove .json extension if present
    if file_lang.endswith('.json'):
        file_lang = file_lang[:-5]
    
    # Return mapped language code or the original if not in mapping
    return LANGUAGE_MAPPING.get(file_lang, file_lang)

# Translate text using Google Translate API if available, otherwise fallback to web scraping
def translate(text, source, target):
    # Map language codes to Google Translate format
    source_lang = get_google_lang_code(source)
    target_lang = get_google_lang_code(target)
    
    print(f"{Fore.CYAN}Translating from {source_lang} to {target_lang}{Style.RESET_ALL}")
    
    if GOOGLETRANS_AVAILABLE:
        try:
            # Use synchronous web scraping instead of async googletrans
            return translate_web_scraping(text, source_lang, target_lang)
        except Exception as e:
            print(Fore.YELLOW + f"Translation error: {e}. Trying alternative method.")
            return translate_web_scraping(text, source_lang, target_lang)
    else:
        return translate_web_scraping(text, source_lang, target_lang)

# Fallback translation method using web scraping
def translate_web_scraping(text, source, target):
    try:
        import requests
        # 使用更可靠的 Google 翻译 API URL
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source}&tl={target}&dt=t&q={requests.utils.quote(text)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # 解析 JSON 响应
            result = response.json()
            # 提取翻译结果
            translated_text = ''
            for sentence in result[0]:
                if len(sentence) > 0:
                    translated_text += sentence[0]
            
            if translated_text:
                return translated_text
            else:
                print(Fore.RED + f"Translation not found for: {text}")
                return text
        else:
            print(Fore.RED + f"Request failed with status code {response.status_code} for: {text}")
            return text
    except Exception as e:
        print(Fore.RED + f"Web scraping translation error: {e}")
        return text

# Process a single language file
def process_language(en_filename, other_filename, create_backup=None):
    # Always use the /locales directory
    en_path = Path("locales") / en_filename
    other_path = Path("locales") / other_filename
    # Infer language code from filename (before .json)
    en_lang = Path(en_filename).stem
    other_lang = Path(other_filename).stem

    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Processing: {other_filename} (Translating to {get_google_lang_code(other_lang)}){Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

    print(f"{Fore.CYAN}Reading source file: {en_path}{Style.RESET_ALL}")
    with open(en_path, encoding='utf-8') as f:
        en = json.load(f)
    
    print(f"{Fore.CYAN}Reading target file: {other_path}{Style.RESET_ALL}")
    try:
        with open(other_path, encoding='utf-8') as f:
            other = json.load(f)
    except FileNotFoundError:
        # If target file doesn't exist, create an empty one
        print(f"{Fore.YELLOW}Target file not found. Creating a new file.{Style.RESET_ALL}")
        other = {}
    except json.JSONDecodeError:
        # If target file is invalid JSON, create an empty one
        print(f"{Fore.YELLOW}Target file contains invalid JSON. Creating a new file.{Style.RESET_ALL}")
        other = {}

    en_keys = get_keys(en)
    other_keys = get_keys(other)

    missing = en_keys - other_keys
    print(f"{Fore.YELLOW}Found {len(missing)} missing keys{Style.RESET_ALL}")

    if not missing:
        print(f"{Fore.GREEN}No missing keys found. Translation is complete!{Style.RESET_ALL}")
        return True

    # Parallel translation using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:  # Further reduced workers for googletrans 4.0.2
        future_to_key = {
            executor.submit(translate, get_by_path(en, key), en_lang, other_lang): key
            for key in missing
        }
        
        completed = 0
        total = len(missing)
        
        for future in as_completed(future_to_key):
            key = future_to_key[future]
            value = get_by_path(en, key)
            try:
                translated = future.result()
                completed += 1
                print(f"{Fore.CYAN}[{completed}/{total}] Translated [{key}]: '{value}' -> " + Fore.MAGENTA + f"'{translated}'")
            except Exception as exc:
                print(f"{Fore.RED}Error translating {key}: {exc}")
                translated = value
            set_by_path(other, key, translated)

    # Ask about backup if not specified
    if create_backup is None and os.path.exists(other_path):
        while True:
            backup_choice = input(f"{Fore.CYAN}Create backup file? (y/N): {Style.RESET_ALL}").lower()
            if backup_choice in ['y', 'yes']:
                create_backup = True
                break
            elif backup_choice in ['', 'n', 'no']:
                create_backup = False
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 'y' or 'n'.{Style.RESET_ALL}")

    # Create backup if requested and file exists
    if create_backup and os.path.exists(other_path):
        backup_path = other_path.with_suffix('.bak.json')
        shutil.copy2(other_path, backup_path)
        print(f"{Fore.GREEN}Backup created at {backup_path}{Style.RESET_ALL}")

    # Save the updated file
    with open(other_path, 'w', encoding='utf-8') as f:
        json.dump(other, f, ensure_ascii=False, indent=4)
    print(f"{Fore.GREEN}File updated: {other_path}{Style.RESET_ALL}")
    return True

# Main function with interactive menu
def main():
    # Check if locales directory exists
    locales_dir = Path("locales")
    if not locales_dir.exists():
        print(f"{Fore.YELLOW}Creating 'locales' directory...{Style.RESET_ALL}")
        locales_dir.mkdir(parents=True)
    
    # Get all JSON files in locales directory (excluding backup files)
    json_files = [f for f in os.listdir(locales_dir) if f.endswith('.json') and not f.endswith('.bak.json')]
    
    # Check if en.json exists (source file)
    if 'en.json' not in json_files:
        print(f"{Fore.RED}Error: 'en.json' not found in locales directory. This file is required as the source for translations.{Style.RESET_ALL}")
        return False
    
    # Get all target language files (excluding en.json)
    target_files = [f for f in json_files if f != 'en.json']
    
    # Add option to create a new language file
    available_languages = list(LANGUAGE_MAPPING.keys())
    if 'en' in available_languages:
        available_languages.remove('en')  # Remove English as it's the source
    
    # Filter out languages that already have files
    existing_lang_codes = [f.split('.')[0] for f in target_files]
    available_languages = [lang for lang in available_languages if lang not in existing_lang_codes]
    
    # Display menu
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Translation Tool - Select target language to update{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    print(f"{Fore.GREEN}0{Style.RESET_ALL}. Translate all existing language files")
    
    # List existing language files
    for i, file in enumerate(target_files, 1):
        lang_code = file.split('.')[0]
        google_lang = get_google_lang_code(lang_code)
        print(f"{Fore.GREEN}{i}{Style.RESET_ALL}. {lang_code} ({google_lang})")
    
    # Option to create a new language file (only if there are available languages)
    next_option = len(target_files) + 1
    
    if available_languages:
        print(f"\n{Fore.CYAN}Create new language file:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{next_option}{Style.RESET_ALL}. Create a new language file")
        max_choice = next_option
    else:
        max_choice = len(target_files)
    
    # Get user choice
    while True:
        try:
            choice = input(f"\n{Fore.CYAN}Enter your choice (0-{max_choice}): {Style.RESET_ALL}")
            
            if choice.strip() == '':
                print(f"{Fore.RED}Please enter a number.{Style.RESET_ALL}")
                continue
                
            choice = int(choice)
            
            if choice < 0 or choice > max_choice:
                print(f"{Fore.RED}Invalid choice. Please enter a number between 0 and {max_choice}.{Style.RESET_ALL}")
                continue
                
            break
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
    
    # Ask about backup for all files
    create_backup = None
    if choice == 0:
        while True:
            backup_choice = input(f"{Fore.CYAN}Create backup files? (y/N): {Style.RESET_ALL}").lower()
            if backup_choice in ['y', 'yes']:
                create_backup = True
                break
            elif backup_choice in ['', 'n', 'no']:
                create_backup = False
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please enter 'y' or 'n'.{Style.RESET_ALL}")
    
    # Process selected language(s)
    if choice == 0:
        print(f"{Fore.CYAN}Translating all existing languages...{Style.RESET_ALL}")
        success_count = 0
        
        for target_file in target_files:
            try:
                if process_language('en.json', target_file, create_backup):
                    success_count += 1
            except Exception as e:
                print(f"{Fore.RED}Error processing {target_file}: {str(e)}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}Translation completed for {success_count} out of {len(target_files)} languages.{Style.RESET_ALL}")
    elif available_languages and choice == next_option:
        # Create a new language file
        print(f"\n{Fore.CYAN}Available languages:{Style.RESET_ALL}")
        for i, lang in enumerate(available_languages):
            google_lang = get_google_lang_code(lang)
            print(f"{Fore.GREEN}{i+1}{Style.RESET_ALL}. {lang} ({google_lang})")
        
        while True:
            try:
                lang_choice = input(f"\n{Fore.CYAN}Select language (1-{len(available_languages)}): {Style.RESET_ALL}")
                lang_choice = int(lang_choice)
                
                if lang_choice < 1 or lang_choice > len(available_languages):
                    print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and {len(available_languages)}.{Style.RESET_ALL}")
                    continue
                
                selected_lang = available_languages[lang_choice-1]
                new_file = f"{selected_lang}.json"
                
                if new_file in json_files:
                    print(f"{Fore.YELLOW}Warning: {new_file} already exists. It will be updated with missing translations.{Style.RESET_ALL}")
                
                process_language('en.json', new_file)
                print(f"\n{Fore.GREEN}Created and translated {new_file}.{Style.RESET_ALL}")
                break
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
    else:
        target_file = target_files[choice - 1]
        try:
            process_language('en.json', target_file)
            print(f"\n{Fore.GREEN}Translation completed for {target_file}.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error processing {target_file}: {str(e)}{Style.RESET_ALL}")
    
    return True

if __name__ == "__main__":
    # If arguments are provided, use the old method
    if len(sys.argv) == 3:
        process_language(sys.argv[1], sys.argv[2])
    else:
        # Otherwise, show the interactive menu
        main()