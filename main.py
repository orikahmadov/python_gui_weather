import requests, os, json
import tkinter as tk
# from tkinter import *



def main():

    """Same font style for all elements"""
    font_style_head = ("Courier", 14, "italic")
    font_color = "blue"
    font_style = "Helvetica 13 bold"
    """ Welcome Text is just a label"""
    window  =  tk.Tk(baseName="Weather App",screenName="Weather App")
    welcome_text =  tk.Label(master =  window, text = "Welcome to the Simple Weather App")
    welcome_text.config(font =( "Arial", 12, "italic"), fg = "Blue", height = 5, justify = "center")
    welcome_text.pack()
    city_text =  tk.Label(master = window,font =( "Arial", 12, "italic"), text = "City name: ",)
    city_text.config(font = font_style_head)
    city_text.pack()
    city_entry  =  tk.Entry(master =  window, width = 30, )
    city_entry.pack()
    search_button = tk.Button(master = window, text = "Search")
    search_button.pack()
    clear_button = tk.Button(master=window, text="Clear")
    clear_button.pack()
    result_label =  tk.Label(master = window, text = "Results will be shown below")
    result_label.pack()


    def send_request():
        parameters = {"q" : city_entry.get(), "appid":"a960484a844584377f6b8516de7e9335"}
        request =  requests.get("https://api.openweathermap.org/data/2.5/weather?", params=parameters)
        weather_json =  request.json()
        if request.status_code == 200:
           return weather_json
        else:
            result_label.config(text = f"Unfortunately no result found for {parameters.get('q')}")
            result_label.config(fg = "red")

    def kelvin_to_celsius(kelvin):
        celsius =  kelvin - 273.15
        return round(celsius)

    def process_data():
        try:
            result_json = send_request()
            coords = [d for d in result_json["coord"].items()]
            weather= [d for d in result_json["weather"]]
            weather_description = weather[0]["description"].capitalize()
            result_label.config(text = "Please click clear button for new search")
            weather_temperature_result= [a for a  in result_json["main"].items()]
            #temperature res
            current_temp_celsius = kelvin_to_celsius(weather_temperature_result[0][1])
            humidity = weather_temperature_result[5][1]
            weather_icon = weather[0]["icon"]
            lon = coords[0][1]
            lat = coords[1][1]
            #Longtitude
            lon_label_text = tk.Label(master=window, text="Longitude", font=font_style)
            lon_label_text.pack()

            lon_label =  tk.Label(master=window, text =  lon, fg = "blue", font = font_style)
            lon_label.pack()
            #Latitude
            lat_label_text = tk.Label(master=window, text="Latitude", font=font_style)
            lat_label_text.pack()
            lat_label = tk.Label(master=window, text=lat, fg = "blue", font = font_style)
            lat_label.pack()
            #Weather Description
            weather_description_label_text = tk.Label(master=window, text="Description of Weather", font =  font_style)
            weather_description_label_text.pack()
            weather_description_label = tk.Label(master = window, font = font_style)
            weather_description_label.config(text =  weather_description, fg = "blue", font = font_style)
            weather_description_label.pack()
            # Temperature Label
            temperature_label_text = tk.Label(master=window, text="Temperature Celsius", font=font_style)
            temperature_label_text.pack()
            # Temperature Label Result
            temperature_label = tk.Label(master=window, text=f"{current_temp_celsius} C\N{DEGREE SIGN}", fg="blue", font=font_style)
            temperature_label.pack()
            #Humidity
            humidity_speed_label_text = tk.Label(master=window, text="Humidity", font = font_style)
            humidity_speed_label_text.pack()
            global humid_label
            humid_label = tk.Label(master=window, text=humidity, fg="blue", font=font_style)
            humid_label.pack()
            #Country Name
            country_text =  tk.Label(master = window, text = "Country", font  =  font_style)
            country_text.pack()
            country_result = tk.Label(master=window, text="", fg="blue", font=font_style)
            country_result.pack()
            with open("countries.json", "r") as f:
                data = f.read()
                object_json = json.loads(data)
                found_country =  [country["name"] for country in object_json if country["code"] == result_json["sys"]["country"]]
                country_result.config(text = found_country[0])
        except :
            pass

    def restart_program():
        # city_entry.delete(0,100)
        # python = sys.executable
        # os.execl(python, python, *sys.argv)
        humid_label.destroy()



        
    

    search_button.config(command = process_data)
    clear_button.config(command =  restart_program)
    window.title("Simple Weather App")
    window.geometry("600x600+300+30")
    window.mainloop()

if __name__ == '__main__':
    main()