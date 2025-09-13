# ➤ Cursor Bypass Tool

<div align="center">
  <p align="center">
    <img src="./images/munir_tool.png" alt="Munir Bypass Tool Logo" width="200" style="border-radius: 6px;"/>
  </p>
  <p align="center">
    [![Release](https://img.shields.io/github/v/release/black12-ag/cursor-bypass-tool)](https://github.com/black12-ag/cursor-bypass-tool/releases/latest)
    [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)
    [![Stars](https://img.shields.io/github/stars/black12-ag/cursor-bypass-tool)](https://github.com/black12-ag/cursor-bypass-tool/stargazers)
    [![Downloads](https://img.shields.io/github/downloads/black12-ag/cursor-bypass-tool/total)](https://github.com/black12-ag/cursor-bypass-tool/releases/latest)
  </p>
  <h4>Supports Latest Cursor Version</h4>
</div>

A powerful tool to enhance your development workflow by bypassing Cursor limitations. It helps with account registration, data resets, and more.

> 🎉 **LATEST UPDATE (Sept 2024):** Fixed installation issues that were causing downloads to fail for YouTube users. The install script now works reliably across all supported platforms!

<!-- 
  **TODO:** Replace this comment with your new image. 
  Make sure the image is in the 'images' directory and named appropriately (e.g., munir_tool.png).
  Example: <img src="./images/munir_tool.png" alt="Munir Bypass Tool" width="800" style="border-radius: 6px;"/>
-->

**Important Notes:**
*   For optimal performance, run with administrator/sudo privileges.
*   Always keep the tool updated to the latest version.
*   Clean your browser's cache and cookies before use.
*   Using a VPN for new account creation is recommended.
*   ⚠️ **For YouTube users:** Make sure to copy ONLY the command (not the comment starting with `#`)

## ✨ Features

*   **Google OAuth Authentication:** Register or log in using Google (Lifetime Access).
*   **GitHub OAuth Authentication:** Register or log in using GitHub (Lifetime Access).
*   **Automatic Registration:** Easily register new Cursor memberships.
*   **Cross-Platform:** Supports Windows, macOS, and Linux.
*   **Auth Verification:** Completes the necessary authentication steps.
*   **Configuration Reset:** Resets Cursor's settings and machine ID.
*   **Account Deletion:** Option to remove the associated Google account from Cursor.
*   **Multi-language Support:** UI available in multiple languages (selected automatically or manually).

## 💻 System Support

| Operating System | Architecture  | Supported |
| :--------------- | :------------ | :-------: |
| Windows          | x64 / x86     |     ✅     |
| macOS            | Intel / Apple Silicon |     ✅     |
| Linux            | x64 / ARM64   |     ✅     |

## 🚀 Installation & Usage

Choose the script for your operating system:

<details open>
<summary><strong>Quick Install & Run Scripts</strong></summary>

### Linux / macOS

```bash
# Download, make executable, and run
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

> 📝 **Note:** Copy the command above exactly as shown. Do NOT copy any comments (lines starting with `#`) that might appear in tutorials or videos.

### Arch Linux (AUR)

```bash
# Install using an AUR helper like yay
yay -S cursor-bypass-tool-git
```

### Windows (PowerShell)

```powershell
# Download and run the installation script
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.ps1 | iex
```

</details>

<details>
<summary><strong>Manual Machine Reset Scripts</strong></summary>

Use these scripts if you only need to reset Cursor's machine ID and configuration without running the full tool.

### Linux / macOS

```bash
# Download and run the reset script with sudo
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.sh | sudo bash
```

### Windows (PowerShell)

```powershell
# Download and run the reset script
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.ps1 | iex
```

</details>

**Stopping the Script:** Press `Ctrl+C` to stop the tool if needed.

## 🎬 Installation Demo

<details>
<summary><strong>What to Expect During Installation</strong></summary>

### macOS/Linux Installation Process

When you run the installation command, here's what you'll see:

```bash
$ curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh

   ███╗   ███╗██╗   ██╗███╗   ██╗██╗██████╗     
   ████╗ ████║██║   ██║████╗  ██║██║██╔══██╗    
   ██╔████╔██║██║   ██║██╔██╗ ██║██║██████╔╝    
   ██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██╗    
   ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██║  ██║    
   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝    

ℹ️ Checking latest version...
✅ Found latest version: 1.0.0
ℹ️ Detected macOS Intel architecture
ℹ️ No existing installation file found, starting download...
ℹ️ Downloading to /Users/username/Downloads...
ℹ️ Trying generic download first: https://github.com/black12-ag/cursor-bypass-tool/releases/download/v1.0.0/CursorFreeVIP_1.0.0_mac
✅ Generic file exists, downloading...
✅ Download completed!
ℹ️ Program downloaded to: /Users/username/Downloads/CursorFreeVIP_1.0.0_mac
⚠️ Requesting administrator privileges...
ℹ️ Starting program with sudo...
Password: [Enter your macOS password]
```

### macOS Security Notice

If you see `Killed: 9`, this is **normal** - macOS Gatekeeper is blocking unsigned binaries. To fix:

```bash
# Remove quarantine attribute (use the actual filename from your Downloads)
sudo xattr -rd com.apple.quarantine ~/Downloads/CursorFreeVIP_1.0.0_mac*

# Run the tool (use the actual filename from your Downloads)
sudo ~/Downloads/CursorFreeVIP_1.0.0_mac*
```

> 📝 **Tip:** The script now downloads the most compatible version for your system automatically.

### Expected Program Interface

Once running, you'll see the main menu:

```
🚀 MUNIR Pro Version Activator v1.9.05
Author: MUNIR KABIR
Press 8 to change language | 按下 8 键切换语言

📋 Main Menu:
──────────────────────────────────────────────────────────────
0. ❌ Exit                           9. 🔄 Disable Auto Update
1. 🔄 Reset Machine ID              10. 🔄 Total Reset
2. ✅ Register Account (Legacy)     11. 🤝 Contributors
3. 🌟 Register Google Account 🚀   12. ⚙️ Configuration
4. ⭐ Register GitHub Account 🚀    13. ⚙️ Chrome Profile
5. ✅ Manual Registration           14. ❌ Delete Google Account
6. 🔄 GitHub Register (Beta)        15. 🔄 Bypass Version Check
7. ❌ Quit Cursor                   16. 🔄 Check Authorization
8. 🌐 Select Language               17. 🔄 Bypass Token Limit
──────────────────────────────────────────────────────────────

➜ Enter choice (0-17):
```

### Success Indicators

- ✅ **Green checkmarks** indicate successful operations
- 🔄 **Blue symbols** show processes in progress  
- ⚠️ **Yellow warnings** are informational
- ❌ **Red X** indicates errors or exit options

</details>

## ⚙️ Configuration

The tool uses a configuration file (`config.ini`) stored in your `Documents/.Cursor Bypass Tool/` directory. You can customize settings related to browser paths, timing, and other utilities.

<details>
<summary><strong>Example `config.ini` Settings</strong></summary>

```ini
[Chrome]
# Path to your Google Chrome executable
chromepath = C:\Program Files\Google\Chrome\Application\chrome.exe

[Turnstile]
# Time delays for handling CAPTCHAs
handle_turnstile_time = 2
handle_turnstile_random_time = 1-3

[OSPaths]
# Paths to Cursor's internal files (usually detected automatically)
storage_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/storage.json
sqlite_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/state.vscdb
machine_id_path = /Users/username/Library/Application Support/Cursor/machineId
# Linux path: ~/.config/cursor/machineid

[Timing]
# Various time delays (in seconds) for browser automation steps
min_random_time = 0.1
max_random_time = 0.8
# ... other timing settings ...
max_timeout = 160

[Utils]
# Enable/disable checking for updates on startup
check_update = True
# Show account information on startup
show_account_info = True
```

</details>

## ❓ Troubleshooting & Common Issues

### Installation Issues
*   **"zsh: command not found: #" Error:** This happens when you accidentally copy a comment line starting with `#`. Make sure to copy ONLY the actual command without any comments.
*   **"Download link does not exist" Error:** This was a known issue that has been fixed. Update to the latest version by running the install script again.
*   **Download Interrupted/Failed:** The install script now automatically tries different download sources. If issues persist, check your internet connection.
*   **Binary Path Issues:** Fixed in the latest version - the script now properly handles file paths when falling back to generic versions.

### macOS Issues
*   **"Killed: 9" Error:** macOS Gatekeeper blocks unsigned binaries. Fix with:
    ```bash
    sudo xattr -rd com.apple.quarantine ~/Downloads/CursorFreeVIP_*_mac_*
    sudo ~/Downloads/CursorFreeVIP_*_mac_*
    ```
*   **"Cannot be opened" Error:** Go to System Preferences → Security & Privacy → Allow the app, then retry.
*   **Permission Denied:** Ensure you run with `sudo` and enter your password when prompted.

### General Issues
*   **Permission Errors:** Ensure you run the script with administrator privileges (Windows) or `sudo` (Linux/macOS).
*   **'User is not authorized' Error:** This usually means the email used (especially temporary ones) was flagged or banned by Cursor. Try using a different, non-temporary email provider.
*   **Script Issues:** Make sure Cursor application is completely closed before running the tool.
*   **Python Version Error:** If you see syntax errors, you need Python 3.10+ or use the pre-built binaries instead.
*   **Network Issues:** Ensure stable internet connection. Some features require accessing external services.

## 🤝 Contribution

Issues and Pull Requests are welcome! Feel free to contribute to the project.

## 📜 Disclaimer

This tool is provided for educational and research purposes only. The user assumes all responsibility for any consequences arising from its use. Please respect Cursor's terms of service.

## ☕ Support the Project

If you find this tool helpful, consider supporting its development via:

*   **Skrill:** [Send 10 USD via Skrill](https://skrill.me/rq/Munir%20Ayub/10/USD?key=1VqVrQ2Ly1LN5JmgKpAlzoMGBEg)
*   **PayPal:** [Donate via PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=muay01111@gmail.com&item_name=Support+Cursor+Bypass+Tool&currency_code=USD)

<p align="center">
  <a href="#binance-payment"> <!-- TODO: Replace #binance-payment with your actual Binance payment link if available -->
    <img src="./images/binance_qr.png" alt="Scan Binance QR to Pay Munir_kabir" width="150"/>
  </a>
  <br/>Scan with Binance App to pay Munir_kabir
</p>

## ⭐ Star History

<div align="center">
  [![Star History Chart](https://api.star-history.com/svg?repos=black12-ag/cursor-bypass-tool&type=Date)](https://star-history.com/#black12-ag/cursor-bypass-tool&Date)
</div>

## 📝 License

This project is licensed under the [MIT License](LICENSE.md).
