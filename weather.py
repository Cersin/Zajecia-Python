import tkinter as tkinter
import requests

def fetchWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" \
          + city \
          + "&appid=7ded97f2e0ce975b4a0bc4630332feec&units=metric&lang=pl"
    json_data = requests.get(api).json()
    temperature = int(json_data['main']['temp'])
    description = json_data['weather'][0]['description']
    temperature_min = int(json_data['main']['temp_min'])
    temperature_max = int(json_data['main']['temp_max'])
    condition = json_data['weather'][0]['main']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    feels_like = json_data['main']['feels_like']
    wind_speed = json_data['wind']['speed']

    main_info = condition + "\n" + str(temperature) + "°C"

    description = "\n" + "Opis: " + str(description) + \
                  "\n" + "Maksymalna temperatura: " + str(temperature_max) + "°C" + \
                "\n" + "Minimalna temperatura: " + str(temperature_min) + "°C" + \
                "\n" + "Odczuwalna: " + str(feels_like) + "°C" +  \
                "\n" + "Ciśnienie: " + str(pressure) + "hPa" + \
                "\n" + "Wilgotność: " + str(humidity) + "%" + \
                "\n" + "Prędkość wiatru: " + str(wind_speed) + "km/h"
    label_first.config(text=main_info)
    label_second.config(text=description)


canvas = tkinter.Tk()
canvas.geometry("400x400")
canvas.title("Aplikacja pogody")

primary_font = ("poppins", 14, "bold")
secondary_font = ("poppins", 30, "bold")

textfield = tkinter.Entry(canvas, font=primary_font)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', fetchWeather)

label_first = tkinter.Label(canvas, font=secondary_font)
label_first.pack()
label_second = tkinter.Label(canvas, font=primary_font)
label_second.pack()

canvas.mainloop()
