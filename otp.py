import phonenumbers
import random

# Function to generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Function to send the OTP (simulate sending)
def send_otp(phone_number, otp):
    print(f"OTP sent to {phone_number}: {otp}")

def main():
    while True:
        raw_phone_number = input("Enter your phone number (with country code, e.g., +1234567890): ")

        try:
            phone_number = phonenumbers.parse(raw_phone_number, None)
            if not phonenumbers.is_valid_number(phone_number):
                print("Invalid phone number. Please enter a valid number.")
                continue

            formatted_phone_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
            
            otp = generate_otp()
            send_otp(formatted_phone_number, otp)
            
            print("OTP sent successfully!")
        except phonenumbers.NumberParseException:
            print("Invalid phone number format. Please enter a valid number.")
        
        choice = input("Do you want to generate OTP for another number? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
