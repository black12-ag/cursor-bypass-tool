import os
import shutil
import platform
import tempfile
import glob
from colorama import Fore, Style, init
import configparser
from new_signup import get_user_documents_path
from config import get_config
from datetime import datetime

# Initialize colorama
init()

# Define emoji constants
EMOJI = {
    "FILE": "📄",
    "BACKUP": "💾",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "RESET": "🔄",
    "WARNING": "⚠️",
}

def get_workbench_cursor_path(translator=None) -> str:
    """Get Cursor workbench.desktop.main.js path"""
    system = platform.system()

    # Read configuration
    config_dir = os.path.join(get_user_documents_path(), ".BYPASS CURSUR")
    config_file = os.path.join(config_dir, "config.ini")
    config = configparser.ConfigParser()

    if os.path.exists(config_file):
        config.read(config_file)
    
    paths_map = {
        "Darwin": {  # macOS
            "base": "/Applications/Cursor.app/Contents/Resources/app",
            "main": "out/vs/workbench/workbench.desktop.main.js"
        },
        "Windows": {
            "main": "out\\vs\\workbench\\workbench.desktop.main.js"
        },
        "Linux": {
            "bases": ["/opt/Cursor/resources/app", "/usr/share/cursor/resources/app", "/usr/lib/cursor/app/"],
            "main": "out/vs/workbench/workbench.desktop.main.js"
        }
    }
    
    if system == "Linux":
        # Add extracted AppImage with correct usr structure
        extracted_usr_paths = glob.glob(os.path.expanduser("~/squashfs-root/usr/share/cursor/resources/app"))
            
        paths_map["Linux"]["bases"].extend(extracted_usr_paths)

    if system not in paths_map:
        raise OSError(translator.get('reset.unsupported_os', system=system) if translator else f"不支持的操作系统: {system}")

    if system == "Linux":
        for base in paths_map["Linux"]["bases"]:
            main_path = os.path.join(base, paths_map["Linux"]["main"])
            print(f"{Fore.CYAN}{EMOJI['INFO']} Checking path: {main_path}{Style.RESET_ALL}")
            if os.path.exists(main_path):
                return main_path

    if system == "Windows":
        base_path = config.get('WindowsPaths', 'cursor_path')
    elif system == "Darwin":
        base_path = paths_map[system]["base"]
    else:  # Linux
        # For Linux, we've already checked all bases in the loop above
        # If we're here, it means none of the bases worked, so we'll use the first one
        base_path = paths_map[system]["bases"][0]

    main_path = os.path.join(base_path, paths_map[system]["main"])
    
    if not os.path.exists(main_path):
        raise OSError(translator.get('reset.file_not_found', path=main_path) if translator else f"未找到 Cursor main.js 文件: {main_path}")
        
    return main_path


def modify_workbench_js(file_path: str, translator=None) -> bool:
    """
    Modify file content
    """
    try:
        # Save original file permissions
        original_stat = os.stat(file_path)
        original_mode = original_stat.st_mode
        original_uid = original_stat.st_uid
        original_gid = original_stat.st_gid

        # Create temporary file
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", errors="ignore", delete=False) as tmp_file:
            # Read original content
            with open(file_path, "r", encoding="utf-8", errors="ignore") as main_file:
                content = main_file.read()

            patterns = {
                # 通用按钮替换模式
                r'B(k,D(Ln,{title:"Upgrade to Pro",size:"small",get codicon(){return A.rocket},get onClick(){return t.pay}}),null)': r'B(k,D(Ln,{title:"MUNIR KABIR",size:"small",get codicon(){return A.github},get onClick(){return function(){window.open("https://example.com/munir-temp-link","_blank")}}}),null)',
                
                # Windows/Linux/Mac 通用按钮替换模式
                r'M(x,I(as,{title:"Upgrade to Pro",size:"small",get codicon(){return $.rocket},get onClick(){return t.pay}}),null)': r'M(x,I(as,{title:"MUNIR KABIR",size:"small",get codicon(){return $.rocket},get onClick(){return function(){window.open("https://example.com/munir-temp-link","_blank")}}}),null)',
                
                # Badge 替换
                r'<div>Pro Trial': r'<div>MUNIR',

                r'py-1">Auto-select': r'py-1">Bypass-Version-Pin',
                
                #
                r'async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;':r'async getEffectiveTokenLimit(e){return 9000000;const n=e.modelName;if(!n)return 9e5;',
                # Pro
                r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>.");': r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>. <h1>MUNIR</h1>");',
                
                # Toast 替换
                r'notifications-toasts': r'notifications-toasts hidden'
            }

            # 使用patterns进行替换
            for old_pattern, new_pattern in patterns.items():
                content = content.replace(old_pattern, new_pattern)

            # Write to temporary file
            tmp_file.write(content)
            tmp_path = tmp_file.name

        # Backup original file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup.{timestamp}"
        shutil.copy2(file_path, backup_path)
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('reset.backup_created', path=backup_path)}{Style.RESET_ALL}")
        
        # Move temporary file to original position
        if os.path.exists(file_path):
            os.remove(file_path)
        shutil.move(tmp_path, file_path)

        # Restore original permissions
        os.chmod(file_path, original_mode)
        if os.name != "nt":  # Not Windows
            os.chown(file_path, original_uid, original_gid)

        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('reset.file_modified')}{Style.RESET_ALL}")
        return True

    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('reset.modify_file_failed', error=str(e))}{Style.RESET_ALL}")
        if "tmp_path" in locals():
            try:
                os.unlink(tmp_path)
            except:
                pass
        return False
    
def run(translator=None):
    config = get_config(translator)
    if not config:
        return False
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['RESET']} {translator.get('bypass_token_limit.title')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"""{Fore.CYAN}
   ███╗   ███╗██╗   ██╗███╗   ██╗██╗██████╗     
   ████╗ ████║██║   ██║████╗  ██║██║██╔══██╗    
   ██╔████╔██║██║   ██║██╔██╗ ██║██║██████╔╝    
   ██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██╗    
   ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██║  ██║    
   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝    
{Style.RESET_ALL}""")

    modify_workbench_js(get_workbench_cursor_path(translator), translator)

    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    input(f"{EMOJI['INFO']} {translator.get('bypass_token_limit.press_enter')}...")

if __name__ == "__main__":
    from main import translator as main_translator
    run(main_translator)