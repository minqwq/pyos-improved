#!/bin/bash

# Function to install packages based on distribution
install_packages() {
    distro=$(awk -F= '/^ID=/{print $2}' /etc/os-release | tr -d '"')

    case $distro in
        arch)
            sudo pacman -Sy --noconfirm ranger python python-pip git mpg123 libopenmpt sidplayfp wildmidi
            ;;
        ubuntu|debian)
            sudo apt update
            sudo apt install -y ranger python3 python3-pip git mpg123 libopenmpt-dev sidplayfp wildmidi
            ;;
        fedora)
            sudo dnf install -y ranger python3 python3-pip git mpg123 libopenmpt-devel sidplayfp wildmidi
            ;;
        opensuse-leap|opensuse-tumbleweed)
            sudo zypper install -y ranger python3 python3-pip git mpg123 libopenmpt-devel sidplayfp wildmidi
            ;;
        *)
            echo "Unsupported distribution: $distro"
            exit 1
            ;;
    esac
}

# Function to install pip packages
install_pip_packages() {
    sudo pip3 install psutil Pillow matplotlib colorama datetime
}

# Main execution starts here
install_packages
install_pip_packages

echo "Installation complete ~\(≧▽≦)/~"
