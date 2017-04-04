from Tkinter import *
from bs4 import BeautifulSoup as bs
import tkFont
import urllib

root = Tk()
root.title("Stock Risk Analyzer")
search_url = "https://www.google.com/finance?q="
default = "$ 0.00"
price_now = StringVar()
price_close = StringVar()
high = StringVar()
low = StringVar()


def stock_id(event):
    stock_data = stock_input_field.get()
    stock_input_field.delete(0, END)
    stock_search_url = search_url + stock_data
    soup = bs(urllib.urlopen(stock_search_url), "lxml")
    span_current = soup.body.find("span", "pr")
    historical_url = soup.body.find(href=re.compile("historical"))
    historical_url = "https://www.google.com" + historical_url['href']
    print(historical_url)
    price_now.set("$ " + span_current.text.strip())
    price_close.set(default)
    #price_close.set("$ "+ span_close.text.strip())

price_now.set(default)
high.set(default)
low.set(default)

app_title = Label(root, text="Welcome to Stock Risk Analyzer", font=("Times", "18"))

input_stock_text = Label(root, text="Input Stock Name", font=("Times", "12"))
stock_input_field = Entry(root)
stock_input_field.bind('<Return>', stock_id)

stock_enter_button = Button(root, text=" Enter ")
stock_enter_button.bind('<Button-1>', stock_id)

current_price_label = Label(root, text="Current Price", font=("Times", "14"))
current_price = Label(root, textvariable=price_now, font=("Times", "14"))

close_price_text = Label(root, text="Close Price", font=("Times", "14"))
close_result = Label(root, textvariable=price_close, font=("Times", "14"))

stock_low = Label(root, text="Low", font=("Times", "14"))
stock_high = Label(root, text="High", font=("Times", "14"))
high_text = Label(root, textvariable=high, font=("Times", "14"))
low_text = Label(root, textvariable=low, font=("Times", "14"))

Graph_text = Label(root, text="Historical Close Price Graph", font=("Times", "18"))

#Grid Layout and Padding
app_title.grid(row=0, columnspan=8, padx=20, pady=20)

input_stock_text.grid(row=1, column=1, sticky=E)

stock_input_field.grid(row=1, column=2, padx=10)
stock_enter_button.grid(row=1, column=3)

current_price_label.grid(row=2, column=0, padx=20, pady=2)
current_price.grid(row=3, column=0, padx=20)

close_price_text.grid(row=2, column=6, padx=20)
close_result.grid(row=3, column=6, padx=20)

stock_low.grid(row=2, column=1)
stock_high.grid(row=2, column=2)

high_text.grid(row=3, column=2)
low_text.grid(row=3, column=1)

Graph_text.grid(row=4, columnspan=8, padx=20, pady=20)

root.mainloop()
