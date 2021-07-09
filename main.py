from MotorModule import Motor
from machine import UART
from utime import sleep
#Ket noi UART chan 6(GP4) 7(GP5)
uart1 = UART(1,115200)
# GPIO 7 In1 & GPIO 8 In2
# GPIO 9 In3 & GPIO 10 In 4
# GPIO 6 EnA & GPIO 11 EnB
motor = Motor(6,7,8,11,9,10)

maxVAl= 0.25 # MAX SPEED cua xe
while True: 
    while uart1.any() > 0:
        rxData = uart1.read(5).decode('utf-8')        
        print(rxData)
    ### Normalization
        curveVal = float(int(rxData)/100)
        # /100 để đồng bộ với joystick 
        # chạy giá trị từ -1 tới 1
        if curveVal>maxVAl:curveVal = maxVAl
        if curveVal<-maxVAl: curveVal = -maxVAl
        motor.move(0.2,curveVal,0.05)

