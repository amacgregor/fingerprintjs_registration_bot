from splinter import Browser
from onesecmail import OneSecMail


def create_mailbox():
    mailbox = OneSecMail.get_random_mailbox()
    return mailbox

def registration(email):
    with Browser() as browser:

        # Visit URL
        url = "http://localhost:3002/signup"
        browser.visit(url)

        # Fill the form
        browser.fill('email', email)

        # Submit the form
        button = browser.find_by_text('Create Account')
        button.click()

        # Validate form submission
        if browser.is_text_present('We have sent you a link to confirm your account'):
            print("[SUCCESS] Registration Successful! :) - {}".format(email))
        else:
            print("[ERROR] Registration Failed :(- {}".format(email))

def main():
    count = input("How many accounts do you want to generate?: ")
    count = int(count)

    for count in range(0,count):
        # Create a random mailbox
        mailbox = create_mailbox()
        # Do initial registration 
        registration(mailbox.address)

if __name__ == "__main__":
    main()
