import bme280
import smbus2



class BME280:
    
    def __init__(self,port = 1,address = 0x76):
        self.bus = smbus2.SMBus(port)
        self.address = address
        

    def read_values(self):
        array = [-255,-255,-255]
        bme280.load_calibration_params(self.bus,self.address)
        bme280_data = bme280.sample(self.bus,self.address)
        array[0]  = bme280_data.humidity
        array[1]  = bme280_data.pressure
        array[2] = bme280_data.temperature
        return array
    
    
    
    