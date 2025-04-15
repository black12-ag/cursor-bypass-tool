# ➤ Cursor Bypass Tool

<div align="center">
  <p align="center">
    <img src="./images/logo.png" alt="Cursor Bypass Tool Logo" width="200" style="border-radius: 6px;"/>
  </p>
  <p align="center">
    [![Release](https://img.shields.io/github/v/release/black12-ag/cursor-bypass-tool)](https://github.com/black12-ag/cursor-bypass-tool/releases/latest)
    [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)
    [![Stars](https://img.shields.io/github/stars/black12-ag/cursor-bypass-tool)](https://github.com/black12-ag/cursor-bypass-tool/stargazers)
    [![Downloads](https://img.shields.io/github/downloads/black12-ag/cursor-bypass-tool/total)](https://github.com/black12-ag/cursor-bypass-tool/releases/latest)
    <a href="https://buymeacoffee.com/black12" target="_blank"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-FFDA33"></a>
  </p>
  <h4>Supports Latest Cursor Version</h4>
</div>

A powerful tool to enhance your development workflow by bypassing Cursor limitations. It helps with account registration, data resets, and more.

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

*   **Permission Errors:** Ensure you run the script with administrator privileges (Windows) or `sudo` (Linux/macOS).
*   **'User is not authorized' Error:** This usually means the email used (especially temporary ones) was flagged or banned by Cursor. Try using a different, non-temporary email provider.
*   **Script Issues:** Make sure Cursor application is completely closed before running the tool.

## 🤝 Contribution

Issues and Pull Requests are welcome! Feel free to contribute to the project.

## 📜 Disclaimer

This tool is provided for educational and research purposes only. The user assumes all responsibility for any consequences arising from its use. Please respect Cursor's terms of service.

## ☕ Support the Project

If you find this tool helpful, consider supporting its development:

<p align="center">
  <a href="https://www.buymeacoffee.com/black12" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
  </a>
</p>

## ⭐ Star History

<div align="center">
  [![Star History Chart](https://api.star-history.com/svg?repos=black12-ag/cursor-bypass-tool&type=Date)](https://star-history.com/#black12-ag/cursor-bypass-tool&Date)
</div>

## 📝 License

This project is licensed under the [MIT License](LICENSE.md).
