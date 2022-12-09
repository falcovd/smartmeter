import serial
import sys

##############################################################################
#Main program
##############################################################################
print("Smartmeter reader is starting...")

#Set COM port config
ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.SEVENBITS
ser.parity = serial.PARITY_EVEN
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = 0
ser.rtscts = 0
ser.timeout = 20
ser.port = "/dev/ttyUSB0"

#Open COM port
try:
    ser.open()
    print("Connected...")
except:
    sys.exit ("Fout bij het openen van %s. Aaaaarch."  % ser.name)
