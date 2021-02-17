import serial
import time

MCOD1 = ""  # put your trinary code here


arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
time.sleep(2)
arduino.write("start".encode())
print("sent")
ECln1 = 483  # change this value if you have changed in the Arduino code


# send m1cde
i = 0
while i < len(MCOD1):
    while True:
        data = arduino.readline()[:-2]
        var = data.decode()
        if var == "o":
            print("Sending "+str(i)+" to "+str(i+ECln1)+" codes")

            break

    cd = MCOD1[i:i+ECln1]
    print(cd)
    arduino.write(cd.encode())
    i = i+ECln1


print("Compleated")
