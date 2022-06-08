import time
import RPi.GPIO as GPIO

usleep = lambda x: time.sleep(x/1000000.0) 
DIR = 23 #Direction
STEP = 18 # Steps


GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT) 
GPIO.setup(DIR, GPIO.OUT)


def SpinMotor(direction, num_steps):
    GPIO.output(DIR, direction)
    for x in range(num_steps):
        GPIO.output(STEP,GPIO.HIGH)
        usleep(100) #Microseconds
        GPIO.output(STEP,GPIO.LOW)
        usleep(100) 
    GPIO.cleanup()  
    return True
    
direction_input = input("Entre O ou C para abrir ou fechar: ")
num_steps = int(input('Por favor entre com o número de passos: '))
if direction_input == 'C':
    SpinMotor(False, num_steps)
else:
    SpinMotor(True, num_steps)
