"""
This is to check passwords and there strength based on length, complexity, and syntax
"""


#Libaries utilizing for this script are
import re
import sys


#List of commonly used weak passwords
COMMON_PASSWORD = [
    "password", "123456", "admin", "letmein", "qwerty",
    "abc123", "welcome", "1234567890"
]

def check_password_strength(password):
    """
    Checks the password strength returns feedback and score
    +1 for length of >= 8
    +2 for length of >=12
    +1 for uppercase and lowercase
    +1 for a digit
    +1 for one special character
    Deductions:
    -2 Password is in commond password list
    """


    score = 0
    feedback = []


    #Check length minimum
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("To short of password we need 8 characters")

    #Check normal length
    if len(password) >=12:
        score += 1
        feedback.append("Good length of 12+ characters")
    else:
        feedback.append("Consider using 12+ characters for better security")


    #Check the case
    if re.search(r'[A_Z]', password) and re.search(r'[a-z]', password):
        score +=1
        feedback.append("Contains both and uppercase and lowercase")
    else:
        feedback.append("Please mix uppercase and lowercase")


    #Check of there is a digit
    if re.search(r'\d', password):
        score +=1
        feedback.append("Contains a digit or number")
    else:
        feedback.append("Suggested to add a number")

    #Check special character
    if re.search(r'[!@#$%^&*(),.?:{}|<>_\-]', password):
        score +=1
        feedback.append("Contains one special character")

    else:
        feedback.append("Add at least one special character")

    #Check password list
    if password.lower() in COMMON_PASSWORD:
        sore -= 2
        feedback.append("This is a common password")

    #Determine the strength of the password
    score = max(score, 0)
    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"



    #Lets call our main
def main():
    print("PASSWORD STRENGTH CHECK")

    #Accept a password from command line
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter your password to check: ")

    score, length, feedback = check_password_strength(password)

    for line in feedback:
            print(f" {line}")


#Call main
if __name__ == "__main__":
    main()
