import smbus
import threading
import logging

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
        i2cBus.write_byte_data(humidAddr, 0, 0)
        
    def displayHumidityData(self):
        buffer = i2cBus.read_i2c_block_data(humidAddr,begAddr,4)
        H0_rh = buffer[2]>>1
        H1_rh = buffer[3]>>1
        print("H0_rh:"+str(H0_rh))
        print("H1_rh:"+str(H1_rh))
        buffer_h0t0out = i2cBus.read_i2c_block_data(humidAddr,0x36,2)
        H0_T0_out = (buffer_h0t0out[1]<<8) | buffer_h0t0out[0]
        print("H0_T0_out:"+str(H0_T0_out))
        
        buffer_h1t0out = i2cBus.read_i2c_block_data(humidAddr,0x3A,2)
        H1_T0_out = (buffer_h1t0out[1]<<8) | buffer_h1t0out[0]
        print("H1_T0_out:"+str(H1_T0_out))
        
        H_T_out = (buffer[1]<<8) | buffer[0]
        print("H_T_out:"+str(H_T_out))
        
        tmp = (H_T_out - H0_T0_out) * (H1_rh - H0_rh)*10
        humidity = (tmp/(H1_T0_out - H0_T0_out) + H0_rh*10)
        print("humidity:" + str(humidity))
        
        if(humidity>1000):
            humidity = 1000

        print("humidity:" + str(humidity))
       
    def run(self):
        while True:
            #if self.enableEmulator:
                # NOTE: you must implement these methods
                #self.displayAccelerometerData()
                #self.displayMagnetometerData()
                #self.displayPressureData()
            self.displayHumidityData()
            sleep(self.rateInSec)