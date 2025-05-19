#!/usr/bin/env python3
import re
import sys

# Function to extract email addresses
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zAZ]{2,}"
    return re.findall(pattern, text)

# Function to extract URLs
def extract_urls(text):
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
    return re.findall(pattern, text)

# Function to extract phone numbers
def extract_phone_numbers(text):
    pattern=r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)

# Function to extract time
def extract_time(text):
    pattern=r"(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9])"

    return re.findall(pattern, text)

# Function to extract credit card numbers
def extract_credit_cards(text):
    pattern=r"\b(?:\d{4}[-\s]?){3}\d{4}\b"
    return re.findall(pattern, text)

def main(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
        
        # Run all extractions and print results
        print("Emails:", extract_emails(content))
        print("URLs:", extract_urls(content))
        print("Phone Numbers:", extract_phone_numbers(content))
        print("Credit Cards:", extract_credit_cards(content))
        print("time:", extract_time(content))
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    
if __name__ == "__main__":
    # Check if a file path argument is passed via sys.argv
    if len(sys.argv) < 2:
        print("Usage: python file.py <file_path>")
    else:
        file_path = sys.argv[1]  # Get the file path from the argument
        main(file_path)
