import requests
import tkinter as tk

def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

    response = requests.get(url).json()

    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    temperature_label.config(text=f"Temperature: {temperature}")
    humidity_label.config(text=f"Humidity: {humidity}")
    description_label.config(text=f"Description: {description}")

root = tk.Tk()

city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

temperature_label = tk.Label(root, text="")
temperature_label.pack()

humidity_label = tk.Label(root, text="")
humidity_label.pack()

description_label = tk.Label(root, text="")
description_label.pack()

root.mainloop()
