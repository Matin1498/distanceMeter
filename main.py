import lcddriver
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

display = lcddriver.lcd()

TRIG = 23
ECHO = 24

print("Distance Measurement in Progress")
display.lcd_display_string("Distance: ", 1)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        
        GPIO.output(TRIG, False)
        print("Waiting for sensor to settle")
        
        time.sleep(2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == False:
            start = time.time()
        while GPIO.input(ECHO) == True: 
            end = time.time()
            
        sig_time = end-start
        
        distance = sig_time / 0.000058
        
        distance = round(distance, 2)
        
        result = str(distance)+" cm"
        display.lcd_display_string(result,2);
        
        if distance < 10:
            for i in range(5):
                time.sleep(0.1)
                GPIO.output(6,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(6,GPIO.LOW)
        
        if distance > 10:
            for i in range(5):
                time.sleep(0.1)
                GPIO.output(5,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(5,GPIO.LOW)
        
except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()