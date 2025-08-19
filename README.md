# 🚀 Cursor Bypass Tool

<div align="center">
  <p align="center">
    <img src="./images/logo.png" alt="Cursor Bypass Tool Logo" width="200" style="border-radius: 10px;"/>
  </p>
  
  <p align="center">
    <strong>A powerful development workflow enhancement tool</strong><br/>
    <em>Bypass Cursor limitations and optimize your coding experience</em>
  </p>

  <p align="center">
    <a href="https://github.com/black12-ag/cursor-bypass-tool/releases/latest">
      <img src="https://img.shields.io/github/v/release/black12-ag/cursor-bypass-tool?style=for-the-badge&logo=github&color=blue" alt="Latest Release"/>
    </a>
    <a href="https://github.com/black12-ag/cursor-bypass-tool/blob/main/LICENSE.md">
      <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
    </a>
    <a href="https://github.com/black12-ag/cursor-bypass-tool/stargazers">
      <img src="https://img.shields.io/github/stars/black12-ag/cursor-bypass-tool?style=for-the-badge&logo=star&color=yellow" alt="GitHub Stars"/>
    </a>
    <a href="https://github.com/black12-ag/cursor-bypass-tool/releases/latest">
      <img src="https://img.shields.io/github/downloads/black12-ag/cursor-bypass-tool/total?style=for-the-badge&logo=download&color=brightgreen" alt="Total Downloads"/>
    </a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square" alt="Cross Platform"/>
    <img src="https://img.shields.io/badge/Languages-15+-blue?style=flat-square" alt="Multi-language"/>
    <img src="https://img.shields.io/badge/Cursor-Latest%20Version-green?style=flat-square" alt="Cursor Support"/>
  </p>
</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Key Features](#-key-features)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage Guide](#-usage-guide)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)
- [License](#-license)

## 🎯 About

**Cursor Bypass Tool** is an advanced, open-source utility designed to enhance your development workflow by providing seamless integration with the Cursor IDE. This powerful tool offers developers unprecedented control over their coding environment, enabling them to bypass various limitations and optimize their productivity.

### 🌟 Why Choose Cursor Bypass Tool?

- **🔓 Freedom**: Bypass restrictive limitations and unlock full potential
- **🌐 Universal**: Works across Windows, macOS, and Linux platforms
- **🎨 Multilingual**: Support for 15+ languages with RTL support for Arabic
- **🔐 Secure**: Multiple authentication methods including OAuth integrations
- **⚡ Fast**: Optimized performance with intelligent caching
- **🛠️ Extensible**: Modular architecture for easy customization

### ⚠️ Important Usage Notes

- **🔑 Administrator Privileges**: Run with admin/sudo privileges for optimal performance
- **🔄 Keep Updated**: Always use the latest version for best compatibility
- **🧹 Clean Environment**: Clear browser cache and cookies before use
- **🌍 VPN Recommended**: Use VPN for new account creation to avoid restrictions

## ✨ Key Features

### 🔐 Authentication & Registration
*   **Google OAuth Authentication:** Register or log in using Google (Lifetime Access).
*   **GitHub OAuth Authentication:** Register or log in using GitHub (Lifetime Access).
*   **Manual Authentication:** Input custom tokens and email for authentication.
*   **Account Manager:** Save and manage account information automatically.
*   **Automatic Registration:** Easily register new Cursor memberships.
*   **Email Tabs Support:** Advanced email handling with temporary email providers.

### ⚙️ Configuration & Management
*   **Machine ID Reset:** Resets Cursor's machine ID and configuration.
*   **Machine ID Backup & Restore:** Create backups and restore previous machine IDs.
*   **Token Limit Bypass:** Bypass various token limitations.
*   **Version Check Bypass:** Bypass version compatibility checks.
*   **Auto-Update Management:** Control automatic updates and version checks.
*   **Account Deletion:** Option to remove associated accounts from Cursor.

### 🌍 Multi-language & Accessibility
*   **Multi-language Support:** UI available in 15+ languages including Arabic, Chinese, Japanese, Italian, etc.
*   **Arabic Language Support:** Full RTL (Right-to-Left) text support for Arabic.
*   **Automatic Language Detection:** Detects system language automatically.
*   **Cross-Platform:** Supports Windows, macOS, and Linux.

### 🔧 Advanced Features
*   **Source Map Support:** Advanced cursor source mapping for version 0.50.5+.
*   **Chrome Profile Selection:** Select specific Chrome profiles for authentication.
*   **Enhanced Configuration:** Extensive configuration options with language caching.
*   **User Authorization Check:** Verify user authorization status.

## 💻 System Support

| Operating System | Architecture  | Supported |
| :--------------- | :------------ | :-------: |
| Windows          | x64 / x86     |     ✅     |
| macOS            | Intel / Apple Silicon |     ✅     |
| Linux            | x64 / ARM64   |     ✅     |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Administrator/sudo privileges (recommended)
- Active internet connection
- Cursor IDE installed

### Quick Installation

Choose your platform and run the appropriate command:

<details>
<summary><strong>🐧 Linux / macOS</strong></summary>

```bash
# One-line installation
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

**Alternative: Manual Download**
```bash
# Download and extract
wget https://github.com/black12-ag/cursor-bypass-tool/archive/main.zip
unzip main.zip && cd cursor-bypass-tool-main
python3 -m pip install -r requirements.txt
python3 main.py
```
</details>

<details>
<summary><strong>🪟 Windows</strong></summary>

**PowerShell (Recommended)**
```powershell
# Run as Administrator
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.ps1 | iex
```

**Manual Installation**
```cmd
# Download from GitHub
# Extract the ZIP file
# Open Command Prompt as Administrator
cd cursor-bypass-tool-main
pip install -r requirements.txt
python main.py
```
</details>

<details>
<summary><strong>🏗️ Arch Linux (AUR)</strong></summary>

```bash
# Using yay
yay -S cursor-bypass-tool-git

# Using paru
paru -S cursor-bypass-tool-git

# Manual build
git clone https://aur.archlinux.org/cursor-bypass-tool-git.git
cd cursor-bypass-tool-git
makepkg -si
```
</details>

### Quick Reset Scripts

For users who only need machine ID reset functionality:

```bash
# Linux/macOS - Quick reset
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.sh | sudo bash

# Windows - Quick reset
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.ps1 | iex
```

## 🏃‍♂️ Quick Start

1. **Launch the tool** with administrator privileges
2. **Select your language** from the available options
3. **Choose authentication method**:
   - Google OAuth (recommended)
   - GitHub OAuth
   - Manual token input
4. **Follow the on-screen instructions**
5. **Enjoy enhanced Cursor experience**

### First Run Checklist
- [ ] Close Cursor IDE completely
- [ ] Run tool with admin/sudo privileges
- [ ] Clear browser cache and cookies
- [ ] Use VPN for account creation (recommended)
- [ ] Keep tool updated to latest version

## ⚙️ Configuration

The tool automatically creates a configuration directory at:
- **Windows**: `%USERPROFILE%\Documents\.cursor-bypass-tool\`
- **macOS**: `~/Documents/.cursor-bypass-tool/`
- **Linux**: `~/Documents/.cursor-bypass-tool/`

<details>
<summary><strong>📝 Configuration File Examples</strong></summary>

**config.ini Structure:**
```ini
[Browser]
default_browser = chrome
chrome_path = /path/to/chrome
# ... other browser settings

[Timing]
min_random_time = 0.1
max_random_time = 0.8
max_timeout = 160
# ... timing configurations

[Language]
current_language = en
fallback_language = en
auto_update_languages = True

[OAuth]
timeout = 120
max_attempts = 3

[Utils]
enabled_update_check = True
enabled_account_info = True
```
</details>

## 📖 Usage Guide

### Main Menu Options

| Option | Description | Access Level |
|:-------|:-----------:|:-------------:|
| 🔐 **Google OAuth** | Register/login with Google account | Standard |
| 🐙 **GitHub OAuth** | Register/login with GitHub account | Standard |
| ⚙️ **Manual Auth** | Custom token authentication | Advanced |
| 💾 **Account Manager** | Manage saved accounts | Standard |
| 🔄 **Reset Machine ID** | Reset system identification | Admin |
| 💾 **Backup/Restore** | Manage machine ID backups | Admin |
| 🌍 **Language Settings** | Change interface language | Standard |

### Authentication Workflows

<details>
<summary><strong>🔑 OAuth Authentication</strong></summary>

1. Select OAuth method (Google/GitHub)
2. Browser window opens automatically
3. Complete authentication in browser
4. Tool automatically captures tokens
5. Account information saved for future use
</details>

<details>
<summary><strong>⚙️ Manual Authentication</strong></summary>

1. Select "Manual Custom Auth"
2. Enter access token directly
3. Choose authentication type (Auth_0/Google/GitHub)
4. Generate or enter email address
5. Validate and save configuration
</details>

## 🔧 Troubleshooting

### Common Issues & Solutions

<details>
<summary><strong>❌ Permission Errors</strong></summary>

**Problem**: Tool can't access system files
**Solution**: 
- Windows: Run as Administrator
- macOS/Linux: Use `sudo` command
- Check file permissions in config directory
</details>

<details>
<summary><strong>🚫 "User not authorized" Error</strong></summary>

**Problem**: Email flagged or banned by Cursor
**Solution**:
- Use different email provider (avoid temporary emails)
- Clear browser data completely
- Try with VPN from different location
- Use established email account
</details>

<details>
<summary><strong>🔄 Browser Automation Issues</strong></summary>

**Problem**: Browser doesn't open or respond
**Solution**:
- Update browser to latest version
- Check browser path in config
- Disable browser extensions
- Clear browser cache and cookies
</details>

<details>
<summary><strong>🌐 Network Connectivity</strong></summary>

**Problem**: Tool can't connect to servers
**Solution**:
- Check internet connection
- Disable VPN temporarily
- Check firewall settings
- Verify DNS resolution
</details>

### Debug Mode

Enable debug mode for detailed logging:
```bash
python main.py --debug
```

### Log Files

Check log files for detailed error information:
- **Windows**: `%USERPROFILE%\Documents\.cursor-bypass-tool\logs\`
- **macOS/Linux**: `~/Documents/.cursor-bypass-tool/logs/`

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### 🐛 Bug Reports
1. Check existing issues first
2. Use the bug report template
3. Include system information and logs
4. Provide steps to reproduce

### 🚀 Feature Requests
1. Search existing feature requests
2. Use the feature request template
3. Explain use case and benefits
4. Provide implementation suggestions

### 💻 Code Contributions
1. Fork the repository
2. Create a feature branch
3. Follow coding standards
4. Add tests for new features
5. Update documentation
6. Submit pull request

### 🌍 Translations
Help translate the tool into your language:
1. Copy `locales/en.json` as template
2. Translate all strings
3. Test with your language
4. Submit translation via PR

## 📞 Support

### 💬 Community Support
- **GitHub Issues**: [Report bugs and request features](https://github.com/black12-ag/cursor-bypass-tool/issues)
- **Discussions**: [Community discussions and Q&A](https://github.com/black12-ag/cursor-bypass-tool/discussions)

### 📧 Direct Support
For urgent issues or private inquiries, contact the development team.

### 💝 Financial Support

If this tool has helped improve your development workflow, consider supporting its continued development:

<div align="center">
  <p><strong>Support Development</strong></p>
  
  <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=muay01111@gmail.com&item_name=Support+Cursor+Bypass+Tool&currency_code=USD">
    <img src="https://img.shields.io/badge/PayPal-Donate-blue?style=for-the-badge&logo=paypal" alt="Donate via PayPal"/>
  </a>
  
  <a href="https://skrill.me/rq/Munir%20Ayub/10/USD?key=1VqVrQ2Ly1LN5JmgKpAlzoMGBEg">
    <img src="https://img.shields.io/badge/Skrill-Send%20%2410-orange?style=for-the-badge" alt="Send via Skrill"/>
  </a>
</div>

## 📈 Project Statistics

<div align="center">
  <img src="https://api.star-history.com/svg?repos=black12-ag/cursor-bypass-tool&type=Date" alt="Star History Chart" width="600"/>
</div>

## 🔒 Security & Privacy

- **🔐 Local Processing**: All operations performed locally
- **🚫 No Data Collection**: Tool doesn't collect personal information
- **🔒 Secure Authentication**: Uses industry-standard OAuth protocols
- **🛡️ Open Source**: Code is fully auditable and transparent

## ⚠️ Disclaimer

This tool is provided for educational and research purposes only. Users assume all responsibility for compliance with applicable terms of service and local laws. The developers are not responsible for any consequences arising from the use of this software.

**Use responsibly and respect service provider terms.**

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for complete details.

```
MIT License - Free to use, modify, and distribute
Copyright (c) 2024 Cursor Bypass Tool Contributors
```

---

<div align="center">
  <p>
    <strong>Made with ❤️ by the open source community</strong><br/>
    <sub>⭐ Star this repo if it helped you! ⭐</sub>
  </p>
  
  <p>
    <a href="#-cursor-bypass-tool">Back to Top ↑</a>
  </p>
</div>
