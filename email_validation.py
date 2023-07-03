import re
#from validate_email import validate_email
from validate_email_address import validate_email

filename = 'list_emails.txt'  # File with emails to validate

print("\n Searching for emails... \n")


def extract_emails(filename):
    all_emails = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', line)
                all_emails.extend(email)
    return all_emails

all_emails = extract_emails(filename)

valid_emails = []
count = 0

print("Validating emails... \n")

for email in all_emails:
    count += 1
    verification = validate_email(email, check_mx=True, verify=True, smtp_timeout=2)
    if verification:
        print(f"The {count}º email ({email}) is valid!.")
        valid_emails.append(email)

print("\n Valid Emails Found: \n")
for email in valid_emails:
    print(email)

