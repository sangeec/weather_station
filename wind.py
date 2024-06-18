from gpiozero import Button
import math
import statistics
import time
# wind_speed_sensor = Button(5)
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1
  #  print("spin" + str(wind_count))
  
def calculate_speed(time_sec):
    
    global wind_count
    global radius_cm
    global wind_interval
    radius_cm = 9.0
    wind_interval = 5
    
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0
    dist_km = circumference_cm * rotations / 100000
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600
    
    return km_per_hour 
    #speed = dist_cm / wind_intervaL
def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin
store_speeds = []
while True:
    wind_interval = 5
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)
        
    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(wind_speed, wind_gust)