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
        H0_rh = i2cBus.read_byte_data(humidAddr,0x30)
        H1_rh = i2cBus.read_byte_data(humidAddr,0x31)
        H0_rh1 = i2cBus.read_byte_data(humidAddr,0x30)>>1
        H1_rh1 = i2cBus.read_byte_data(humidAddr,0x31)>>1
        print("H0_rh:"+str(H0_rh) + " H0_rh1:"+str(H0_rh1))
        print("H1_rh:"+str(H1_rh) + " H1_rh1:"+str(H1_rh1))
        
        buffer_h0t0out = i2cBus.read_i2c_block_data(humidAddr,0x36,2)
        H0_T0_out = (buffer_h0t0out[1]<<8) | buffer_h0t0out[0]
        
        H0_T0_out1 = (i2cBus.read_byte_data(humidAddr,0x37)<<8) | i2cBus.read_byte_data(humidAddr,0x36)
        H0_T0_36 = i2cBus.read_byte_data(humidAddr,0x36)
        H0_T0_37 = i2cBus.read_byte_data(humidAddr,0x37) 
        
        print("H0_T0_out:"+str(H0_T0_out)+" H0_T0_out1:"+str(H0_T0_out1))
        print("H0_T0_36:"+str(H0_T0_36)+" H0_T0_37:"+str(H0_T0_37))
        
        buffer_h1t0out = i2cBus.read_i2c_block_data(humidAddr,0x3A,2)
        H1_T0_out = (buffer_h1t0out[1]<<8) | buffer_h1t0out[0]
        H1_T0_3A = i2cBus.read_byte_data(humidAddr,0x3A)
        H1_T0_3B = i2cBus.read_byte_data(humidAddr,0x3B)
        H1_T0_out1 = (H1_T0_3B<<8) | H1_T0_3A
        print("H1_T0_out:"+str(H1_T0_out) + " H1_T0_out1:"+str(H1_T0_out1))
        print("H1_T0_3A:"+str(H1_T0_3A)+" H1_T0_3B:"+str(H1_T0_3B))
        
        H_T_out = (buffer[1]<<8) | buffer[0]
        H_T_28 = i2cBus.read_byte_data(humidAddr,0x28)
        H_T_29 = i2cBus.read_byte_data(humidAddr,0x29)
        H_T_out1 = (H_T_29<<8) | H_T_28
        print("H_T_out:"+str(H_T_out) +" H_T_28:"+str(H_T_28)+" H_T_29:"+str(H_T_29)  )
        print("H_T_out1:"+str(H_T_out1))
        
        tmp = (H_T_out - H0_T0_out) * (H1_rh - H0_rh)*10
        humidity = (tmp/(H1_T0_out - H0_T0_out) + H0_rh*10)
        print("humidity:" + str(humidity))
        
        tmp1 = (H_T_out1 - H0_T0_out1) * (H1_rh1 - H0_rh1)*10
        humidity1 = (tmp1/(H1_T0_out1 - H0_T0_out1) + H0_rh1*10)
        if(humidity>1000):
            humidity = 1000

        print("humidity:" + str(humidity))
        print("humidity1:" + str(humidity1))
       
    def run(self):
        while True:
            #if self.enableEmulator:
                # NOTE: you must implement these methods
                #self.displayAccelerometerData()
                #self.displayMagnetometerData()
                #self.displayPressureData()
            self.displayHumidityData()
            sleep(self.rateInSec)