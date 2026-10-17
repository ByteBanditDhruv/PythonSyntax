import pyautogui
import time
import webbrowser

# Safety feature
pyautogui.FAILSAFE = True

# Open Gmail
webbrowser.open("https://mail.google.com/")
print("Opening Gmail...")
time.sleep(10)

# Recipient and message
recipients = {"dhruv.shah@onmyowntechnology.com": """
Hello!

👋 This is a special email sent by my Python program!

Today I taught my computer how to:
✅ Open Gmail
✅ Type an email
✅ Write a message
✅ Click the Send button

It feels like I have my own little robot helper! 🤖

Thank you for reading my first automated email.

Have a fantastic day! 😊

From,
Dhruv
"""}


for email, message in recipients.items():

    # Click Compose
    pyautogui.click(172, 198)
    time.sleep(2)

    # Click TO field
    pyautogui.click(1319, 467)
    time.sleep(1)

    # Type recipient
    pyautogui.write(email, interval=0.05)

    # Confirm the email address
    pyautogui.press("enter")
    time.sleep(1)

    # Click Subject field
    pyautogui.click(1334, 525)
    time.sleep(1)

    pyautogui.write("Python Email Automation Demo", interval=0.05)
    time.sleep(1)

    # Click BODY
    pyautogui.click(1272, 545)
    time.sleep(1)

    pyautogui.write(message, interval=0.02)
    time.sleep(2)

    # Click SEND button
    pyautogui.click(1301, 983)
    time.sleep(4)

    print(f"Email sent to {email}")

print("✅ All emails sent successfully!")
