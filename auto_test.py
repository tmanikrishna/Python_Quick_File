from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set your automated reply message
AUTO_REPLY_MESSAGE = "Hello! I'm currently unavailable. I will get back to you as soon as possible."

# Initialize the WebDriver (Update the path to the ChromeDriver)
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to scan QR code
print("Please scan the QR code to log in.")
time.sleep(15)  # Adjust sleep time based on your need

def get_new_messages():
    """
    Fetch chats with unread messages.
    """
    try:
        # Find all unread chats (icon with a green dot)
        unread_chats = driver.find_elements(By.XPATH, '//span[@class="aumms1qt"]')
        return unread_chats
    except Exception as e:
        print(f"Error finding unread chats: {e}")
        return []

def send_reply(chat):
    """
    Send an automated reply to the selected chat.
    """
    try:
        # Click the chat to open it
        chat.click()
        time.sleep(2)  # Wait for the chat to load

        # Find the message input box
        message_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
        
        # Type and send the message
        message_box.send_keys(AUTO_REPLY_MESSAGE + Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error sending reply: {e}")

try:
    while True:
        print("Checking for new messages...")
        unread_chats = get_new_messages()

        if unread_chats:
            print(f"Found {len(unread_chats)} unread chat(s).")
            for chat in unread_chats:
                send_reply(chat)
        else:
            print("No new messages.")

        # Wait before checking again
        time.sleep(5)

except KeyboardInterrupt:
    print("Stopping the script.")
finally:
    driver.quit()
