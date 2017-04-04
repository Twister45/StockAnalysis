from Tkinter import *
from bs4 import BeautifulSoup as bs
import tkFont
import urllib

class analysis:

    def __init__(self, master):
        self.master = master
        master.title("Stock Risk Analyzer")
        self.default = "$ 0.00"
        self.price_now = StringVar()
        self.price_now.set(self.default)
        self.information()
        self.grid()

    def information(self):
        self.app_title = Label(root, text="Welcome to Stock Risk Analyzer", font=("Times", "18"))
        self.input_stock_text = Label(root, text="Input Stock Name", font=("Times", "12"))
        self.stock_input_field = Entry(root)
        self.stock_input_field.bind('<Return>', self.stock_id_search)
        self.stock_enter_button = Button(root, text=" Enter ")
        self.stock_enter_button.bind('<Button-1>', self.stock_id_search)
        self.current_price_label = Label(root, text="Current Price", font=("Times", "14"))
        self.current_price = Label(root, textvariable=self.price_now, font=("Times", "14"))
        self.Graph_text = Label(root, text="Historical Close Price Graph", font=("Times", "18"))

    def grid(self):
        self.app_title.grid(row=0, columnspan=8, padx=20, pady=20)
        self.input_stock_text.grid(row=1, column=1, sticky=E, pady=(0, 20))
        self.stock_input_field.grid(row=1, column=2, padx=10, pady=(0, 20))
        self.stock_enter_button.grid(row=1, column=3, pady=(0, 20))
        self.current_price_label.grid(row=2, column=0, padx=20, pady=2)
        self.current_price.grid(row=3, column=0, padx=20)
        self.Graph_text.grid(row=2, column=1, columnspan=8, padx=20)

    def stock_id_search(self, event):
        search_url = "https://www.google.com/finance?q="
        self.stock_data = self.stock_input_field.get()
        self.stock_input_field.delete(0, END)
        self.stock_search_url = search_url + self.stock_data
        self.soup = bs(urllib.urlopen(self.stock_search_url), "lxml")
        self.span_current = self.soup.body.find("span", "pr")
        self.price_now.set("$ " + self.span_current.text.strip())
        historical_url = self.soup.body.find(href=re.compile("historical"))
        historical_url = "https://www.google.com" + historical_url['href']
        print(historical_url)

root = Tk()
my_gui = analysis(root)
root.mainloop()
