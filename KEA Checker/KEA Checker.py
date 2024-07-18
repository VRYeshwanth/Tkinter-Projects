from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from datetime import date
import webbrowser

window = tk.Tk()
window.title('KEA Checker')
window.geometry("375x425")
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\KEA Checker\book.ico')

def format_1():
    d = date.today()
    fd = d.strftime("%d-%m")
    return fd

def format_2():
    d = date.today()
    fd = d.strftime("%d/%m/%Y")
    return fd

def open_url(event):
    webbrowser.open_new(event.widget.tag_names(tk.CURRENT)[0])

def on_enter(event):
    announcement_text.config(cursor="hand2")

def on_leave(event):
    announcement_text.config(cursor="")

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
        current_url = tr.find_elements(By.TAG_NAME, 'a')
        if format_1() in text or format_2() in text:
            if current_url:
                tpl = (text, current_url[0].get_attribute('href'))
                todays_announcements.append(tpl)
            else:
                todays_announcements.append((text, None))
    browser.quit()
    
    if len(todays_announcements) == 0:
        announcement_text.config(state=tk.NORMAL)
        announcement_text.delete('1.0', tk.END)
        announcement_text.insert(tk.END, "No new Announcements")
        announcement_text.config(state=tk.DISABLED)
    else:
        announcement_text.config(state=tk.NORMAL)
        announcement_text.delete('1.0', tk.END)
        for name, link in todays_announcements:
            announcement_text.insert(tk.END, f"{name} ")
            if link:
                announcement_text.insert(tk.END, "CLICK HERE\n", link)
                announcement_text.tag_configure(link, foreground="blue", underline=True)
                announcement_text.tag_bind(link, "<Button-1>", open_url)
                announcement_text.tag_bind(link, "<Enter>", on_enter)
                announcement_text.tag_bind(link, "<Leave>", on_leave)
            else:
                announcement_text.insert(tk.END, "No link available\n", "disabled")
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
