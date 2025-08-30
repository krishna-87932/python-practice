import serial
import time

arduino= serial.Serial('COM6', 9600)
time.sleep(2)

def send_angle(angle):
    arduino.write(f'{angle}\n'.encode())
    print(f"dent angle {angle}")

for angle in range(0,181,30):
    send_angle(angle)
    time.sleep(1)
# for angle in range(180, -1,-30):
#     send_angle(angle)
#     time.sleep(1)
time.sleep(2)
for i in range(10):
    
    send_angle(-30)
    time.sleep(1)