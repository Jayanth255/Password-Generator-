import random
import string

generated_passwords = set()

def generate_password(length=16):
    if length < 12:
        raise ValueError("Password must be more than 12 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one of each required type
    all_chars = lowercase + uppercase + digits + special

    while True:
        # Guarantee at least 1 of each character type
        password_chars = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special),
        ]

        # Fill remaining characters randomly
        password_chars += random.choices(all_chars, k=length - 4)

        # Shuffle to avoid predictable pattern
        random.shuffle(password_chars)

        password = ''.join(password_chars)

        # Ensure password is unique (never repeated)
        if password not in generated_passwords:
            generated_passwords.add(password)
            return password


def main():
    print("=" * 40)
    print("       🔐 Password Generator")
    print("=" * 40)

    try:
        length = int(input("Enter password length (minimum 13): "))
        if length <= 12:
            print("❌ Error: Password must be MORE than 12 characters.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    count = int(input("How many passwords to generate? "))

    print("\n✅ Generated Passwords:\n")
    for i in range(1, count + 1):
        pwd = generate_password(length)
        print(f"  {i}. {pwd}")

    print("\n" + "=" * 40)
    print(f"Total unique passwords generated: {len(generated_passwords)}")


if __name__ == "__main__":
    main()
