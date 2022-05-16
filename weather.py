from tkinter import *
from PIL import ImageTk, Image
from matplotlib.ft2font import BOLD
import requests

class Weather:
    def __init__(self):

        self.initUI()
    
    def initUI(self):
        self.window = Tk()
        self.window.title("DzWeather")
        self.window.geometry("466x665")
        self.window.resizable(0,0)
        self.window.configure(bg = "white")

        #Background
        self.bg_label = Label(self.window, bg = "#01aaed")
        self.bg_label.place(x = 0, y = 0, width = 466, height = 219)

        #Image
        self.img = Image.open("weather.png")
        self.resized_img = self.img.resize((111, 81), Image.ANTIALIAS)

        self.pic = ImageTk.PhotoImage(self.resized_img)
        self.label = Label(self.window, image = self.pic, bg = "#01aaed")
        self.label.place(x = 180, y = 120)


        #Input
        self.search_city = Entry(self.window, bg = "white", fg = "black", font = ("Arial", 20))
        self.search_city.bind("<Return>", self.weather)
        self.search_city.place(x = 80, y = 50, width = 317, height = 45)


        #Label
        self.city_name = Label(self.window, bg = "white", font = ("Arial", 30, "bold"))
        self.city_name.place(x = 20, y =260, width = 439, height = 52)

        self.temperature = Label(self.window, bg = "white", font = ("Arial", 25))
        self.temperature.place(x = 180, y = 350, width = 114, height = 58)

        self.desc = Label(self.window, bg = "white", font = ("Arial", 25))
        self.desc.place(x = 90, y = 440, width = 300, height = 30)

        self.wind = Label(self.window, bg = "white", font = ("Arial", 20))
        self.wind.place(x = 55, y = 580, width= 130, height = 35)

        self.pressure = Label(self.window, bg = "white", font = ("Arial", 20))
        self.pressure.place(x = 300, y = 580, width= 130, height = 35)

        self.window.mainloop()
    
    def weather(self, event):
        city = self.search_city.get()
        if city != "":
            self.city_name.config(text = city)

            try:     
                API_KEY = "27e6dcba9273868c29160d303e857e82"
                request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"
                
                respond = requests.get(request_url).json()
                
                temperature = round(respond["main"]["temp"] - 273.15, 1)
                description = respond["weather"][0]["main"]
                wind = respond["wind"]["speed"]
                pressure = respond["main"]["pressure"]

                self.temperature.config(text = f"{temperature}°C")
                self.desc.config(text = description)
                self.wind.config(text = f"{wind}mph")
                self.pressure.config(text = f"{pressure}Pa")

                #Just some effect to look nicer :>
                self.wind_label = Label(self.window, bg = "white", font = ("Arial", 25, "bold"), text = "Wind")
                self.wind_label.place(x = 75, y = 520, width= 80, height = 35)
                self.pressure_label = Label(self.window, bg = "white", font = ("Arial", 25, "bold"), text = "Pressure")
                self.pressure_label.place(x = 290, y =520, width= 150, height = 25 )
                
            except:
                pass
            


        

if __name__ == "__main__":
    Weather()