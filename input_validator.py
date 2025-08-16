# Input Validator and Tester


def validate_age(age):
    if age.isdigit():
        age = int(age)
        if 0 <= age <= 120:
            return True
        else:
            return False
    return False

def validate_email(email):
    return "@" in email and "." in email

if __name__ == "__main__":
    print("Input Validation Tester")
    
    age_input = input("Enter your age: ")
    email_input = input("Enter your email: ")

    if validate_age(age_input):
        print("Valid age entered.")
    else:
        print("Invalid age! Must be 0-120.")

    if validate_email(email_input):
        print("Valid email entered.")
    else:
        print("Invalid email!")
