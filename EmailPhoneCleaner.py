import re

def extract_email_or_phone(text):
    # Clean up the input by stripping unwanted characters (like trailing colons and spaces)
    text = text.strip().strip(':')

    # Regex pattern for email extraction, with or without angle brackets
    email_pattern = r'<?([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)>?'
    
    # Regex pattern for phone number extraction (matches a 10-digit phone number)
    phone_pattern = r'(\d{3})(\d{3})(\d{4})'
    
    # Try to find an email first, with or without angle brackets
    email_match = re.search(email_pattern, text)
    
    # Check if the email contains only digits before the @ sign (potential phone number)
    if email_match:
        local_part = email_match.group(1).split('@')[0]
        if local_part.isdigit() and len(local_part) == 10:
            # If local part is all digits and 10 characters, treat it as a phone number
            phone_match = re.search(phone_pattern, local_part)
            if phone_match:
                # Format the phone number as 603*475*7681
                formatted_phone = f"{phone_match.group(1)}*{phone_match.group(2)}*{phone_match.group(3)}"
                return f"Phone number found: {formatted_phone}"
        else:
            # Otherwise, treat it as a regular email
            return f"Email found: {email_match.group(1)}"
    
    # If no email or numeric email, try to find a phone number in the text
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        # Format the phone number as 603*475*7681
        formatted_phone = f"{phone_match.group(1)}*{phone_match.group(2)}*{phone_match.group(3)}"
        return f"Phone number found: {formatted_phone}"
    
    return "No email or phone number found."

def main():
    while True:
        # Prompt user for input
        user_input = input("Please enter a line containing an email or phone number: ")

        # Clean and process the input
        result = extract_email_or_phone(user_input)

        # Output the result
        print(result)

        # Ask user if they want to start over or exit
        restart = input("Do you want to submit another entry? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Exiting the program. Goodbye!")
            break

# Run the main loop
main()