from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from datetime import date

window = tk.Tk()
window.title('KEA Checker')
window.geometry("400x400")
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\KEA Checker\book.ico')

def format_1():
    d = date.today()
    fd = d.strftime("%d-%m")
    return fd

def format_2():
    d = date.today()
    fd = d.strftime("%d/%m/%Y")
    return fd

def get_announcements():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--default-gpu")
    chrome_options.add_argument("--window-size=1366,768")
    
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://cetonline.karnataka.gov.in/kea/")
    btn = browser.find_element(By.XPATH, '//*[@id="ddlLanguage"]/option[2]')
    btn.click()
    table = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Gridlatestannoc"]')

    todays_announcements = []
    tr_tags = table.find_elements(By.TAG_NAME, 'tr')
    for tr in tr_tags:
        text = tr.text.strip()
        if format_1() in text or format_2() in text:
            todays_announcements.append(text)
    browser.quit()

    if len(todays_announcements) == 0:
        text_display = "No new announcements"
    else:
        text_display = "\n".join(todays_announcements)
    
    announcement_text.config(state=tk.NORMAL)
    announcement_text.delete('1.0', tk.END)
    announcement_text.insert(tk.END, text_display)
    announcement_text.config(state=tk.DISABLED)

check_btn = tk.Button(window, text="Check for announcements", font="Calibri 13 bold", command=get_announcements)
check_btn.pack(padx=20, pady=10, ipadx=10, ipady=10)

announcement_text = tk.Text(window, font="Calibri 15", width=50, height=20, wrap=tk.WORD)
announcement_text.pack(padx=20, pady=(0, 20), fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(announcement_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
announcement_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=announcement_text.yview)

window.mainloop()