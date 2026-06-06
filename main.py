from services.ocean import get_companies
from services.prospeo import get_contacts
from services.eazyreach import get_email
from services.brevo import send_email

domain = input("Enter company domain: ")

companies = get_companies(domain)

all_emails = []

for company in companies:

    contacts = get_contacts(company)

    for contact in contacts:

        email = get_email(contact["linkedin"])

        all_emails.append(email)

        print(
            f"{contact['name']} | "
            f"{contact['role']} | "
            f"{email}"
        )

print("\nSummary")
print("Emails Found:", len(all_emails))

confirm = input("Send emails? (y/n): ")

if confirm.lower() == "y":

    for email in all_emails:
        send_email(email)

else:
    print("Cancelled")