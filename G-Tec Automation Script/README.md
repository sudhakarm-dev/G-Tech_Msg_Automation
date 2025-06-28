# 🟢 WhatsApp Message Automation using Python + Selenium

This project automates sending WhatsApp messages to multiple contacts using data from an Excel file. It supports both **Firefox** and **Chrome** browsers and can personalize each message using the contact's name.

---

## 📌 Features

- ✅ Read names and numbers from an Excel file (`.xlsx`)
- ✅ Send personalized messages like: _"Hi John, this is an automated message."_
- ✅ Works with both Firefox and Chrome
- ✅ Logs which contacts are and aren’t on WhatsApp
- ✅ Auto-login using your existing browser profile
- ✅ Shows sending progress (e.g., Sending 3 of 10...)

---

## 🧾 Requirements

- Python 3.x
- `pandas`
- `selenium`
- `openpyxl`

Install dependencies:

```bash
pip install pandas selenium openpyxl
```

---

## 📂 Folder Structure

```
Project/
│
├── Driver/
│   └── geckodriver.exe / chromedriver.exe
│
├── Excel/
│   └── Data.xlsx  # Should contain columns: Name, Number
│
├── whatsapp_automation.py
│
├── README.md
```

---

## 📄 Excel Format

Create an Excel file with the following structure:

| Name       | Number        |
|------------|---------------|
| John Doe   | +911234567890 |
| Jane Smith | +919876543210 |

- Keep the header row (`Name`, `Number`) intact.
- Phone numbers must include the **country code** (`+91` for India, etc.).

---

## 🚀 Usage

### 🔸 Step-by-Step

1. Make sure you're logged into WhatsApp Web in the browser you choose (Chrome/Firefox)
2. Run the script and select the browser
3. Ensure Excel file is in correct format and path
4. Messages will be sent one by one with a delay

---

## ⚠️ Notes

- Do **not close the browser** while the script is running
- Ensure Excel data is clean and includes correct country codes
- XPaths may need adjustment if WhatsApp Web changes

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE)

---

## 🙋‍♂️ Author

Developed by **Sudhakar .M**  
Feel free to contribute or report issues
