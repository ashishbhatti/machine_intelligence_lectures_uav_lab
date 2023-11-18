'''
Serial Receive Python: Module for serial communication

This will allow us to write/send or receive any command.
For now we will focus on sending part, later we will see the receiving part as well.
We need a library python serial.
'''

import serial
import time

# function to initialize 
def initConnection(portNo, baudRate):
    # because sometimes it fails
    try:                                           
        ser = serial.Serial(portNo, baudRate)
        print("Device Connected Successfully!")
        return ser
    except:
        print("Not Connected!")


# function to send data to arduino
def sendData(se, data, digits):
    '''
    Args:
        se: serial object
        data: data to send in list format
        digits: digits per value
    '''
    myString = '$'
    for d in data:
        myString += str(d).zfill(digits)

    try:
        se.write(myString.encode())
        print(myString)
    except:
        print("Data Transmission Failed!")


if __name__ == "__main__":
    port = '/dev/ttyACM0'                     # Arduino UNO
    # port = '/dev/ttyUSB0'                     # SmartElex Board
    ser = initConnection(port, 9600)
    while True:
        sendData(ser, [50,255], 3)
        time.sleep(1)
        sendData(ser, [0, 0], 3)
        time.sleep(1)

        