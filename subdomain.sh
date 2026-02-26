#!/bin/bash

check_amass() {
    if ! command -v amass &> /dev/null; then
        echo "Amass is not installed. Installing..."
        sudo apt update
        sudo snap install amass
    else
        echo "Already installed."
    fi
}

check_subfinder() {
    if ! command -v subfinder &> /dev/null; then
        echo "Subfinder is not installed. Installing..."
        sudo apt install golang -y
        wget https://go.dev/dl/go1.24.0.linux-amd64.tar.gz
        sudo tar -C /usr/local -xzf go1.24.0.linux-amd64.tar.gz
        source ~/.bashrc
        go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
    else
        echo "Already installed."
    fi
}

perform_amass_enum() {
    check_amass
    if [ ! -d "$domain/amass" ]; then          
        mkdir -p "$domain/amass"
        echo "Created folder: amass"
    else
        echo "Folder already exists"
    fi
    datetime=$(date +%Y-%m-%d_%H-%M-%S)
    output_file="$domain/amass/amass_${domain}_${datetime}.txt"
    echo "Saving results to: $output_file"
    amass enum -active -d "$domain" -r 8.8.8.8 2>/dev/tty | tee "$output_file"
    echo "Amass enumeration completed. Results saved to: $output_file"
}

perform_subfinder_enum() {
    check_subfinder
    if [ ! -d "$domain/subfinder" ]; then          
        mkdir -p "$domain/subfinder"
        echo "Created folder: subfinder"
    else
        echo "Folder already exists"
    fi
    datetime=$(date +%Y-%m-%d_%H-%M-%S)
    output_file="$domain/subfinder/subfinder_${domain}_${datetime}.txt"
    echo "Saving results to: $output_file"
    subfinder -d "$domain" -all -recursive  2>/dev/tty | tee "$output_file"
    echo "Subfinder enumeration completed. Results saved to: $output_file"
}

choose_tool() {
    echo "Choose the tool you want to use:"
    echo "1. Amass"
    echo "2. Subfinder"
    read -p "Enter your choice: " choice
    case $choice in
        1) perform_amass_enum ;;
        2) perform_subfinder_enum ;;
    esac
}

echo "Subdomain Enumeration"
echo "Perform subdomain enumeration using amass tool: "
read -p "Enter the target domain name: " domain

if [ ! -d "$domain" ]; then                    # ← space before ]
    mkdir -p "$domain"
    echo "Created folder: $domain"
else
    echo "Folder already exists"
fi

choose_tool