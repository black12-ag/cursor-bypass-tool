import requests
import time
import re
from colorama import Fore, Style

EMOJI = {
    'MAIL': '📧',
    'SUCCESS': '✅',
    'ERROR': '❌',
    'WAIT': '⏳',
    'INFO': 'ℹ️'
}

class SimpleTempMail:
    """Simple temporary email using temp-mail.org API"""
    
    def __init__(self, translator=None):
        self.translator = translator
        self.base_url = "https://api.internal.temp-mail.io/api/v3"
        self.email = None
        self.token = None
    
    def generate_email(self):
        """Generate a new temporary email address"""
        try:
            # Create a new mailbox
            response = requests.post(
                f"{self.base_url}/email/new",
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            self.email = data.get('email')
            self.token = data.get('token')
            
            if self.email:
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Generated temp email: {self.email}{Style.RESET_ALL}")
                return self.email
            return None
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to generate email: {str(e)}{Style.RESET_ALL}")
            return None
    
    def get_messages(self):
        """Get all messages for the email"""
        try:
            if not self.email or not self.token:
                return []
            
            response = requests.get(
                f"{self.base_url}/email/{self.email}/messages",
                headers={'Authorization': f'Bearer {self.token}'},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            # Silent fail for polling
            return []
    
    def read_message(self, message_id):
        """Read a specific message"""
        try:
            response = requests.get(
                f"{self.base_url}/messages/{message_id}",
                headers={'Authorization': f'Bearer {self.token}'},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return None
    
    def get_verification_code(self, max_attempts=30, interval=2):
        """Wait for and extract verification code from Cursor email"""
        print(f"{Fore.CYAN}{EMOJI['WAIT']} Waiting for verification email...{Style.RESET_ALL}")
        
        for attempt in range(max_attempts):
            messages = self.get_messages()
            
            if messages:
                for msg in messages:
                    # Check if it's from Cursor
                    from_email = msg.get('from', '')
                    subject = msg.get('subject', '')
                    
                    if 'cursor' in from_email.lower() or 'cursor' in subject.lower():
                        # Read the full message
                        msg_id = msg.get('_id') or msg.get('id')
                        full_msg = self.read_message(msg_id)
                        
                        if full_msg:
                            # Extract verification code from body
                            body_html = full_msg.get('body_html', '')
                            body_text = full_msg.get('body_text', '') or full_msg.get('body', '')
                            body = body_html + ' ' + body_text
                            
                            # Try to find 6-digit code
                            match = re.search(r'\b(\d{6})\b', body)
                            if match:
                                code = match.group(1)
                                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Found verification code: {code}{Style.RESET_ALL}")
                                return code
            
            if attempt < max_attempts - 1:
                print(f"{Fore.YELLOW}{EMOJI['WAIT']} Attempt {attempt + 1}/{max_attempts}... waiting {interval}s{Style.RESET_ALL}")
                time.sleep(interval)
        
        print(f"{Fore.RED}{EMOJI['ERROR']} No verification code found after {max_attempts} attempts{Style.RESET_ALL}")
        return None


if __name__ == "__main__":
    # Test the temporary email service
    temp_mail = SimpleTempMail()
    email = temp_mail.generate_email()
    
    if email:
        print(f"\n{EMOJI['INFO']} Temporary email created: {email}")
        print(f"{EMOJI['INFO']} Waiting for messages...")
        
        code = temp_mail.get_verification_code()
        if code:
            print(f"\n{EMOJI['SUCCESS']} Verification code: {code}")
        else:
            print(f"\n{EMOJI['ERROR']} No verification code received")
