from gpiozero import MCP3008
import time
import json


class wind_direction:
    def __init__(self):
        
        with open("/home/sangeetha/Documents/weather_station/weather_final/wind_direction.json", "r") as file:
            self.config = json.load(file)
                     
        

    def get_wind_direction(self,adc_channel = 0):
        self.adc = MCP3008(channel= adc_channel)
        voltage = self.adc.value * 3.3
        for direction in self.config["directions"]:
            if direction["min_voltage"] <= voltage <= direction["max_voltage"]:
                return direction["name"]
        return "Direction not found"





