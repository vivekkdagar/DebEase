#!/bin/bash

# Function to read input case-insensitively
read_case_insensitive() {
    prompt="$1"
    input=""
    while true; do
        read -p "$prompt" input
        input_lowercase=$(echo "$input" | tr '[:upper:]' '[:lower:]')
        if [ "$input_lowercase" == "i" ] || [ "$input_lowercase" == "a" ]; then
            break
        else
            echo "Invalid input. Please enter 'i' or 'a' (case-insensitive)."
        fi
    done
}

read_case_insensitive "Select i for Intel or a for AMD: "
selected_option="$input_lowercase"


if [ "$selected_option" == "i" ]; then
    echo "Installing CPU firmware for Intel: "
    sudo apt install intel-microcode -y
elif [ "$selected_option" == "a" ]; then
    echo "Installing CPU firmware for AMD: "
    sudo apt install amd64-microcode -y
fi