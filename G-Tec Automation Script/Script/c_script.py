import pandas as pd
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
CHROME_PROFILE = "C:\\Users\\Your-Name\\AppData\\Local\\Google\\Chrome\\User Data"
CHROME_DRIVER_PATH = "D:\\G-Tec Automation Script\\Driver\\chromedriver.exe"
WAIT_TIME = 20
EXCEL_PATH = r"D:\\G-Tec Automation Script\\Excel\\Data.xlsx"
SMALL_DELAY = 10

#  Load Excel
def load_contacts(path):
    df = pd.read_excel(path, engine='openpyxl')
    df.columns = df.columns.str.strip().str.lower()
    return df[["name", "number"]].dropna().to_dict(orient="records")

#  Setup Chrome
def setup_driver():
    options = Options()
    options.add_argument(f"user-data-dir={CHROME_PROFILE}")
    options.add_argument("--profile-directory=Default")  # You can change if needed
    service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)

#  Send message
def send_message(driver, name, number):
    message = f"Hi {name}, this is an automated message. Have a great day!"
    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_msg}"
    driver.get(url)

    wait = WebDriverWait(driver, WAIT_TIME)

    try:
        # Check if number is not on WhatsApp
        error_xpath = "//div[contains(text(), 'phone number shared via url is not on WhatsApp')]"
        wait.until(EC.presence_of_element_located((By.XPATH, error_xpath)))
        print(f" {number} is not on WhatsApp.")
        return False
    except:
        try:
            # Send message
            box_xpath = "//div[@contenteditable='true' and @data-tab='10']"
            msg_box = wait.until(EC.presence_of_element_located((By.XPATH, box_xpath)))
            time.sleep(1)
            msg_box.send_keys(Keys.ENTER)
            print(f" Message sent to {name} ({number})")
            time.sleep(SMALL_DELAY)
            return True
        except Exception as e:
            print(f" Failed to send message to {name} ({number}). Error: {e}")
            return False

#  Main
def main():
    print(" Starting WhatsApp message automation with Chrome...")
    contacts = load_contacts(EXCEL_PATH)
    driver = setup_driver()
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

    total = len(contacts)
    for index, contact in enumerate(contacts):
        name = contact["name"]
        number = str(contact["number"])
        print(f"\n Sending {index+1} of {total}: {name} ({number})")
        send_message(driver, name, number)

    driver.quit()
    print(" All messages sent. Chrome closed.")

if __name__ == "__main__":
    main()
