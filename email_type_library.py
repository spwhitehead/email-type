
from email_validator import validate_email, EmailNotValidError

email = input("Enter your email address: ")

try:
    email = validate_email(email).email
except EmailNotValidError as e:
    print(str(e))
