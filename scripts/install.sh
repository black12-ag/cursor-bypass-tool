#!/bin/bash

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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
}

# Get download folder path
get_downloads_dir() {
    if [[ "$(uname)" == "Darwin" ]]; then
        echo "$HOME/Downloads"
    else
        if [ -f "$HOME/.config/user-dirs.dirs" ]; then
            . "$HOME/.config/user-dirs.dirs"
            echo "${XDG_DOWNLOAD_DIR:-$HOME/Downloads}"
        else
            echo "$HOME/Downloads"
        fi
    fi
}

# Get latest version
get_latest_version() {
    echo -e "${CYAN}ℹ️ Checking latest version...${NC}"
    latest_release=$(curl -s https://api.github.com/repos/black12-ag/cursor-bypass-tool/releases/latest) || {
        echo -e "${RED}❌ Cannot get latest version information${NC}"
        exit 1
    }
    
    VERSION=$(echo "$latest_release" | grep -o '"tag_name": ".*"' | cut -d'"' -f4 | tr -d 'v')
    if [ -z "$VERSION" ]; then
        echo -e "${RED}❌ Failed to parse version from GitHub API response:\n${latest_release}"
        exit 1
    fi

    echo -e "${GREEN}✅ Found latest version: ${VERSION}${NC}"
}

# Detect system type and architecture
detect_os() {
    if [[ "$(uname)" == "Darwin" ]]; then
        # Detect macOS architecture
        ARCH=$(uname -m)
        if [[ "$ARCH" == "arm64" ]]; then
            OS="mac_arm64"
            echo -e "${CYAN}ℹ️ Detected macOS ARM64 architecture${NC}"
        else
            OS="mac_intel"
            echo -e "${CYAN}ℹ️ Detected macOS Intel architecture${NC}"
        fi
    elif [[ "$(uname)" == "Linux" ]]; then
        # Detect Linux architecture
        ARCH=$(uname -m)
        if [[ "$ARCH" == "aarch64" || "$ARCH" == "arm64" ]]; then
            OS="linux_arm64"
            echo -e "${CYAN}ℹ️ Detected Linux ARM64 architecture${NC}"
        else
            OS="linux_x64"
            echo -e "${CYAN}ℹ️ Detected Linux x64 architecture${NC}"
        fi
    else
        # Assume Windows
        OS="windows"
        echo -e "${CYAN}ℹ️ Detected Windows system${NC}"
    fi
}

# Install and download
install_cursor_free_vip() {
    local downloads_dir=$(get_downloads_dir)
    local binary_name="CursorFreeVIP_${VERSION}_${OS}"
    local binary_path="${downloads_dir}/${binary_name}"
    local download_url="https://github.com/black12-ag/cursor-bypass-tool/releases/download/v${VERSION}/${binary_name}"
    
    # For macOS and Linux, try generic version first (more likely to exist)
    local generic_os=""
    local try_generic_first=false
    
    if [[ "$OS" == "mac_arm64" || "$OS" == "mac_intel" ]]; then
        generic_os="mac"
        try_generic_first=true
    elif [[ "$OS" == "linux_x64" || "$OS" == "linux_arm64" ]]; then
        generic_os="linux"
        try_generic_first=true
    fi
    
    # If we should try generic first, check for existing files with both names
    if [ "$try_generic_first" = true ]; then
        local generic_binary_name="CursorFreeVIP_${VERSION}_${generic_os}"
        local generic_binary_path="${downloads_dir}/${generic_binary_name}"
        
        # Check if generic version already exists
        if [ -f "${generic_binary_path}" ]; then
            echo -e "${GREEN}✅ Found existing installation file (generic)${NC}"
            echo -e "${CYAN}ℹ️ Location: ${generic_binary_path}${NC}"
            run_binary "${generic_binary_path}"
            return
        fi
        
        # Check if architecture-specific version exists
        if [ -f "${binary_path}" ]; then
            echo -e "${GREEN}✅ Found existing installation file (arch-specific)${NC}"
            echo -e "${CYAN}ℹ️ Location: ${binary_path}${NC}"
            run_binary "${binary_path}"
            return
        fi
    else
        # Check if file already exists
        if [ -f "${binary_path}" ]; then
            echo -e "${GREEN}✅ Found existing installation file${NC}"
            echo -e "${CYAN}ℹ️ Location: ${binary_path}${NC}"
            run_binary "${binary_path}"
            return
        fi
    fi
    
    echo -e "${CYAN}ℹ️ No existing installation file found, starting download...${NC}"
    echo -e "${CYAN}ℹ️ Downloading to ${downloads_dir}...${NC}"
    
    # For macOS and Linux, try generic version first
    if [ "$try_generic_first" = true ]; then
        local generic_binary_name="CursorFreeVIP_${VERSION}_${generic_os}"
        local generic_binary_path="${downloads_dir}/${generic_binary_name}"
        local generic_download_url="https://github.com/black12-ag/cursor-bypass-tool/releases/download/v${VERSION}/${generic_binary_name}"
        
        echo -e "${CYAN}ℹ️ Trying generic download first: ${generic_download_url}${NC}"
        
        if curl --output /dev/null --silent --head --fail "$generic_download_url"; then
            echo -e "${GREEN}✅ Generic file exists, downloading...${NC}"
            download_and_run "$generic_download_url" "$generic_binary_path"
            return
        else
            echo -e "${YELLOW}⚠️ Generic version not found, trying architecture-specific...${NC}"
        fi
    fi
    
    # Try architecture-specific version
    echo -e "${CYAN}ℹ️ Download link: ${download_url}${NC}"
    
    if curl --output /dev/null --silent --head --fail "$download_url"; then
        echo -e "${GREEN}✅ Architecture-specific file exists, downloading...${NC}"
        download_and_run "$download_url" "$binary_path"
    else
        echo -e "${RED}❌ No suitable download found for your system${NC}"
        echo -e "${YELLOW}⚠️ Tried:${NC}"
        if [ "$try_generic_first" = true ]; then
            echo -e "${YELLOW}  - ${generic_download_url}${NC}"
        fi
        echo -e "${YELLOW}  - ${download_url}${NC}"
        exit 1
    fi
}

# Helper function to run binary
run_binary() {
    local binary_path="$1"
    
    # Check if running as root
    if [ "$EUID" -ne 0 ]; then
        echo -e "${YELLOW}⚠️ Requesting administrator privileges...${NC}"
        if command -v sudo >/dev/null 2>&1; then
            echo -e "${CYAN}ℹ️ Starting program with sudo...${NC}"
            sudo chmod +x "${binary_path}"
            sudo "${binary_path}"
        else
            echo -e "${YELLOW}⚠️ sudo not found, trying to run normally...${NC}"
            chmod +x "${binary_path}"
            "${binary_path}"
        fi
    else
        # Already running as root
        echo -e "${CYAN}ℹ️ Already running as root, starting program...${NC}"
        chmod +x "${binary_path}"
        "${binary_path}"
    fi
}

# Helper function to download and run
download_and_run() {
    local download_url="$1"
    local binary_path="$2"
    
    # Download file
    if ! curl -L -o "${binary_path}" "$download_url"; then
        echo -e "${RED}❌ Download failed${NC}"
        exit 1
    fi
    
    # Check downloaded file size
    local file_size=$(stat -f%z "${binary_path}" 2>/dev/null || stat -c%s "${binary_path}" 2>/dev/null)
    echo -e "${CYAN}ℹ️ Downloaded file size: ${file_size} bytes${NC}"
    
    # If file is too small, it might be an error message
    if [ "$file_size" -lt 1000 ]; then
        echo -e "${YELLOW}⚠️ Warning: Downloaded file is too small, possibly not a valid executable file${NC}"
        echo -e "${YELLOW}⚠️ File content:${NC}"
        cat "${binary_path}"
        echo ""
        echo -e "${RED}❌ Download failed, please check version and operating system${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Download completed!${NC}"
    echo -e "${CYAN}ℹ️ Program downloaded to: ${binary_path}${NC}"
    
    # Use the run_binary helper function
    run_binary "${binary_path}"
}

# Main program
main() {
    print_logo
    get_latest_version
    detect_os
    install_cursor_free_vip
}

# Run main program
main 
