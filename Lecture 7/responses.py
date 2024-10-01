import validators

email=input("What's your email address?").strip()

if validators.email(email) ==True :
    print("Valid")
else:
    print("Invalid")
