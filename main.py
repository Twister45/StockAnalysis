from tkinter import *
from bs4 import BeautifulSoup as bs
import urllib.request

class analysis:

    def __init__(self, master):
        self.master = master
        master.title("Stock Risk Analyzer")
        master.config(bg='White')
        self.default = "$ 0.00"
        self.price_now = StringVar()
        self.price_now.set(self.default)
        self.frameInit()
        self.mainLayout()

    def mainLayout(self):
        #--------TopFrame------------
        self.app_title = Label(self.TopFrame, text="Stock Risk Analyzer", font=("Times", "18", "bold"), bg='white')
        self.app_title.grid(row=0, column=0, pady=(20,45))
        #-------LeftFrame------------
        self.current_price_text = Label(self.LeftFrame, text="Current Price", font=("Times", "14"), bg='white')
        self.current_price = Label(self.LeftFrame, textvariable=self.price_now, font=("Times", "14"), bg='white')
        self.current_price_text.grid(row=0, column=0, padx=20)
        self.current_price.grid(row=1, column=0, pady=(0,220))
        #-------CenterFrame----------
        self.graph_text = Label(self.CenterFrame, text="Historic Trend", font=("Times", "18"), bg='white')
        self.graph_chart = Label(self.CenterFrame, width=65, height=20)
        self.graph_text.grid(row=0, column=0, pady=(0,15))
        self.graph_chart.grid(row=1, column=0)
        #-------RightFrame-----------
        self.risk_text = Label(self.RightFrame, text="Risk Analysis", font=("Times", "14"), bg='white')
        self.risk_text.grid(row=0, column=0, padx=20,  pady=(0,250))
        #-------BottomFrame----------
        self.input_stock_text = Label(self.BottomFrame, text="Stock Name", font=("Times", "12"), bg='white')
        self.stock_input_field = Entry(self.BottomFrame, font=("Times", "16"))
        self.stock_input_field.bind('<Return>', self.stock_id_search)
        self.stock_enter_button = Button(self.BottomFrame, text=" Enter ")
        self.stock_enter_button.bind('<Button-1>', self.stock_id_search)
        self.input_stock_text.grid(row=0, column=0, pady=20, padx=10)
        self.stock_input_field.grid(row=0, column=1)
        self.stock_enter_button.grid(row=0, column=2, padx=10)

    def frameInit(self):
        self.TopFrame = Frame(root, bg='white')
        self.TopFrame.grid(row=0, column=1)
        self.LeftFrame = Frame(root, bg='white')
        self.LeftFrame.grid(row=1, column=0)
        self.CenterFrame = Frame(root, bg='white')
        self.CenterFrame.grid(row=1, column=1)
        self.RightFrame = Frame(root, bg='white')
        self.RightFrame.grid(row=1, column=2)
        self.BottomFrame = Frame(root, bg='white')
        self.BottomFrame.grid(row=2, column=1)

    def stock_id_search(self, event):
        search_url = "https://www.google.com/finance?q="
        self.stock_data = self.stock_input_field.get()
        self.stock_input_field.delete(0, END)
        self.stock_search_url = search_url + self.stock_data
        self.soup = bs(urllib.request.urlopen(self.stock_search_url), "lxml")
        self.span_current = self.soup.body.find("span", "pr")
        self.price_now.set("$ " + self.span_current.text.strip())
        historical_url = self.soup.body.find(href=re.compile("historical"))
        historical_url = "https://www.google.com" + historical_url['href']
        print(historical_url)

root = Tk()
my_gui = analysis(root)
root.mainloop()
