import pandas as pd
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
FIREFOX_PROFILE = "C:\\Users\\LENOVA\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\mrbpplrs.default-esr"
GECKO_PATH = "D:\\G-Tec Automation Script\\Driver\\geckodriver.exe"
WAIT_TIME = 20
EXCEL_PATH = r"D:\\G-Tec Automation Script\\Excel\\Data.xlsx"

# Load Excel
def load_contacts(path):
    df = pd.read_excel(path, engine='openpyxl')
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    return df[["name", "number"]].dropna().to_dict(orient="records")

# Setup Firefox
def setup_driver():
    options = Options()
    options.add_argument("-profile")
    options.add_argument(FIREFOX_PROFILE)
    service = FirefoxService(executable_path=GECKO_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    return driver

# Send message to one contact
def send_message(driver, name, number):
    message = f"Hi {name}, this is an automated message. Have a great day!"
    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_msg}"
    driver.get(url)

    wait = WebDriverWait(driver, WAIT_TIME)

    try:
        error_xpath = "//div[contains(text(), 'phone number shared via url is not on WhatsApp')]"
        wait.until(EC.presence_of_element_located((By.XPATH, error_xpath)))
        print(f" {number} is not on WhatsApp.")
        return False
    except:
        try:
            box_xpath = "//div[@contenteditable='true' and @data-tab='10']"
            msg_box = wait.until(EC.presence_of_element_located((By.XPATH, box_xpath)))
            msg_box.send_keys(Keys.ENTER)
            time.sleep(15)
            print(f" Message sent to {name} ({number})")
            time.sleep(3)
            return True
        except Exception as e:
            print(f" Failed to send message to {name} ({number}). Error: {e}")
            return False

# Main Function
def main():
    print(' Your script has started...')
    contacts = load_contacts(EXCEL_PATH)
    driver = setup_driver()
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

    total = len(contacts)
    for index, contact in enumerate(contacts):
        name = contact["name"]
        number = str(contact["number"])
        print(f" Sending {index+1} of {total} - {name} ({number})")
        send_message(driver, name, number)

    print(" All messages processed.")
    driver.quit()

if __name__ == "__main__":
    main()
