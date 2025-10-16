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
    echo -e "${GREEN}Customized by Munir${NC}"
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

# Clone repository
clone_repo() {
    REPO_URL="https://github.com/black12-ag/cursor-bypass-tool.git"
    INSTALL_DIR="$HOME/cursor-bypass-tool"
    
    echo -e "${CYAN}ℹ️  Cloning repository...${NC}"
    
    if [ -d "$INSTALL_DIR" ]; then
        echo -e "${YELLOW}⚠️  Directory already exists: ${INSTALL_DIR}${NC}"
        echo -e "${CYAN}ℹ️  Updating existing installation...${NC}"
        cd "$INSTALL_DIR" || exit 1
        git pull origin main || {
            echo -e "${RED}❌ Failed to update repository${NC}"
            exit 1
        }
    else
        git clone "$REPO_URL" "$INSTALL_DIR" || {
            echo -e "${RED}❌ Failed to clone repository${NC}"
            exit 1
        }
        cd "$INSTALL_DIR" || exit 1
    fi
    
    echo -e "${GREEN}✅ Repository ready${NC}"
}

# Install dependencies
install_dependencies() {
    echo -e "${CYAN}ℹ️  Installing Python dependencies...${NC}"
    
    $PIP_CMD install -r requirements.txt || {
        echo -e "${RED}❌ Failed to install dependencies${NC}"
        exit 1
    }
    
    echo -e "${GREEN}✅ Dependencies installed${NC}"
}

# Run the tool
run_tool() {
    echo -e "${GREEN}✅ Installation complete!${NC}"
    echo -e "${CYAN}ℹ️  Starting Cursor Bypass Tool...${NC}"
    echo ""
    
    $PYTHON_CMD main.py
}

# Main installation process
main() {
    print_logo
    
    echo -e "${CYAN}🚀 Starting installation...${NC}"
    echo ""
    
    check_python
    check_pip
    check_git
    echo ""
    
    clone_repo
    echo ""
    
    install_dependencies
    echo ""
    
    run_tool
}

# Run main
main
