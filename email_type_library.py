
from email_validator import validate_email, EmailNotValidError

email = input("Enter your email address: ")

try:
    emailinfo = validate_email(email, check_deliverability=True)

    email = emailinfo.normalized

    print("Email is valid")

except EmailNotValidError as e:
    print(str(e))
