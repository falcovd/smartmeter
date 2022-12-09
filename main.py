import serial
import sys

##############################################################################
# CONFIGS
##############################################################################

# DSMR Version 2 or 4. Check: http://domoticx.com/p1-poort-slimme-meter-hardware/
dsmr_version = 4

##############################################################################
# Main program
##############################################################################
print("Smartmeter reader is starting...")

# Set COM port config
ser = serial.Serial()

if dsmr_version == 2:
    ser.baudrate = 9600
    ser.bytesize = serial.SEVENBITS
    ser.parity = serial.PARITY_EVEN
    ser.stopbits = serial.STOPBITS_ONE
else :
    if dsmr_version == 4:
        ser.baudrate = 115200
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
    else :
        sys.exit("Invalid DSMR Version")

ser.xonxoff = 0
ser.rtscts = 0
ser.timeout = 60

ser.port = "/dev/ttyUSB0"

# Open COM port
try:
    ser.open()
    print("Connected...")
except:
    sys.exit("Fout bij het openen van %s." % ser.name)

while True:
    raw = ser.readline()
    raw_as_string = str(raw)
    line = raw_as_string.strip()
    print(line)
