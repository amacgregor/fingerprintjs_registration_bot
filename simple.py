from splinter import Browser
import random
import string

with Browser() as browser:
    # Visit URL
    url = "http://localhost:3002/signup"
    browser.visit(url)

    # Fill the form
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10))
    email = "{}@thebuilder.com".format(email)
    browser.fill('email', email)

    # Submit the form
    button = browser.find_by_text('Create Account')
    button.click()

    # Validate form submission
    if browser.is_text_present('We have sent you a link to confirm your account'):
        print("[SUCCESS] Registration Successful! :)")
    else:
        print("[ERROR] Registration Failed :(")