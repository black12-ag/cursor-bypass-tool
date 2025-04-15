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

<h4>Support Latest 0.48.x Version | 支持最新 0.48.x 版本</h4>

A powerful tool that enhances your development workflow by bypassing Cursor limitations. This tool registers accounts with custom emails, supports Google and GitHub account registrations, resets and wipes Cursor data and hardware info.

Supports Windows, macOS and Linux.

For optimal performance, run with privileges and always stay up to date.

Always clean your browser's cache and cookies. If possible, use a VPN to create new accounts.


這是一個自動化工具，自動註冊，支持 Windows macOS 和 Linux 系統，完成 Auth 驗證，重置 Cursor 的配置。

<p align="center">
  <img src="./images/pro_2025-04-05_18-47-56.png" alt="new" width="800" style="border-radius: 6px;"/><br>
</p>

##### If you don't have browser, you can download it from 
[Google Chrome](https://www.google.com/intl/en_pk/chrome/) or [Opera](https://www.opera.com/download) or [Edge](https://www.microsoft.com/en-us/edge) or [Firefox](https://www.mozilla.org/en-US/firefox/new/) or [Brave](https://www.brave.com/download/)

##### 如果沒有瀏覽器，可以從
[Google Chrome](https://www.google.com/intl/en_pk/chrome/) 或 [Opera](https://www.opera.com/download) 或 [Edge](https://www.microsoft.com/en-us/edge) 或 [Firefox](https://www.mozilla.org/en-US/firefox/new/) 或 [Brave](https://www.brave.com/download/) 下載

</div>

## 🔄 Change Log | 更新日志

[Watch Change Log | 查看更新日志](CHANGELOG.md)

## ✨ Features | 功能特點

* 🌟 Google OAuth Authentication with Lifetime Access<br>使用 Google OAuth 認證（終身訪問）<br>

* ⭐ GitHub OAuth Authentication with Lifetime Access<br>使用 GitHub OAuth 認證（終身訪問）<br>

* Automatically register Cursor membership<br>自動註冊 Cursor 會員<br>

* Support Windows macOS and Linux systems<br>支持 Windows、macOS 和 Linux 系統<br>

* Complete Auth verification<br>完成 Auth 驗證<br>

* Reset Cursor's configuration<br>重置 Cursor 的配置<br>

* Delete Cursor Google Account<br>删除 Cursor Google 账号<br>

* Multi-language support (English, 简体中文, 繁體中文, Vietnamese)<br>多語言支持（英文、简体中文、繁體中文、越南語）<br>

## 💻 System Support | 系統支持

| Windows |  x64  | ✅ | macOS |     Intel     | ✅ |
|:-------:|:-----:|:-:|:-----:|:-------------:|:-:|
| Windows |  x86  | ✅ | macOS | Apple Silicon | ✅ |
|  Linux  |  x64  | ✅ | Linux |      x86      | ✅ |
|  Linux  | ARM64 | ✅ | Linux |     ARM64     | ✅ |

## 👀 How to use | 如何使用

<details open>
<summary><b>⭐ Auto Run Script | 腳本自動化運行</b></summary>

### **Linux/macOS**

```bash
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

### **Archlinux**

Install via [AUR](https://aur.archlinux.org/packages/cursor-bypass-tool-git)

```bash
yay -S cursor-bypass-tool-git
```

### **Windows**

```powershell
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/install.ps1 | iex
```

</details>

<details>
<summary><b>⭐ Manual Reset Machine | 手動運行重置機器</b></summary>

### **Linux/macOS**

```bash
curl -fsSL https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.sh | sudo bash
```

### **Windows**

```powershell
irm https://raw.githubusercontent.com/black12-ag/cursor-bypass-tool/main/scripts/reset.ps1 | iex
```

</details>

If you want to stop the script, please press Ctrl+C<br>要停止腳本，請按 Ctrl+C

## ❗ Note | 注意事項

📝 Config | 文件配置
`Win / Macos / Linux Path | 路徑 [Documents/.Cursor Bypass Tool/config.ini]`
<details>
<summary><b>⭐ Config | 文件配置</b></summary>

```
[Chrome]
# Default Google Chrome Path | 默認Google Chrome 遊覽器路徑
chromepath = C:\Program Files\Google/Chrome/Application/chrome.exe

[Turnstile]
# Handle Turnstile Wait Time | 等待人機驗證時間
handle_turnstile_time = 2
# Handle Turnstile Wait Random Time (must merge 1-3 or 1,3) | 等待人機驗證隨機時間（必須是 1-3 或者 1,3 這樣的組合）
handle_turnstile_random_time = 1-3

[OSPaths]
# Storage Path | 存儲路徑
storage_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/storage.json
# SQLite Path | SQLite路徑
sqlite_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/state.vscdb
# Machine ID Path | 機器ID路徑
machine_id_path = /Users/username/Library/Application Support/Cursor/machineId
# For Linux users: ~/.config/cursor/machineid

[Timing]
# Min Random Time | 最小隨機時間
min_random_time = 0.1
# Max Random Time | 最大隨機時間
max_random_time = 0.8
# Page Load Wait | 頁面加載等待時間
page_load_wait = 0.1-0.8
# Input Wait | 輸入等待時間
input_wait = 0.3-0.8
# Submit Wait | 提交等待時間
submit_wait = 0.5-1.5
# Verification Code Input | 驗證碼輸入等待時間
verification_code_input = 0.1-0.3
# Verification Success Wait | 驗證成功等待時間
verification_success_wait = 2-3
# Verification Retry Wait | 驗證重試等待時間
verification_retry_wait = 2-3
# Email Check Initial Wait | 郵件檢查初始等待時間
email_check_initial_wait = 4-6
# Email Refresh Wait | 郵件刷新等待時間
email_refresh_wait = 2-4
# Settings Page Load Wait | 設置頁面加載等待時間
settings_page_load_wait = 1-2
# Failed Retry Time | 失敗重試時間
failed_retry_time = 0.5-1
# Retry Interval | 重試間隔
retry_interval = 8-12
# Max Timeout | 最大超時時間
max_timeout = 160

[Utils]
# Check Update | 檢查更新
check_update = True
# Show Account Info | 顯示賬號信息
show_account_info = True
```

</details>

* Use administrator privileges to run the script <br>請使用管理員身份運行腳本

* Confirm that Cursor is closed before running the script <br>請確保在運行腳本前已經關閉 Cursor<br>

* This tool is only for learning and research purposes <br>此工具僅供學習和研究使用<br>

* Please comply with the relevant software usage terms when using this tool <br>使用本工具時請遵守相關軟件使用條款

## 🚨 Common Issues | 常見問題

|                   如果遇到權限問題，請確保：                    |                   此腳本以管理員身份運行                    |
|:--------------------------------------------------:|:------------------------------------------------:|
| If you encounter permission issues, please ensure: | This script is run with administrator privileges |
| Error 'User is not authorized' | This means your account was banned for using temporary (disposal) mail. Ensure using a non-temporary mail service |

## 🤩 Contribution | 貢獻

歡迎提交 Issue 和 Pull Request！

## 📩 Disclaimer | 免責聲明

本工具僅供學習和研究使用，使用本工具所產生的任何後果由使用者自行承擔。 <br>

This tool is only for learning and research purposes, and any consequences arising from the use of this tool are borne
by the user.

## 💰 Buy Me a Coffee | 請我喝杯咖啡

<p align="center">
  <a href="https://www.buymeacoffee.com/black12" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
  </a>
</p>

## ⭐ Star History | 星星數

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=black12-ag/cursor-bypass-tool&type=Date)](https://star-history.com/#black12-ag/cursor-bypass-tool&Date)

</div>

## 📝 License | 授權

本項目採用 [MIT License](https://opensource.org/licenses/MIT) 授權。
Please refer to the [LICENSE](LICENSE.md) file for details.
