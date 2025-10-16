# main.py
# This script allows the user to choose which script to run.
import os
import sys
import json
from logo import print_logo, version
from colorama import Fore, Style, init
import locale
import platform
import requests
import subprocess
from config import get_config, force_update_config
import shutil
import re
from utils import get_user_documents_path  

# Add these imports for Arabic support
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:
    arabic_reshaper = None
    get_display = None

# Only import windll on Windows systems
if platform.system() == 'Windows':
    import ctypes
    # Only import windll on Windows systems
    from ctypes import windll

# Initialize colorama
init()

# Define emoji and color constants
EMOJI = {
    "FILE": "📄",
    "BACKUP": "💾",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "RESET": "🔄",
    "MENU": "📋",
    "ARROW": "➜",
    "LANG": "🌐",
    "UPDATE": "🔄",
    "ADMIN": "🔐",
    "AIRDROP": "💰",
    "ROCKET": "🚀",
    "STAR": "⭐",
    "SUN": "🌟",
    "CONTRIBUTE": "🤝",
    "SETTINGS": "⚙️"
}

# Function to check if running as frozen executable
def is_frozen():
    """Check if the script is running as a frozen executable."""
    return getattr(sys, 'frozen', False)

# Function to check admin privileges (Windows only)
def is_admin():
    """Check if the script is running with admin privileges (Windows only)."""
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except Exception:
            return False
    # Always return True for non-Windows to avoid changing behavior
    return True

# Function to restart with admin privileges
def run_as_admin():
    """Restart the current script with admin privileges (Windows only)."""
    if platform.system() != 'Windows':
        return False
        
    try:
        args = [sys.executable] + sys.argv
        
        # Request elevation via ShellExecute
        print(f"{Fore.YELLOW}{EMOJI['ADMIN']} Requesting administrator privileges...{Style.RESET_ALL}")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", args[0], " ".join('"' + arg + '"' for arg in args[1:]), None, 1)
        return True
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Failed to restart with admin privileges: {e}{Style.RESET_ALL}")
        return False

class Translator:
    def __init__(self):
        self.translations = {}
        self.config = get_config()
        
        # Create language cache directory if it doesn't exist
        if self.config and self.config.has_section('Language'):
            self.language_cache_dir = self.config.get('Language', 'language_cache_dir')
            os.makedirs(self.language_cache_dir, exist_ok=True)
        else:
            self.language_cache_dir = None
        
        # Set fallback language from config if available
        self.fallback_language = 'en'
        if self.config and self.config.has_section('Language') and self.config.has_option('Language', 'fallback_language'):
            self.fallback_language = self.config.get('Language', 'fallback_language')
        
        # Load saved language from config if available, otherwise detect system language
        if self.config and self.config.has_section('Language') and self.config.has_option('Language', 'current_language'):
            saved_language = self.config.get('Language', 'current_language')
            if saved_language and saved_language.strip():
                self.current_language = saved_language
            else:
                self.current_language = self.detect_system_language()
                # Save detected language to config
                if self.config.has_section('Language'):
                    self.config.set('Language', 'current_language', self.current_language)
                    config_dir = os.path.join(get_user_documents_path(), ".cursor-free-vip")
                    config_file = os.path.join(config_dir, "config.ini")
                    with open(config_file, 'w', encoding='utf-8') as f:
                        self.config.write(f)
        else:
            self.current_language = self.detect_system_language()
        
        self.load_translations()
    
    def detect_system_language(self):
        """Always return English"""
        return 'en'
    
    
    def download_language_file(self, lang_code):
        """Method kept for compatibility but now returns False as language files are integrated"""
        print(f"{Fore.YELLOW}{EMOJI['INFO']} Languages are now integrated into the package, no need to download.{Style.RESET_ALL}")
        return False
            
    def load_translations(self):
        """Load all available translations from the integrated package"""
        try:
            # Collection of languages we've successfully loaded
            loaded_languages = set()
            
            locales_paths = []
            
            # Check for PyInstaller bundle first
            if hasattr(sys, '_MEIPASS'):
                locales_paths.append(os.path.join(sys._MEIPASS, 'locales'))
            
            # Check script directory next
            script_dir = os.path.dirname(os.path.abspath(__file__))
            locales_paths.append(os.path.join(script_dir, 'locales'))
            
            # Also check current working directory
            locales_paths.append(os.path.join(os.getcwd(), 'locales'))
            
            for locales_dir in locales_paths:
                if os.path.exists(locales_dir) and os.path.isdir(locales_dir):
                    for file in os.listdir(locales_dir):
                        if file.endswith('.json'):
                            lang_code = file[:-5]  # Remove .json
                            try:
                                with open(os.path.join(locales_dir, file), 'r', encoding='utf-8') as f:
                                    self.translations[lang_code] = json.load(f)
                                    loaded_languages.add(lang_code)
                                    loaded_any = True
                            except (json.JSONDecodeError, UnicodeDecodeError) as e:
                                print(f"{Fore.RED}{EMOJI['ERROR']} Error loading {file}: {e}{Style.RESET_ALL}")
                                continue

        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to load translations: {e}{Style.RESET_ALL}")
            # Create at least minimal English translations for basic functionality
            self.translations['en'] = {"menu": {"title": "Menu", "exit": "Exit", "invalid_choice": "Invalid choice"}}
    
    def fix_arabic(self, text):
        if self.current_language == 'ar' and arabic_reshaper and get_display:
            try:
                reshaped_text = arabic_reshaper.reshape(text)
                bidi_text = get_display(reshaped_text)
                return bidi_text
            except Exception:
                return text
        return text

    def get(self, key, **kwargs):
        """Get translated text with fallback support"""
        try:
            # Try current language
            result = self._get_translation(self.current_language, key)
            if result == key and self.current_language != self.fallback_language:
                # Try fallback language if translation not found
                result = self._get_translation(self.fallback_language, key)
            formatted = result.format(**kwargs) if kwargs else result
            return self.fix_arabic(formatted)
        except Exception:
            return key
    
    def _get_translation(self, lang_code, key):
        """Get translation for a specific language"""
        try:
            keys = key.split('.')
            value = self.translations.get(lang_code, {})
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k, key)
                else:
                    return key
            return value
        except Exception:
            return key
    
    def set_language(self, lang_code):
        """Set current language with validation"""
        if lang_code in self.translations:
            self.current_language = lang_code
            return True
        return False

    def get_available_languages(self):
        """Get list of available languages"""
        # Get currently loaded languages
        available_languages = list(self.translations.keys())
        
        # Sort languages alphabetically for better display
        return sorted(available_languages)

# Create translator instance
translator = Translator()

def print_menu():
    """Print menu options"""
    try:
        config = get_config()
        if config.getboolean('Utils', 'enabled_account_info'):
            import cursor_acc_info
            cursor_acc_info.display_account_info(translator)
    except Exception as e:
        print(f"{Fore.YELLOW}{EMOJI['INFO']} {translator.get('menu.account_info_error', error=str(e))}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{EMOJI['MENU']} {translator.get('menu.title')}:{Style.RESET_ALL}")
    if translator.current_language == 'zh_cn' or translator.current_language == 'zh_tw':
        print(f"{Fore.YELLOW}{'─' * 70}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}{'─' * 110}{Style.RESET_ALL}")
    
    # Get terminal width
    try:
        terminal_width = shutil.get_terminal_size().columns
    except:
        terminal_width = 80  # Default width
    
    # Define all menu items
    menu_items = {
        0: f"{Fore.GREEN}0{Style.RESET_ALL}. {EMOJI['ERROR']} {translator.get('menu.exit')}",
        1: f"{Fore.GREEN}1{Style.RESET_ALL}. {EMOJI['RESET']} {translator.get('menu.reset')}",
        2: f"{Fore.GREEN}2{Style.RESET_ALL}. {EMOJI['SUCCESS']} {translator.get('menu.register_manual')}",
        3: f"{Fore.GREEN}3{Style.RESET_ALL}. {EMOJI['RESET']} {translator.get('menu.totally_reset')}"
    }
    
    # Automatically calculate the number of menu items in the left and right columns
    total_items = len(menu_items)
    left_column_count = (total_items + 1) // 2  # The number of options displayed on the left (rounded up)
    
    # Build left and right columns of menus
    sorted_indices = sorted(menu_items.keys())
    left_menu = [menu_items[i] for i in sorted_indices[:left_column_count]]
    right_menu = [menu_items[i] for i in sorted_indices[left_column_count:]]
    
    # Calculate the maximum display width of left menu items
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def get_display_width(s):
        """Calculate the display width of a string, considering Chinese characters and emojis"""
        # Remove ANSI color codes
        clean_s = ansi_escape.sub('', s)
        width = 0
        for c in clean_s:
            # Chinese characters and some emojis occupy two character widths
            if ord(c) > 127:
                width += 2
            else:
                width += 1
        return width
    
    max_left_width = 0
    for item in left_menu:
        width = get_display_width(item)
        max_left_width = max(max_left_width, width)
    
    # Set the starting position of right menu
    fixed_spacing = 4  # Fixed spacing
    right_start = max_left_width + fixed_spacing
    
    # Calculate the number of spaces needed for right menu items
    spaces_list = []
    for i in range(len(left_menu)):
        if i < len(left_menu):
            left_item = left_menu[i]
            left_width = get_display_width(left_item)
            spaces = right_start - left_width
            spaces_list.append(spaces)
    
    # Print menu items
    max_rows = max(len(left_menu), len(right_menu))
    
    for i in range(max_rows):
        # Print left menu items
        if i < len(left_menu):
            left_item = left_menu[i]
            print(left_item, end='')
            
            # Use pre-calculated spaces
            spaces = spaces_list[i]
        else:
            # If left side has no items, print only spaces
            spaces = right_start
            print('', end='')
        
        # Print right menu items
        if i < len(right_menu):
            print(' ' * spaces + right_menu[i])
        else:
            print()  # Change line
    if translator.current_language == 'zh_cn' or translator.current_language == 'zh_tw':
        print(f"{Fore.YELLOW}{'─' * 70}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}{'─' * 110}{Style.RESET_ALL}")



def main():
    # Check for admin privileges if running as executable on Windows only
    if platform.system() == 'Windows' and is_frozen() and not is_admin():
        print(f"{Fore.YELLOW}{EMOJI['ADMIN']} {translator.get('menu.admin_required')}{Style.RESET_ALL}")
        if run_as_admin():
            sys.exit(0)  # Exit after requesting admin privileges
        else:
            print(f"{Fore.YELLOW}{EMOJI['INFO']} {translator.get('menu.admin_required_continue')}{Style.RESET_ALL}")
    
    print_logo()
    
    # Initialize configuration
    config = get_config(translator)
    if not config:
        print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('menu.config_init_failed')}{Style.RESET_ALL}")
        return
    force_update_config(translator)

    # Auto quit Cursor and logout on startup
    print(f"\n{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['INFO']} Preparing Cursor environment...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}\n")
    
    # Step 1: Quit Cursor if running
    import quit_cursor
    quit_cursor.quit_cursor(translator)
    
    # Step 2: Logout any existing account
    import auto_logout
    auto_logout.auto_logout(translator)
    
    print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} Ready! Cursor has been closed and logged out.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}\n")

    print_menu()
    
    while True:
        try:
            choice_num = 3
            choice = input(f"\n{EMOJI['ARROW']} {Fore.CYAN}{translator.get('menu.input_choice', choices=f'0-{choice_num}')}: {Style.RESET_ALL}")

            match choice:
                case "0":
                    print(f"\n{Fore.YELLOW}{EMOJI['INFO']} {translator.get('menu.exit')}...{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}")
                    return
                case "1":
                    import reset_machine_manual
                    reset_machine_manual.run(translator)
                    print_menu()   
                case "2":
                    import cursor_register_manual
                    cursor_register_manual.main(translator)
                    print_menu()    
                case "3":
                    import totally_reset_cursor
                    totally_reset_cursor.run(translator)
                    print_menu()
                case _:
                    print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('menu.invalid_choice')}{Style.RESET_ALL}")
                    print_menu()

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}{EMOJI['INFO']}  {translator.get('menu.program_terminated')}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}")
            return
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('menu.error_occurred', error=str(e))}{Style.RESET_ALL}")
            print_menu()

if __name__ == "__main__":
    main()