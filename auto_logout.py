import sqlite3
import os
import sys
from colorama import Fore, Style, init
from config import get_config

# Initialize colorama
init()

# Define emoji constants
EMOJI = {
    'SUCCESS': '✅',
    'ERROR': '❌',
    'INFO': 'ℹ️',
}

def auto_logout(translator=None):
    """Automatically logout by clearing authentication data from Cursor database"""
    try:
        # Get configuration
        config = get_config(translator)
        if not config:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to load configuration{Style.RESET_ALL}")
            return False
            
        # Get database path based on operating system
        try:
            if sys.platform == "win32":  # Windows
                if not config.has_section('WindowsPaths'):
                    raise ValueError("Windows paths not configured")
                db_path = config.get('WindowsPaths', 'sqlite_path')
                
            elif sys.platform == 'linux':  # Linux
                if not config.has_section('LinuxPaths'):
                    raise ValueError("Linux paths not configured")
                db_path = config.get('LinuxPaths', 'sqlite_path')
                
            elif sys.platform == 'darwin':  # macOS
                if not config.has_section('MacPaths'):
                    raise ValueError("macOS paths not configured")
                db_path = config.get('MacPaths', 'sqlite_path')
                
            else:
                print(f"{Fore.RED}{EMOJI['ERROR']} Unsupported platform{Style.RESET_ALL}")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Error getting database path: {str(e)}{Style.RESET_ALL}")
            return False

        # Check if database exists
        if not os.path.exists(db_path):
            print(f"{Fore.YELLOW}{EMOJI['INFO']} No active Cursor session found (database doesn't exist){Style.RESET_ALL}")
            return True

        # Connect to database and clear authentication
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Add timeout settings
            conn.execute("PRAGMA busy_timeout = 5000")
            
            # List of authentication keys to delete
            auth_keys = [
                "cursorAuth/accessToken",
                "cursorAuth/refreshToken",
                "cursorAuth/cachedEmail",
                "cursorAuth/cachedSignUpType"
            ]
            
            # Delete authentication data
            cursor.execute("BEGIN TRANSACTION")
            deleted_count = 0
            
            for key in auth_keys:
                cursor.execute("DELETE FROM ItemTable WHERE key = ?", (key,))
                if cursor.rowcount > 0:
                    deleted_count += 1
            
            cursor.execute("COMMIT")
            
            if deleted_count > 0:
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Logged out successfully (cleared {deleted_count} auth entries){Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{EMOJI['INFO']} No active login found{Style.RESET_ALL}")
            
            return True
            
        except sqlite3.Error as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Database error: {str(e)}{Style.RESET_ALL}")
            return False
        finally:
            if conn:
                conn.close()
                
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Logout error: {str(e)}{Style.RESET_ALL}")
        return False

if __name__ == "__main__":
    auto_logout()
