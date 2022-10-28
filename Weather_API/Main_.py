from cProfile import label
from cgitb import text
from tkinter import *
from main import weather
from ip_details import get_ip_details


def GUI():
    
    root = Tk()

    root.geometry("300x300")
    root.title(f"{get_ip_details.city()} Weather")

    def display_city_name(city):
        city_label = Label(root, text=f'{get_ip_details.city()}')
        city_label.config(font=("Consolas", 28))
        city_label.pack(side="top")

    def display_status():
        temp = Label(root, text=f"{weather.temp_kelvin_to_celcius()}")
        clouds = Label(root, text=f"Clouds {weather.clouds()}")
        humidity = Label(root, text=f"humidity {weather.humidity()}")

        temp.config(font=("Consolas", 22))
        clouds.config(font=("Consolas", 16))
        humidity.config(font=("Consolas", 16))

        temp.pack(side="top")
        clouds.pack(side="top")
        humidity.pack(side="top")



    display_city_name(get_ip_details.city())
    display_status()
    mainloop()




if __name__ == '__main__':
  GUI()