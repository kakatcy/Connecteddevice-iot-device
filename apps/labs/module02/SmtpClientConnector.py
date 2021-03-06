'''
Created on Sep 27, 2019

@author: cytang
'''
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from labbenchstudios.common import ConfigUtil
from labbenchstudios.common import ConfigConst

class SmtpClientConnector():
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
    #    logging.info('Configuration data...\n' + str(self.config))
     
    def publishMessage(self, topic, data):
        host= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        port= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)
        fromAddr= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)
        toAddr= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)

        '''        print(host)
        print(port)
        print(fromAddr)
        print(toAddr)
        print(authToken)
    '''        
        #    msg= mimeMultipart()
        msg= MIMEMultipart()
        msg['From']= fromAddr
        msg['To']= toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        #   msgBody = "welcome to python"

        #    msg.attach(mimeText(msgBody)) 
        msg.attach(MIMEText(msgBody)) 
        msgText = msg.as_string()

        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port) 
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken) 
        smtpServer.sendmail(fromAddr, toAddr, msgText) 
        smtpServer.close()