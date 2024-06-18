import temp_bme280
import interrupt_client
import wind_direction
from time import sleep


   
interrupts = interrupt_client.interrupt_client(port = 49502)

while(1):

    print("RAIN in mm: %s" % interrupts.get_rain())
    print()
    sleep(2)

