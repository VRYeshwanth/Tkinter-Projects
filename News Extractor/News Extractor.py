import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import requests
from bs4 import BeautifulSoup

style = Style('darkly')
window = style.master
window.title('News Extractor')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\News Extractor\news.ico')
window.resizable(0,0)

def generate_news():
    output.delete("1.0", tk.END)
    world_news_url = "https://www.indiatoday.in/world"
    world_page = requests.get(world_news_url)
    world_soup = BeautifulSoup(world_page.text, "html.parser")
    if world_page.status_code == 200:
        wor_div = world_soup.find("div", class_ = "story__grid")
        w_article = wor_div.find_all("article")
        w_headlines = []
        for article in w_article:
            w_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "International News :-\n")
        for i, headline in enumerate(w_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    else:
        messagebox.showerror("ERROR", "We had a problem fetching International News")
    
    output.insert(tk.END, "\n")

    india_news_url = "https://www.indiatoday.in/india"
    india_page = requests.get(india_news_url)
    india_soup = BeautifulSoup(india_page.text, "html.parser")
    if india_page.status_code == 200:
        ind_div = india_soup.find("div", class_ = "story__grid")
        i_article = ind_div.find_all("article")
        i_headlines = []
        for article in i_article:
            i_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "National News :-\n")
        for i, headline in enumerate(i_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    else:
        messagebox.showerror("ERROR", "We had a problem fetching India News")
    
    output.insert(tk.END, "\n")

    business_news_url = "https://www.indiatoday.in/business"
    business_page = requests.get(business_news_url)
    business_soup = BeautifulSoup(business_page.text, "html.parser")
    if business_page.status_code == 200:
        bus_div = business_soup.find("div", class_ = "story__grid")
        b_article = bus_div.find_all("article")
        b_headlines = []
        for article in b_article:
            b_headlines.append(article.find("h2").text.strip())
        output.insert(tk.END, "Business News :-\n")
        for i, headline in enumerate(b_headlines):
            output.insert(tk.END, f"{i+1}) {headline}\n")
    else:
        messagebox.showerror("ERROR", "We had a problem fetching Business News")
    

btn = tk.Button(window, text="Today's News", command=generate_news, font="Calibri 15")
btn.pack(padx=20, pady=15, ipadx=20, ipady=5)

output = tk.Text(window, wrap="word", width=50, height=15, font="Calibri 20")
output.pack(side="left", fill="both", expand=True)

scroll_bar = tk.Scrollbar(window, command=output.yview)
scroll_bar.pack(fill="y", side="right")
output.config(yscrollcommand=scroll_bar.set)

window.mainloop()