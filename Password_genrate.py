import random
import string

def create_password(len):
    # Define the character sets to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation
    
    # Combine all character sets
    all_char = lowercase + uppercase + digits + special_char
    
    # create the password
    password = ''.join(random.choice(all_char) 
                       for _ in range(len))
    return password

def main():
    print("Password Generator")
    
    # Prompt the user to specify the desired len of the password
    while True:
        try:
            len = int(input("Enter length of the password: "))
            if len <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Create the password
    password = create_password(len)
    
    # Display the generated password
    print("Created Password:", password)

if __name__ == "__main__":
    main()
