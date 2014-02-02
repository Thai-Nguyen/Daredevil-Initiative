""" 
UltrasonicRangeFinder class

Used to receive data from the Maxsonar EZ4 1240

Author: Thai Nguyen
Date: January 31, 2014

Revisions:
Feb 1, 2014 - Added flushInput to remove lag in data reading
"""

import serial
import RPi.GPIO as GPIO

class UltrasonicRangeFinder:
    def __init__(self, device_id, serial_port = "/dev/ttyAMA0"):
        """
        Constructor method
        device_id - use to determine which sensor transmits data
        serial_port - determine where to read the data (default of
	                        /dev/ttyAMA0)
    	""" 
        self.device_id = device_id
        self.serial_port = serial_port
        self.ser = serial.Serial(self.serial_port)
        
    def __del__(self):
        """
        Destructor closes port
        """
        self.ser.close()
    
    def read_data(self):
        """ Gets the distance in centimetres from the ultrasonic rangefinder """ 
        self.ser.flushInput()
        data = self.ser.read(5)
        return int(data.replace("R", "")) #should remove the R

# This is just test code. Create an instance of the UltrasonicRangeFinder 
# in your main program instead.
if __name__ == "__main__":
    import time
    sensor_1 = UltrasonicRangeFinder(1) # Create an instance of 
                                        # UltrasonicRangeFinder with an ID
                                        # of 1
    while(1):
        distance = sensor_1.read_data()
        print distance
        time.sleep(1)
