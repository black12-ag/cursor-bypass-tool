"""
Manual Custom Auth for Cursor AI
This script allows users to manually input access token and email to authenticate with Cursor AI.
"""

import os
import sys
import random
import string
from colorama import Fore, Style, init
from cursor_auth import CursorAuth

# Initialize colorama
init(autoreset=True)

# Define emoji and color constants
EMOJI = {
    'DB': '🗄️',
    'UPDATE': '🔄',
    'SUCCESS': '✅',
    'ERROR': '❌',
    'WARN': '⚠️',
    'INFO': 'ℹ️',
    'FILE': '📄',
    'KEY': '🔐'
}

def generate_random_email():
    """Generate a random Cursor email address"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"cursor_{random_string}@cursor.ai"

def main(translator=None):
    """Main function to handle manual authentication"""
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Manual Cursor Authentication{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    # Get token from user
    print(f"\n{Fore.YELLOW}{EMOJI['INFO']} {translator.get('manual_auth.token_prompt') if translator else 'Enter your Cursor token (access_token/refresh_token):'}{Style.RESET_ALL}")
    token = input(f"{Fore.CYAN}> {Style.RESET_ALL}").strip()
    
    if not token:
        print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.token_required') if translator else 'Token is required'}{Style.RESET_ALL}")
        return False
    
    # Verify token validity
    try:
        from check_user_authorized import check_user_authorized
        print(f"\n{Fore.CYAN}{EMOJI['INFO']} {translator.get('manual_auth.verifying_token') if translator else 'Verifying token validity...'}{Style.RESET_ALL}")
        
        is_valid = check_user_authorized(token, translator)
        
        if not is_valid:
            print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.invalid_token') if translator else 'Invalid token. Authentication aborted.'}{Style.RESET_ALL}")
            return False
            
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('manual_auth.token_verified') if translator else 'Token verified successfully!'}{Style.RESET_ALL}")
    except ImportError:
        print(f"{Fore.YELLOW}{EMOJI['WARN']} {translator.get('manual_auth.token_verification_skipped') if translator else 'Token verification skipped (check_user_authorized.py not found)'}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}{EMOJI['WARN']} {translator.get('manual_auth.token_verification_error', error=str(e)) if translator else f'Error verifying token: {str(e)}'}{Style.RESET_ALL}")
        
        # Ask user if they want to continue despite verification error
        continue_anyway = input(f"{Fore.YELLOW}{translator.get('manual_auth.continue_anyway') if translator else 'Continue anyway? (y/N): '}{Style.RESET_ALL}").strip().lower()
        if continue_anyway not in ["y", "yes"]:
            print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.operation_cancelled') if translator else 'Operation cancelled'}{Style.RESET_ALL}")
            return False
    
    # Get email (or generate random one)
    print(f"\n{Fore.YELLOW}{EMOJI['INFO']} {translator.get('manual_auth.email_prompt') if translator else 'Enter email (leave blank for random email):'}{Style.RESET_ALL}")
    email = input(f"{Fore.CYAN}> {Style.RESET_ALL}").strip()
    
    if not email:
        email = generate_random_email()
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('manual_auth.random_email_generated', email=email) if translator else f'Random email generated: {email}'}{Style.RESET_ALL}")
    
    # Get auth type
    print(f"\n{Fore.YELLOW}{EMOJI['INFO']} {translator.get('manual_auth.auth_type_prompt') if translator else 'Select authentication type:'}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. {translator.get('manual_auth.auth_type_auth0') if translator else 'Auth_0 (Default)'}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. {translator.get('manual_auth.auth_type_google') if translator else 'Google'}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. {translator.get('manual_auth.auth_type_github') if translator else 'GitHub'}{Style.RESET_ALL}")
    
    auth_choice = input(f"{Fore.CYAN}> {Style.RESET_ALL}").strip()
    
    if auth_choice == "2":
        auth_type = "Google"
    elif auth_choice == "3":
        auth_type = "GitHub"
    else:
        auth_type = "Auth_0"
    
    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('manual_auth.auth_type_selected', type=auth_type) if translator else f'Selected authentication type: {auth_type}'}{Style.RESET_ALL}")
    
    # Confirm before proceeding
    print(f"\n{Fore.YELLOW}{EMOJI['WARN']} {translator.get('manual_auth.confirm_prompt') if translator else 'Please confirm the following information:'}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Token: {token[:10]}...{token[-10:] if len(token) > 20 else token[10:]}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Email: {email}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Auth Type: {auth_type}{Style.RESET_ALL}")
    
    confirm = input(f"\n{Fore.YELLOW}{translator.get('manual_auth.proceed_prompt') if translator else 'Proceed? (y/N): '}{Style.RESET_ALL}").strip().lower()
    
    if confirm not in ["y", "yes"]:
        print(f"{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.operation_cancelled') if translator else 'Operation cancelled'}{Style.RESET_ALL}")
        return False
    
    # Initialize CursorAuth and update the database
    print(f"\n{Fore.CYAN}{EMOJI['UPDATE']} {translator.get('manual_auth.updating_database') if translator else 'Updating Cursor authentication database...'}{Style.RESET_ALL}")
    
    try:
        cursor_auth = CursorAuth(translator)
        result = cursor_auth.update_auth(
            email=email,
            access_token=token,
            refresh_token=token,
            auth_type=auth_type
        )
        
        if result:
            print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} {translator.get('manual_auth.auth_updated_successfully') if translator else 'Authentication information updated successfully!'}{Style.RESET_ALL}")
            return True
        else:
            print(f"\n{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.auth_update_failed') if translator else 'Failed to update authentication information'}{Style.RESET_ALL}")
            return False
            
    except Exception as e:
        print(f"\n{Fore.RED}{EMOJI['ERROR']} {translator.get('manual_auth.error', error=str(e)) if translator else f'Error: {str(e)}'}{Style.RESET_ALL}")
        return False

if __name__ == "__main__":
    # force to run with None
    main(None) 