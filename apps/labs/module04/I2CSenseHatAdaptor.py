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
        #1.Read H0_rH and H1_rH coefficients
        H0_rh = i2cBus.read_byte_data(humidAddr,0x30)>>1
        H1_rh = i2cBus.read_byte_data(humidAddr,0x31)>>1
        
        #2.Read H0_T0_OUT
        H0_T0_36 = i2cBus.read_byte_data(humidAddr,0x36)
        H0_T0_37 = i2cBus.read_byte_data(humidAddr,0x37) 
        H0_T0_out = (H0_T0_37<<8) | H0_T0_36
       
        #3.Read H1_T0_OUT
        H1_T0_3A = i2cBus.read_byte_data(humidAddr,0x3A)
        H1_T0_3B = i2cBus.read_byte_data(humidAddr,0x3B)
        H1_T0_out = (H1_T0_3B<<8) | H1_T0_3A
        H1_T0_out = self.checknegative(H1_T0_out)
        
        #4.Read H_T_OUT
        H_T_28 = i2cBus.read_byte_data(humidAddr,0x28)
        H_T_29 = i2cBus.read_byte_data(humidAddr,0x29)
        H_T_out = (H_T_29<<8) | H_T_28
        H_T_out = self.checknegative(H_T_out)
        
        #5.Compute the RH [%] value by linear interpolation
        tmp = (H_T_out - H0_T0_out) * (H1_rh - H0_rh)
        humidity = (tmp/(H1_T0_out - H0_T0_out) + H0_rh)
        
        #Saturation condition
        if(humidity>100):
            humidity = 100
        
        return humidity
        #logging.info("humidity from i2c:" + str(humidity))

    def displayTemperatureData(self):
        #1. Read from 0x32 & 0x33 registers the value of coefficients T0_degC_x8 and T1_degC_x8
        T0_degC_x8 = i2cBus.read_byte_data(humidAddr,0x32)
        T1_degC_x8 = i2cBus.read_byte_data(humidAddr,0x33)
        #2. Read from 0x35 register the value of the MSB bits of T1_degC and T0_degC 
        T_degC_x8_H = i2cBus.read_byte_data(humidAddr,0x35)
        
        #Calculate the T0_degC and T1_degC values
        T0_degC_x8_u16 = ((T_degC_x8_H & 0x03)<<8) | T0_degC_x8
        T1_degC_x8_u16 = ((T_degC_x8_H & 0x0C)<<6) | T1_degC_x8
        T0_degC = T0_degC_x8_u16>>3
        T1_degC = T1_degC_x8_u16>>3
        
        #3 Read from 0x3C & 0x3D registers the value of T0_OUT
        T0_OUT_L = i2cBus.read_byte_data(humidAddr,0x3C)
        T0_OUT_H = i2cBus.read_byte_data(humidAddr,0x3D)
        T0_OUT = (T0_OUT_H<<8)|T0_OUT_L
        
        #4.Read from 0x3E & 0x3F registers the value of T1_OUT
        T1_OUT_L = i2cBus.read_byte_data(humidAddr,0x3E)
        T1_OUT_H = i2cBus.read_byte_data(humidAddr,0x3F)
        T1_OUT = (T1_OUT_H<<8)|T1_OUT_L
        
        #5.Read from 0x2A & 0x2B registers the value T_OUT (ADC_OUT).
        T_OUT_L = i2cBus.read_byte_data(humidAddr,0x2A)
        T_OUT_H = i2cBus.read_byte_data(humidAddr,0x2B)
        T_OUT = (T_OUT_H<<8)|T_OUT_L
        
        # 6.Compute the Temperature value by linear interpolation
        tmp32 = ((T_OUT - T0_OUT)) * ((T1_degC - T0_degC));
        temperature = tmp32 /(T1_OUT - T0_OUT) + T0_degC;
        
        return temperature
        #logging.info("temperature from i2c:"+str(temperature))
    
    #if data is negative integer, call this method        
    def checknegative(self,data):
        if(data>=0x8000):
            data=data-1
            data=data^0xffff
            data = 0-data
        return data
       
    def run(self):
        while True:
            #if self.enableEmulator:
                # NOTE: you must implement these methods
                #self.displayAccelerometerData()
                #self.displayMagnetometerData()
                #self.displayPressureData()
            temp = self.displayTemperatureData()
            humidity = self.displayHumidityData()
            logging.info("humidity from i2c:" + str(humidity) + " temperature from i2c:"+str(temp))
            sleep(self.rateInSec)