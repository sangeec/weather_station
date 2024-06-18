import temp_bme280
import interrupt_client
import ds18b20_therm
import wind_direction
from time import sleep

def main():

    bme280_sensor = temp_bme280.BME280()
    humidity, pressure, temp_celsius = bme280_sensor.read_values()
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    print("HUMIDITY : ",humidity," RH%")
    print("PRESSURE : ",pressure," hPa")
    print("TEMPERATURE : ",temp_celsius," °C ", temp_fahrenheit," °F")


    try:
        ds18b20_sensor = ds18b20_therm.DS18B20()
        surface_temp_c, surface_temp_f = ds18b20_sensor.read_temp()
        print(f"SURFACE TEMPERATURE: {surface_temp_c}°C / {surface_temp_f}°F")
    except AttributeError:
        print("Failed to read Surface temperature.")

    interrupt_client_instance = interrupt_client.interrupt_client(port=49502)
    print(f"RAIN in mm: {interrupt_client_instance.get_rain()}")
    print(f"WIND in kmph: {interrupt_client_instance.get_wind()}")
    print(f"GUST in kmph: {interrupt_client_instance.get_wind_gust()}")

    wind_dir_sensor = wind_direction.wind_direction()
    print(f"WIND DIRECTION: {wind_dir_sensor.get_wind_direction()}")

    print()

    interrupt_client_instance.reset()

if __name__ == "__main__":
    main()
