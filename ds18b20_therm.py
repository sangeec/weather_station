import glob
import time

class DS18B20(object):
    def __init__(self):
        # Attempt to find the first device file matching the DS18B20 sensor. If none are found, the path will be None.
        device_files = glob.glob("/sys/bus/w1/devices/28*")
        self.device_file = device_files[0] + "/w1_slave" if device_files else None
        
    def read_temp_raw(self):
        if self.device_file is not None:
            try:
                with open(self.device_file, "r") as file:
                    lines = file.readlines()
                return lines
            except IOError:
                print("Error reading from device file.")
        return None
    
    def crc_check(self, lines):
        # Check if lines are valid and perform CRC check
        if lines and len(lines) > 0:
            return lines[0].strip()[-3:] == "YES"
        return False
    
    def read_temp(self):
        if self.device_file is None:
            print("Device file not found.")
            return None

        temp = [-255,-255]
        attempts = 0
        lines = self.read_temp_raw()
        success = self.crc_check(lines)
        
        while not success and attempts < 3:
            time.sleep(0.2)
            lines = self.read_temp_raw()
            success = self.crc_check(lines)
            attempts += 1
            
        if not success:
            print("CRC check failed after 3 attempts.")
            return None
        
        if success and lines and len(lines) > 1:
            temp_line = lines[1]
            equal_pos = temp_line.find("t=")
            if equal_pos != -1:
                temp[0] = float(temp_line[equal_pos + 2:])/1000.0
                temp[1] = temp[0] * 9.0 / 5.0 + 32.0

        return temp



