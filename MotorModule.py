from machine import Pin, PWM
from utime import sleep

half_speed = 32768
full_speed = 65535

class Motor():
    # EnA is right side gear //EnB is left side gear
    def __init__(self,EnA,In1,In2,EnB,In3,In4):
        self.EnA = EnA
        self.In1 = In1
        self.In2 = In2
        self.EnB = EnB
        self.In3 = In3
        self.In4 = In4
        self.in1 = Pin(self.In1,Pin.OUT)
        self.in2 = Pin(self.In2,Pin.OUT)
        self.enA = PWM(Pin(self.EnA))
        self.in3 = Pin(self.In3,Pin.OUT)
        self.in4 = Pin(self.In4,Pin.OUT)
        self.enB = PWM(Pin(self.EnB))
        self.enA.freq(100)
        self.enB.freq(100)
        
    def move(self,speed=0.5,turn=0,t=0):
        #Normalization
        speed *= full_speed
        turn *= full_speed
        speed = round(speed)
        turn = round(turn)
        #turn to decide left or right, EnA is Right motor, EnB is Left motor
        leftSpeed = speed + turn
        rightSpeed = speed - turn
        if leftSpeed > full_speed: leftSpeed = full_speed
        elif leftSpeed < -full_speed: leftSpeed = -full_speed
        if rightSpeed > full_speed: rightSpeed = full_speed
        elif rightSpeed < -full_speed: rightSpeed = -full_speed
        self.enA.duty_u16(abs(rightSpeed))
        self.enB.duty_u16(abs(leftSpeed))
        
        #forward or backward
        if rightSpeed>0:self.in1.value(1); self.in2.value(0)
        else: self.in1.value(0); self.in2.value(1)
        if leftSpeed>0: self.in3.value(1);self.in4.value(0)
        else: self.in3.value(0);self.in4.value(1)
        sleep(t)
    

    def stop(self, t=0):
        self.enA.duty_u16(0)
        self.enB.duty_u16(0)
        sleep(t)
    
def main():
    motor.move(0.5,0,2)
    motor.stop(2)
    motor.move(-0.5,0,2)
    motor.stop(2)


if __name__ == '__main__':
    motor = Motor(3,4,5,8,6,7)
    main()
    
