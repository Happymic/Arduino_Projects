# Untitled - By: michaelli - 周四 7月 29 2021
from machine import PWM,Timer
import machine
import sensor, image, time
from Maix import GPIO
from board import board_info
#from machine import Pin, PWM
from time import sleep_ms
from fpioa_manager import *
import time

from fpioa_manager import fm


print("hi")

ENA = 14
IN1 = 13
IN2 = 12


fm.register(ENA, fm.fpioa.GPIO0)
fm.register(IN1,fm.fpioa.GPIO1)
fm.register(IN2,fm.fpioa.GPIO2)

ENA = GPIO(GPIO.GPIO0, GPIO.OUT)
IN1 = GPIO(GPIO.GPIO1, GPIO.OUT)
IN2 = GPIO(GPIO.GPIO2, GPIO.OUT)



#boot_key = GPIO(GPIO.GPIO3,GPIO.IN)

print(ENA.value())

#ena = PWM(GPIO0,freq = 1000, duty = 0)
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
pwm = machine.PWM(tim,freq = 1000, duty = 30, pin = 10, enable=True)
pwm.enable()

ENA.value(1)
IN1.value(0)
IN2.value(1)
'''
for duty in range(800, 1023 + 1):
    print(duty)
    ena.duty(duty)
    sleep_ms(50)
'''

sleep_ms(10000)

import sensor, image, time, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()

img = image.Image(size=(100, 100))
img2 = img.resize(50, 50)

lcd.init(freq=16000000)

while(True):
    lcd.display(sensor.snapshot())

task = kpu.load(0x300000)
task = kpu.load("/sd/face.kmodel")
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

code = kpu.run_yolo2(task, img)
