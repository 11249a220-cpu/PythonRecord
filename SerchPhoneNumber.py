import re
def extract_contacts(filename):
# Open and read the file
with open(filename, 'r') as file:
content = file.read()
# Regex patterns
phone_pattern = r"\+91\d{10}"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Finding all phone numbers and emails

phones = re.findall(phone_pattern, content)
emails = re.findall(email_pattern, content)

# Display results
print("Phone Numbers Found:")
for phone in phones:
print(phone)

print("\nEmail Addresses Found:")
for email in emails:
print(email)

# Example usage
extract_contacts("sample.txt") # Make sure this file exists with test data

SAMPLE CONTENT OF SAMPLE.TXT
Here are some contacts:
Call me at +919900889977 or +918888123456.
You can also email me at sample@gmail.com or contact_hr@example.co.in

SAMPLE OUTPUT:

Phone Numbers Found:
+919900889977
+918888123456

Email Addresses Found:
sample@gmail.com
contact_hr@example.co.in

