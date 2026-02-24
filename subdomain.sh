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

perform_amass_enum() {
    check_amass
    if [ ! -d "$domain/amass" ]; then          # ← space before ]
        mkdir -p "$domain/amass"
        echo "Created folder: amass"
    else
        echo "Folder already exists"
    fi
    datetime=$(date +%Y-%m-%d_%H-%M-%S)
    output_file="$domain/amass/amass_${domain}_${datetime}.txt"
    echo "Saving results to: $output_file"
    amass enum -active -d "$domain" -r 8.8.8.8 2>/dev/tty | tee "$output_file"
}

perform_subfinder_enum() {
    echo "Perform subdomain enumeration using subfinder tool"
}

choose_tool() {
    echo "Choose the tool you want to use:"
    echo "1. Amass"
    echo "2. Subfinder"
    read -p "Enter your choice: " choice
    case $choice in
        1) perform_amass_enum ;;
        2) perform_subfinder_enum ;;
        *) echo "Invalid choice" ;;
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