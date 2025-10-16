# Cursor Bypass Tool Installer for Windows
# Version 1.0.4 by Munir

# Colors
$Host.UI.RawUI.ForegroundColor = "Cyan"

# Logo
function Show-Logo {
    Write-Host @"
  ███╗   ███╗██╗   ██╗███╗   ██╗██╗██████╗ 
  ████╗ ████║██║   ██║████╗  ██║██║██╔══██╗
  ██╔████╔██║██║   ██║██╔██╗ ██║██║██████╔╝
  ██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██╗
  ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██║  ██║
  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
"@ -ForegroundColor Cyan
    Write-Host "Cursor Bypass Tool v1.0.4" -ForegroundColor Yellow
    Write-Host "Customized by Munir" -ForegroundColor Green
    Write-Host ""
}

# Check if Python is installed
function Test-Python {
    Write-Host "ℹ️  Checking Python installation..." -ForegroundColor Cyan
    
    $pythonCmd = $null
    
    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        $pythonCmd = "python3"
        $version = & python3 --version 2>&1
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        $pythonCmd = "python"
        $version = & python --version 2>&1
        if ($version -notmatch "Python 3\.") {
            Write-Host "❌ Python 3 is required but not found" -ForegroundColor Red
            Write-Host "Please install Python 3.8 or higher from https://www.python.org/" -ForegroundColor Yellow
            exit 1
        }
    }
    else {
        Write-Host "❌ Python is not installed" -ForegroundColor Red
        Write-Host "Please install Python 3.8 or higher from https://www.python.org/" -ForegroundColor Yellow
        Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
        exit 1
    }
    
    Write-Host "✅ Python found: $version" -ForegroundColor Green
    return $pythonCmd
}

# Check if pip is installed
function Test-Pip {
    param($pythonCmd)
    
    Write-Host "ℹ️  Checking pip installation..." -ForegroundColor Cyan
    
    if (Get-Command pip3 -ErrorAction SilentlyContinue) {
        Write-Host "✅ pip3 found" -ForegroundColor Green
        return "pip3"
    }
    elseif (Get-Command pip -ErrorAction SilentlyContinue) {
        Write-Host "✅ pip found" -ForegroundColor Green
        return "pip"
    }
    else {
        Write-Host "⚠️  pip not found, trying to install..." -ForegroundColor Yellow
        & $pythonCmd -m ensurepip --default-pip
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to install pip" -ForegroundColor Red
            exit 1
        }
        Write-Host "✅ pip installed" -ForegroundColor Green
        return "$pythonCmd -m pip"
    }
}

# Check if git is installed
function Test-Git {
    Write-Host "ℹ️  Checking git installation..." -ForegroundColor Cyan
    
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Host "⚠️  git not found" -ForegroundColor Yellow
        Write-Host "Please install git from https://git-scm.com/download/win" -ForegroundColor Yellow
        exit 1
    }
    
    Write-Host "✅ git found" -ForegroundColor Green
}

# Clone repository
function Get-Repository {
    $repoUrl = "https://github.com/black12-ag/cursor-bypass-tool.git"
    $installDir = "$env:USERPROFILE\cursor-bypass-tool"
    
    Write-Host "ℹ️  Cloning repository..." -ForegroundColor Cyan
    
    if (Test-Path $installDir) {
        Write-Host "⚠️  Directory already exists: $installDir" -ForegroundColor Yellow
        Write-Host "ℹ️  Updating existing installation..." -ForegroundColor Cyan
        Set-Location $installDir
        git pull origin main
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to update repository" -ForegroundColor Red
            exit 1
        }
    }
    else {
        git clone $repoUrl $installDir
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Failed to clone repository" -ForegroundColor Red
            exit 1
        }
        Set-Location $installDir
    }
    
    Write-Host "✅ Repository ready" -ForegroundColor Green
    return $installDir
}

# Install dependencies
function Install-Dependencies {
    param($pipCmd)
    
    Write-Host "ℹ️  Installing Python dependencies..." -ForegroundColor Cyan
    
    & $pipCmd install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
}

# Run the tool
function Start-Tool {
    param($pythonCmd)
    
    Write-Host "✅ Installation complete!" -ForegroundColor Green
    Write-Host "ℹ️  Starting Cursor Bypass Tool..." -ForegroundColor Cyan
    Write-Host ""
    
    & $pythonCmd main.py
}

# Main installation process
function Main {
    Show-Logo
    
    Write-Host "🚀 Starting installation..." -ForegroundColor Cyan
    Write-Host ""
    
    $pythonCmd = Test-Python
    $pipCmd = Test-Pip -pythonCmd $pythonCmd
    Test-Git
    Write-Host ""
    
    $installDir = Get-Repository
    Write-Host ""
    
    Install-Dependencies -pipCmd $pipCmd
    Write-Host ""
    
    Start-Tool -pythonCmd $pythonCmd
}

# Run main
Main
