#!/bin/bash

# Bulletproof Installation Script for Cursor Bypass Tool
# Handles all git conflicts and edge cases

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logo
print_logo() {
    echo -e "${CYAN}"
    cat << "EOF"
  ███╗   ███╗██╗   ██╗███╗   ██╗██╗██████╗ 
  ████╗ ████║██║   ██║████╗  ██║██║██╔══██╗
  ██╔████╔██║██║   ██║██╔██╗ ██║██║██████╔╝
  ██║╚██╔╝██║██║   ██║██║╚██╗██║██║██╔══██╗
  ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║██║  ██║
  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
EOF
    echo -e "${NC}"
    echo -e "${YELLOW}Cursor Bypass Tool v1.0.4${NC}"
    echo -e "${GREEN}Bulletproof Installation Script by Munir${NC}"
    echo ""
}

# Logging function
log() {
    local level=$1
    shift
    case $level in
        "INFO")  echo -e "${CYAN}ℹ️  $*${NC}" ;;
        "SUCCESS") echo -e "${GREEN}✅ $*${NC}" ;;
        "WARN")  echo -e "${YELLOW}⚠️  $*${NC}" ;;
        "ERROR") echo -e "${RED}❌ $*${NC}" ;;
        *)       echo -e "$*" ;;
    esac
}

# Check if Python 3 is installed
check_python() {
    log "INFO" "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        log "SUCCESS" "Python 3 found: ${PYTHON_VERSION}"
        return 0
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        if [[ $PYTHON_VERSION == 3.* ]]; then
            log "SUCCESS" "Python 3 found: ${PYTHON_VERSION}"
            return 0
        fi
    fi
    
    log "ERROR" "Python 3 is required but not found"
    log "INFO" "Please install Python 3.8 or higher:"
    if [[ "$(uname)" == "Darwin" ]]; then
        echo -e "  ${CYAN}brew install python3${NC}"
    else
        echo -e "  ${CYAN}sudo apt install python3 python3-pip${NC}  # Ubuntu/Debian"
        echo -e "  ${CYAN}sudo dnf install python3 python3-pip${NC}  # Fedora"
        echo -e "  ${CYAN}sudo pacman -S python python-pip${NC}     # Arch"
    fi
    return 1
}

# Check if pip is installed
check_pip() {
    log "INFO" "Checking pip installation..."
    
    if command -v pip3 &> /dev/null; then
        PIP_CMD="pip3"
        log "SUCCESS" "pip3 found"
        return 0
    elif command -v pip &> /dev/null; then
        PIP_CMD="pip"
        log "SUCCESS" "pip found"
        return 0
    else
        log "WARN" "pip not found, trying to install..."
        if $PYTHON_CMD -m ensurepip --default-pip 2>/dev/null; then
            PIP_CMD="$PYTHON_CMD -m pip"
            log "SUCCESS" "pip installed"
            return 0
        else
            log "ERROR" "Failed to install pip"
            return 1
        fi
    fi
}

# Check if git is installed
check_git() {
    log "INFO" "Checking git installation..."
    
    if command -v git &> /dev/null; then
        log "SUCCESS" "git found"
        return 0
    fi
    
    log "WARN" "git not found"
    log "INFO" "Please install git:"
    if [[ "$(uname)" == "Darwin" ]]; then
        echo -e "  ${CYAN}brew install git${NC}"
    else
        echo -e "  ${CYAN}sudo apt install git${NC}     # Ubuntu/Debian"
        echo -e "  ${CYAN}sudo dnf install git${NC}     # Fedora"
        echo -e "  ${CYAN}sudo pacman -S git${NC}       # Arch"
    fi
    return 1
}

# Force clean git repository
force_clean_git() {
    local repo_dir="$1"
    log "INFO" "Force cleaning git repository..."
    
    cd "$repo_dir" || return 1
    
    # Backup any user files
    if [ -f "user_config.py" ] || [ -f "custom_settings.json" ]; then
        log "INFO" "Backing up user files..."
        mkdir -p ~/.cursor-bypass-backup 2>/dev/null
        cp user_config.py ~/.cursor-bypass-backup/ 2>/dev/null || true
        cp custom_settings.json ~/.cursor-bypass-backup/ 2>/dev/null || true
    fi
    
    # Nuclear option - completely reset
    git fetch origin 2>/dev/null || return 1
    git reset --hard HEAD 2>/dev/null || true
    git clean -fdx 2>/dev/null || true
    git checkout main 2>/dev/null || git checkout -b main 2>/dev/null || true
    git reset --hard origin/main 2>/dev/null || return 1
    
    log "SUCCESS" "Repository force cleaned"
    return 0
}

# Setup repository with full error handling
setup_repository() {
    local repo_url="https://github.com/black12-ag/cursor-bypass-tool.git"
    local install_dir="$HOME/cursor-bypass-tool"
    
    log "INFO" "Setting up repository..."
    
    # Create parent directory if needed
    mkdir -p "$(dirname "$install_dir")" 2>/dev/null || true
    
    if [ -d "$install_dir" ]; then
        log "WARN" "Directory already exists: ${install_dir}"
        
        if [ -d "$install_dir/.git" ]; then
            log "INFO" "Found existing git repository"
            cd "$install_dir" || return 1
            
            # Try simple pull first
            if git pull origin main 2>/dev/null; then
                log "SUCCESS" "Repository updated successfully"
                return 0
            fi
            
            # Try fetch and reset
            log "INFO" "Simple pull failed, trying force clean..."
            if force_clean_git "$install_dir"; then
                log "SUCCESS" "Repository force updated"
                return 0
            fi
            
            # Last resort - remove and re-clone
            log "WARN" "Force clean failed, removing and re-cloning..."
            cd "$HOME" || return 1
            rm -rf "$install_dir"
        else
            log "INFO" "Directory exists but not a git repo, removing..."
            rm -rf "$install_dir"
        fi
    fi
    
    # Fresh clone
    log "INFO" "Cloning fresh repository..."
    if git clone "$repo_url" "$install_dir"; then
        cd "$install_dir" || return 1
        log "SUCCESS" "Repository cloned successfully"
        return 0
    else
        log "ERROR" "Failed to clone repository"
        return 1
    fi
}

# Install dependencies with multiple retry strategies
install_dependencies() {
    log "INFO" "Installing Python dependencies..."
    
    # Upgrade pip first
    log "INFO" "Upgrading pip..."
    $PIP_CMD install --upgrade pip 2>/dev/null || true
    
    # Try different installation strategies
    local strategies=(
        "$PIP_CMD install -r requirements.txt"
        "$PIP_CMD install --user -r requirements.txt"
        "$PIP_CMD install --no-cache-dir -r requirements.txt"
        "$PIP_CMD install --break-system-packages -r requirements.txt"
        "$PIP_CMD install --break-system-packages --user -r requirements.txt"
        "$PIP_CMD install --force-reinstall -r requirements.txt"
    )
    
    for strategy in "${strategies[@]}"; do
        log "INFO" "Trying: $strategy"
        if eval "$strategy" 2>/dev/null; then
            log "SUCCESS" "Dependencies installed successfully"
            return 0
        fi
        log "WARN" "Strategy failed, trying next..."
    done
    
    log "ERROR" "All installation strategies failed"
    return 1
}

# Test installation integrity
test_installation() {
    log "INFO" "Testing installation integrity..."
    
    # Test Python imports
    if $PYTHON_CMD -c "import sys; print('Python OK')" 2>/dev/null; then
        log "SUCCESS" "Python test passed"
    else
        log "WARN" "Python test failed"
        return 1
    fi
    
    # Test main module
    if $PYTHON_CMD -c "import main" 2>/dev/null; then
        log "SUCCESS" "Main module test passed"
    else
        log "WARN" "Main module test failed (may work anyway)"
    fi
    
    # Test critical dependencies
    local critical_deps=("colorama" "requests")
    for dep in "${critical_deps[@]}"; do
        if $PYTHON_CMD -c "import $dep" 2>/dev/null; then
            log "SUCCESS" "$dep dependency OK"
        else
            log "WARN" "$dep dependency missing"
        fi
    done
    
    return 0
}

# Create desktop shortcut (optional)
create_shortcut() {
    local install_dir="$HOME/cursor-bypass-tool"
    
    if [[ "$(uname)" == "Darwin" ]]; then
        # macOS - create alias
        log "INFO" "Creating macOS alias..."
        osascript -e "tell application \"Finder\" to make alias file to POSIX file \"$install_dir\" at desktop" 2>/dev/null || true
    elif command -v desktop-file-install &> /dev/null; then
        # Linux - create desktop entry
        log "INFO" "Creating Linux desktop entry..."
        cat > ~/.local/share/applications/cursor-bypass.desktop << EOF
[Desktop Entry]
Name=Cursor Bypass Tool
Comment=Cursor AI Bypass Tool by Munir
Exec=$PYTHON_CMD $install_dir/main.py
Path=$install_dir
Icon=terminal
Terminal=true
Type=Application
Categories=Development;
EOF
    fi
}

# Main installation process
main() {
    # Handle interruptions gracefully
    trap 'echo -e "\n${YELLOW}ℹ️  Installation interrupted by user${NC}"; exit 130' INT TERM
    
    print_logo
    
    log "INFO" "Starting bulletproof installation process..."
    echo ""
    
    # Check all prerequisites
    log "INFO" "Checking prerequisites..."
    check_python || exit 1
    check_pip || exit 1
    check_git || exit 1
    echo ""
    
    # Setup repository
    log "INFO" "Setting up repository..."
    setup_repository || {
        log "ERROR" "Failed to setup repository"
        exit 1
    }
    echo ""
    
    # Install dependencies
    log "INFO" "Installing dependencies..."
    install_dependencies || {
        log "ERROR" "Failed to install dependencies"
        exit 1
    }
    echo ""
    
    # Test installation
    log "INFO" "Testing installation..."
    test_installation || log "WARN" "Some tests failed but installation may still work"
    echo ""
    
    # Success!
    echo -e "${GREEN}══════════════════════════════════════════════════════════${NC}"
    log "SUCCESS" "INSTALLATION COMPLETED SUCCESSFULLY!"
    echo -e "${GREEN}══════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Auto-run the tool immediately
    echo -e "${CYAN}🚀 Auto-starting Cursor Bypass Tool...${NC}"
    echo -e "${CYAN}══════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Change to install directory and run
    cd "$HOME/cursor-bypass-tool" || exit 1
    exec $PYTHON_CMD main.py
}

# Run with error handling
if ! main "$@"; then
    echo ""
    log "ERROR" "Installation failed with exit code $?"
    echo -e "${YELLOW}Please try running the script again or install manually:${NC}"
    echo -e "${CYAN}git clone https://github.com/black12-ag/cursor-bypass-tool.git${NC}"
    echo -e "${CYAN}cd cursor-bypass-tool${NC}"
    echo -e "${CYAN}pip3 install -r requirements.txt${NC}"
    echo -e "${CYAN}python3 main.py${NC}"
    exit 1
fi