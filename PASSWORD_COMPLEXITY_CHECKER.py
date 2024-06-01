import re

def check_password_strength(password):
    # Initialize criteria counters
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate strength based on met criteria
    strength_points = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback
    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    # Determine strength level
    if strength_points == 5:
        strength_level = "Very Strong"
    elif strength_points == 4:
        strength_level = "Strong"
    elif strength_points == 3:
        strength_level = "Moderate"
    elif strength_points == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    return strength_level, feedback

def main():
    password = input("Enter your password: ")
    strength_level, feedback = check_password_strength(password)

    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
