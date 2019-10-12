import smbus
import threading
import logging
import sys

from time import sleep
from labbenchstudios.common import ConfigUtil
from labbenchstudios.common import ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +
enableControl = 0x2D  
enableMeasure = 0x08  
accelAddr = 0x1C  # address for IMU (accelerometer)
magAddr = 0x6A    # address for IMU (magnetometer)
pressAddr = 0x5C  # address for pressure sensor
humidAddr = 0x5F  # address for humidity sensor

begAddr = 0x28
totBytes = 6

DEFAULT_RATE_IN_SEC = 5


class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        self.initI2CBus()
        
    def initI2CBus(self):
        logging.info("Initializing I2C bus and enabling I2C addresses...")
        i2cBus.write_byte_data(accelAddr, 0, 0)
        i2cBus.write_byte_data(magAddr, 0, 0)
        i2cBus.write_byte_data(pressAddr, 0, 0)
        #i2cBus.write_byte_data(humidAddr, 0, 0)
        
    def displayHumidityData(self):
        H0_rh = i2cBus.read_byte_data(humidAddr,0x30)>>1
        H1_rh = i2cBus.read_byte_data(humidAddr,0x31)>>1
        print(sys.getsizeof(H0_rh))
        print(i2cBus.read_byte_data(humidAddr,0x30))
        print(i2cBus.read_byte_data(humidAddr,0x31))
        print("H0_rh:"+str(H0_rh))
        print("H1_rh:"+str(H1_rh)+"\n")
        
        H0_T0_36 = i2cBus.read_byte_data(humidAddr,0x36)
        H0_T0_37 = i2cBus.read_byte_data(humidAddr,0x37) 
        H0_T0_out = (H0_T0_37<<8) | H0_T0_36
        print(sys.getsizeof(H0_T0_37))
        print(sys.getsizeof(H0_T0_36))
        print(str(H0_T0_37 & 0xffff))
        print(str(H0_T0_36 & 0xffff))
        print(sys.getsizeof(H0_T0_out))
        print(str(H0_T0_out & 0xffffff))
        print("H0_T0_36:"+str(H0_T0_36)+" H0_T0_37:"+str(H0_T0_37))
        print("H0_T0_out:"+str(H0_T0_out)+"\n")
       
        H1_T0_3A = i2cBus.read_byte_data(humidAddr,0x3A)
        H1_T0_3B = i2cBus.read_byte_data(humidAddr,0x3B)
        H1_T0_out = (H1_T0_3B<<8) | H1_T0_3A
        H1_T0_out = self.checknegative(H1_T0_out)
        print(sys.getsizeof(H1_T0_3A))
        print(sys.getsizeof(H1_T0_3B))
        print(str(H1_T0_3A& 0xffff))
        print(str(H1_T0_3B& 0xffff))
        print(sys.getsizeof(H1_T0_out))
        print(str(H1_T0_out& 0xffffff))
        print("H1_T0_3A:"+str(H1_T0_3A)+" H1_T0_3B:"+str(H1_T0_3B))
        print("H1_T0_out:"+str(H1_T0_out)+"\n")

        
        H_T_28 = i2cBus.read_byte_data(humidAddr,0x28)
        H_T_29 = i2cBus.read_byte_data(humidAddr,0x29)
        H_T_out = (H_T_29<<8) | H_T_28
        H_T_out = self.checknegative(H_T_out)
        print(sys.getsizeof(H_T_28))
        print(sys.getsizeof(H_T_29))
        print(str(H_T_28& 0xffff))
        print(str(H_T_29& 0xffff))
        print(sys.getsizeof(H_T_out))
        print(str(H_T_out& 0xffffff))
        print("H_T_28:"+str(H_T_28)+" H_T_29:"+str(H_T_29))
        print("H_T_out:"+str(H_T_out)+"\n")
        
        tmp = (H_T_out - H0_T0_out) * (H1_rh - H0_rh)
        humidity = (tmp/(H1_T0_out - H0_T0_out) + H0_rh)
        print("humidity:" + str(humidity)+"\n")
        
        if(humidity>1000):
            humidity = 1000

        print("humidity:" + str(humidity))
    
    def checknegative(self,data):
        if(data>=0x80):
            data=data-1
            print("negative:"+str(data))
            data=data^0xffff
            print("negative:"+str(data))
            data = 0-data
            print("negative:"+str(data))
        return data
       
    def run(self):
        while True:
            #if self.enableEmulator:
                # NOTE: you must implement these methods
                #self.displayAccelerometerData()
                #self.displayMagnetometerData()
                #self.displayPressureData()
            self.displayHumidityData()
            sleep(self.rateInSec)