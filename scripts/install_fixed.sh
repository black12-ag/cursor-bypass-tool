#!/bin/bash

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
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
    echo -e "${GREEN}Customized by Munir - Improved Install Script${NC}"
    echo ""
}

# Check if Python 3 is installed
check_python() {
    echo -e "${CYAN}ℹ️  Checking Python installation...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        echo -e "${GREEN}✅ Python 3 found: ${PYTHON_VERSION}${NC}"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        if [[ $PYTHON_VERSION == 3.* ]]; then
            echo -e "${GREEN}✅ Python 3 found: ${PYTHON_VERSION}${NC}"
        else
            echo -e "${RED}❌ Python 3 is required but not found${NC}"
            echo -e "${YELLOW}Please install Python 3.8 or higher${NC}"
            exit 1
        fi
    else
        echo -e "${RED}❌ Python is not installed${NC}"
        echo -e "${YELLOW}Please install Python 3.8 or higher:${NC}"
        if [[ "$(uname)" == "Darwin" ]]; then
            echo -e "  ${CYAN}brew install python3${NC}"
        else
            echo -e "  ${CYAN}sudo apt install python3 python3-pip${NC}  # Ubuntu/Debian"
            echo -e "  ${CYAN}sudo dnf install python3 python3-pip${NC}  # Fedora"
            echo -e "  ${CYAN}sudo pacman -S python python-pip${NC}     # Arch"
        fi
        exit 1
    fi
}

# Check if pip is installed
check_pip() {
    echo -e "${CYAN}ℹ️  Checking pip installation...${NC}"
    
    if command -v pip3 &> /dev/null; then
        PIP_CMD="pip3"
        echo -e "${GREEN}✅ pip3 found${NC}"
    elif command -v pip &> /dev/null; then
        PIP_CMD="pip"
        echo -e "${GREEN}✅ pip found${NC}"
    else
        echo -e "${YELLOW}⚠️  pip not found, trying to install...${NC}"
        $PYTHON_CMD -m ensurepip --default-pip 2>/dev/null || {
            echo -e "${RED}❌ Failed to install pip${NC}"
            exit 1
        }
        PIP_CMD="$PYTHON_CMD -m pip"
        echo -e "${GREEN}✅ pip installed${NC}"
    fi
}

# Check if git is installed
check_git() {
    echo -e "${CYAN}ℹ️  Checking git installation...${NC}"
    
    if ! command -v git &> /dev/null; then
        echo -e "${YELLOW}⚠️  git not found${NC}"
        echo -e "${YELLOW}Please install git:${NC}"
        if [[ "$(uname)" == "Darwin" ]]; then
            echo -e "  ${CYAN}brew install git${NC}"
        else
            echo -e "  ${CYAN}sudo apt install git${NC}     # Ubuntu/Debian"
            echo -e "  ${CYAN}sudo dnf install git${NC}     # Fedora"
            echo -e "  ${CYAN}sudo pacman -S git${NC}       # Arch"
        fi
        exit 1
    fi
    echo -e "${GREEN}✅ git found${NC}"
}

# Force clean repository update - handles all git conflicts
force_clean_repo() {
    local repo_dir="$1"
    echo -e "${YELLOW}ℹ️  Force cleaning repository state...${NC}"
    
    cd "$repo_dir" || return 1
    
    # Save current branch
    current_branch=$(git branch --show-current 2>/dev/null || echo "main")
    
    # Reset any local changes
    git reset --hard HEAD 2>/dev/null || true
    
    # Clean untracked files
    git clean -fd 2>/dev/null || true
    
    # Fetch latest
    git fetch origin 2>/dev/null || {
        echo -e "${RED}❌ Failed to fetch from origin${NC}"
        return 1
    }
    
    # Force reset to remote
    git reset --hard "origin/$current_branch" 2>/dev/null || git reset --hard "origin/main" 2>/dev/null || {
        echo -e "${RED}❌ Failed to reset to remote${NC}"
        return 1
    }
    
    echo -e "${GREEN}✅ Repository cleaned and updated${NC}"
    return 0
}

# Clone or update repository with conflict resolution
clone_repo() {
    REPO_URL="https://github.com/black12-ag/cursor-bypass-tool.git"
    INSTALL_DIR="$HOME/cursor-bypass-tool"
    
    echo -e "${CYAN}ℹ️  Setting up repository...${NC}"
    
    if [ -d "$INSTALL_DIR" ]; then
        echo -e "${YELLOW}⚠️  Directory already exists: ${INSTALL_DIR}${NC}"
        
        # Check if it's a git repository
        if [ -d "$INSTALL_DIR/.git" ]; then
            echo -e "${CYAN}ℹ️  Updating existing git repository...${NC}"
            
            # Try normal pull first
            cd "$INSTALL_DIR" || exit 1
            if git pull origin main 2>/dev/null; then
                echo -e "${GREEN}✅ Repository updated successfully${NC}"
            else
                echo -e "${YELLOW}⚠️  Pull failed, force cleaning repository...${NC}"
                
                # Force clean and update
                if ! force_clean_repo "$INSTALL_DIR"; then
                    echo -e "${YELLOW}ℹ️  Repository cleanup failed, removing and re-cloning...${NC}"
                    cd "$HOME" || exit 1
                    rm -rf "$INSTALL_DIR"
                    
                    git clone "$REPO_URL" "$INSTALL_DIR" || {
                        echo -e "${RED}❌ Failed to clone repository${NC}"
                        exit 1
                    }
                fi
            fi
        else
            echo -e "${YELLOW}ℹ️  Directory exists but not a git repo, removing and re-cloning...${NC}"
            rm -rf "$INSTALL_DIR"
            
            git clone "$REPO_URL" "$INSTALL_DIR" || {
                echo -e "${RED}❌ Failed to clone repository${NC}"
                exit 1
            }
        fi
    else
        echo -e "${CYAN}ℹ️  Cloning fresh repository...${NC}"
        git clone "$REPO_URL" "$INSTALL_DIR" || {
            echo -e "${RED}❌ Failed to clone repository${NC}"
            exit 1
        }
    fi
    
    cd "$INSTALL_DIR" || exit 1
    echo -e "${GREEN}✅ Repository ready at: ${INSTALL_DIR}${NC}"
}

# Install dependencies with retry
install_dependencies() {
    echo -e "${CYAN}ℹ️  Installing Python dependencies...${NC}"
    
    # Upgrade pip first
    echo -e "${CYAN}ℹ️  Upgrading pip...${NC}"
    $PIP_CMD install --upgrade pip 2>/dev/null || true
    
    # Install dependencies with retry
    local max_attempts=3
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo -e "${CYAN}ℹ️  Installation attempt $attempt/$max_attempts...${NC}"
        
        if $PIP_CMD install -r requirements.txt; then
            echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
            return 0
        else
            echo -e "${YELLOW}⚠️  Installation attempt $attempt failed${NC}"
            attempt=$((attempt + 1))
            
            if [ $attempt -le $max_attempts ]; then
                echo -e "${CYAN}ℹ️  Retrying in 2 seconds...${NC}"
                sleep 2
            fi
        fi
    done
    
    echo -e "${RED}❌ Failed to install dependencies after $max_attempts attempts${NC}"
    exit 1
}

# Test installation
test_installation() {
    echo -e "${CYAN}ℹ️  Testing installation...${NC}"
    
    # Test Python imports
    if $PYTHON_CMD -c "import main; print('✅ Main module loads successfully')" 2>/dev/null; then
        echo -e "${GREEN}✅ Installation test passed${NC}"
        return 0
    else
        echo -e "${YELLOW}⚠️  Installation test failed, but continuing...${NC}"
        return 0
    fi
}

# Run the tool
run_tool() {
    echo -e "${GREEN}✅ Installation complete!${NC}"
    echo -e "${CYAN}══════════════════════════════════════${NC}"
    echo -e "${GREEN}🎉 Ready to use! Starting tool...${NC}"
    echo -e "${CYAN}══════════════════════════════════════${NC}"
    echo ""
    
    # Run with error handling
    if ! $PYTHON_CMD main.py; then
        echo ""
        echo -e "${RED}❌ Tool execution failed${NC}"
        echo -e "${YELLOW}ℹ️  You can run it manually later with:${NC}"
        echo -e "${CYAN}   cd $HOME/cursor-bypass-tool${NC}"
        echo -e "${CYAN}   $PYTHON_CMD main.py${NC}"
    fi
}

# Main installation process
main() {
    # Trap to handle script interruption
    trap 'echo -e "\n${YELLOW}ℹ️  Installation interrupted by user${NC}"; exit 1' INT TERM
    
    print_logo
    
    echo -e "${CYAN}🚀 Starting bulletproof installation...${NC}"
    echo ""
    
    # Check prerequisites
    check_python
    check_pip
    check_git
    echo ""
    
    # Setup repository
    clone_repo
    echo ""
    
    # Install dependencies
    install_dependencies
    echo ""
    
    # Test installation
    test_installation
    echo ""
    
    # Success message
    echo -e "${GREEN}══════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ Installation completed successfully!${NC}"
    echo -e "${GREEN}══════════════════════════════════════${NC}"
    echo ""
    
    # Ask user if they want to run it now
    echo -e "${CYAN}Would you like to run the tool now? (y/n):${NC} "
    read -r response
    
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo ""
        run_tool
    else
        echo ""
        echo -e "${GREEN}✅ Installation complete!${NC}"
        echo -e "${CYAN}ℹ️  To run the tool later, use:${NC}"
        echo -e "${YELLOW}   cd $HOME/cursor-bypass-tool${NC}"
        echo -e "${YELLOW}   $PYTHON_CMD main.py${NC}"
        echo ""
        echo -e "${GREEN}Thank you for using Cursor Bypass Tool!${NC}"
    fi
}

# Run main with error handling
if ! main "$@"; then
    echo -e "${RED}❌ Installation failed${NC}"
    exit 1
fi