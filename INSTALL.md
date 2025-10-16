# Installation Guide

Complete installation instructions for Windows, macOS, and Linux.

---

## 📋 Prerequisites

Before installing, make sure you have:
- Python 3.8 or higher
- Git (optional, for cloning)
- Admin/sudo privileges
- Internet connection

---

## 🪟 Windows Installation

### Method 1: Using Git

1. **Open PowerShell or Command Prompt**
   ```powershell
   # Navigate to where you want to install
   cd C:\Users\YourUsername\Desktop
   ```

2. **Clone the repository**
   ```powershell
   git clone https://github.com/black12-ag/cursor-bypass-tool.git
   cd cursor-bypass-tool
   ```

3. **Install Python dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the tool**
   ```powershell
   python main.py
   ```

### Method 2: Download ZIP

1. Download the ZIP file from GitHub
2. Extract to your desired location
3. Open PowerShell in the extracted folder
4. Run:
   ```powershell
   pip install -r requirements.txt
   python main.py
   ```

### Troubleshooting Windows

**"pip is not recognized"**
```powershell
python -m pip install -r requirements.txt
```

**Need admin privileges**
- Right-click PowerShell → "Run as Administrator"

**Python not found**
- Download from [python.org](https://www.python.org/downloads/)
- Check "Add Python to PATH" during installation

---

## 🍎 macOS Installation

### Using Terminal

1. **Open Terminal** (Cmd + Space, type "Terminal")

2. **Navigate to Desktop**
   ```bash
   cd ~/Desktop
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/black12-ag/cursor-bypass-tool.git
   cd cursor-bypass-tool
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run the tool**
   ```bash
   python3 main.py
   ```

### Troubleshooting macOS

**"command not found: python3"**
- Install Python from [python.org](https://www.python.org/downloads/)
- Or use Homebrew: `brew install python3`

**Permission denied**
```bash
chmod +x main.py
python3 main.py
```

**Need sudo for some operations**
```bash
sudo python3 main.py
```

---

## 🐧 Linux Installation

### Ubuntu/Debian

```bash
# Update package list
sudo apt update

# Install Python and pip (if not installed)
sudo apt install python3 python3-pip git

# Clone repository
cd ~
git clone https://github.com/black12-ag/cursor-bypass-tool.git
cd cursor-bypass-tool

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Fedora/RHEL/CentOS

```bash
# Install Python and pip
sudo dnf install python3 python3-pip git

# Clone repository
cd ~
git clone https://github.com/black12-ag/cursor-bypass-tool.git
cd cursor-bypass-tool

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Arch Linux

```bash
# Install Python and pip
sudo pacman -S python python-pip git

# Clone repository
cd ~
git clone https://github.com/black12-ag/cursor-bypass-tool.git
cd cursor-bypass-tool

# Install dependencies
pip3 install -r requirements.txt

# Run the tool
python3 main.py
```

### Troubleshooting Linux

**"No module named 'xxx'"**
```bash
pip3 install --user -r requirements.txt
```

**Permission issues**
```bash
sudo python3 main.py
```

**Display issues (headless server)**
```bash
export DISPLAY=:0
python3 main.py
```

---

## 🔧 Verifying Installation

After installation, verify everything works:

1. **Check Python version**
   ```bash
   python3 --version
   # Should show Python 3.8 or higher
   ```

2. **Check installed packages**
   ```bash
   pip3 list | grep -E "(colorama|DrissionPage|selenium)"
   ```

3. **Run the tool**
   ```bash
   python3 main.py
   ```

   You should see the MUNIR logo and menu.

---

## 📦 Dependencies

The tool will install these Python packages:

- `colorama` - Terminal colors
- `DrissionPage` - Browser automation
- `selenium` - Web driver
- `requests` - HTTP requests
- `psutil` - Process management
- `Faker` - Generate fake data
- `python-dotenv` - Environment variables
- `watchdog` - File monitoring
- `arabic-reshaper` - Arabic text support
- `python-bidi` - Bidirectional text
- `webdriver_manager` - Auto driver management

---

## 🚀 Quick Start After Installation

```bash
# Navigate to project directory
cd cursor-bypass-tool

# Run the tool
python3 main.py    # macOS/Linux
python main.py     # Windows

# Follow the on-screen menu:
# 1. Reset Machine ID
# 2. Register new account (Automatic or Manual)
# 3. Total reset
```

---

## 🆘 Getting Help

If you encounter issues:

1. **Check the [FAQ](README.md#-faq) in README**
2. **Read the [Manual Registration Guide](MANUAL_REGISTRATION_GUIDE.md)**
3. **Open an issue on [GitHub](https://github.com/black12-ag/cursor-bypass-tool/issues)**

---

## ✅ Post-Installation

After successful installation:

1. ✅ Run `python3 main.py` to verify
2. ✅ The tool auto-configures for your OS
3. ✅ Config stored in `~/Documents/.cursor-free-vip/`
4. ✅ Ready to use!

---

**Made with ❤️ by Munir** | Version 1.0.4
