#!/bin/bash

# Texts
echo "Installing packages..."

# Function to install packages based on distribution
install_packages() {
    distro=$(awk -F= '/^ID=/{print $2}' /etc/os-release | tr -d '"')

    case $distro in
        arch)
            echo "Detected you are Arch Linux, using pacman to install packages..."
            sudo pacman -Sy --noconfirm ranger python python-pip git mpg123 libopenmpt sidplayfp wildmidi calcurse
            ;;
        ubuntu|debian)
            echo "Detected you are Ubuntu or Debian, Updating your system and install packages..."
            sudo apt update
            sudo apt install -y ranger python3 python3-pip git mpg123 libopenmpt-dev sidplayfp wildmidi calcurse
            ;;
        fedora)
            echo "Detected you are Fedora, using dnf to install packages..."
            sudo dnf install -y ranger python3 python3-pip git mpg123 libopenmpt-devel sidplayfp wildmidi calcurse
            ;;
        opensuse-leap|opensuse-tumbleweed)
            echo "Detected you are Opensuse, using zypper to install packages..."
，            sudo zypper install -y ranger python3 python3-pip git mpg123 libopenmpt-devel sidplayfp wildmidi calcurse
            ;;
        *)
            echo "Unsupported distribution(Are you using Windows?): $distro"
            exit 1
            ;;
    esac
}

# Function to install pip packages
install_pip_packages() {
    sudo pip3 install psutil colorama datetime pretty-errors
}

# Main execution starts here
install_packages
install_pip_packages

echo "Installation complete ~\(≧▽≦)/~"
echo "Type 'python3 pyosimproved.py' to start system..."
