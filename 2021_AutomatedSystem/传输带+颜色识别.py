# Untitled - By: michaelli - 周五 7月 30 2021
import machine
from machine import PWM,Timer
import machine
import sensor, image, time
from Maix import GPIO
from board import board_info
from machine import PWM
from time import sleep_ms
from fpioa_manager import *
import time
import socket
from fpioa_manager import *
from Maix import I2S, GPIO
import audio
import image
import lcd
import time
from fpioa_manager import fm
print("hi")

ENA = 14
IN1 = 13
IN2 = 12
count_sensor = 22
countnumber = 21
SEND = 3
YELLOW = 15

fm.register(ENA, fm.fpioa.GPIO0)
fm.register(IN1,fm.fpioa.GPIO1)
fm.register(IN2,fm.fpioa.GPIO2)
fm.register(SEND, fm.fpioa.GPIO3)
fm.register(count_sensor,fm.fpioa.GPIO4)
fm.register(YELLOW,fm.fpioa.GPIO5)
fm.register(countnumber,fm.fpioa.GPIO6)
ENA = GPIO(GPIO.GPIO0, GPIO.OUT)
IN1 = GPIO(GPIO.GPIO1, GPIO.OUT)
IN2 = GPIO(GPIO.GPIO2, GPIO.OUT)
SEND = GPIO(GPIO.GPIO3,GPIO.OUT)
count_sensor = GPIO(GPIO.GPIO4,GPIO.IN)
YELLOW = GPIO(GPIO.GPIO5,GPIO.OUT)
countnumber = GPIO(GPIO.GPIO6,GPIO.IN)
def on_timer(timer):
    ENA.value(0)
    IN1.value(0)
    IN2.value(1)
    print("time up:",timer)
    print("param:",timer.callback_arg())

SEND.value(0)
YELLOW.value(0)
print(ENA.value())

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
pwm = machine.PWM(tim,freq = 500, duty = 5, pin = 10, enable=True)
pwm.enable()

ENA.value(0)
IN1.value(1)
IN2.value(1)
sleep_ms(5000)

lcd.init(freq=18000000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
yellow_threshold  = (100, 81, -15, -80, 70, 121)
number_blocks = 0
#red_threshold = (21, 98, 12, 127, 108, -39)
exsistence = 0
count = 0
block = 0
go = 0
#run_signal = GPIO(GPIO.GPIO13,GPIO.OUT)
while block < 7:
    img=sensor.snapshot()
    blobs = img.find_blobs([yellow_threshold])
    lcd.display(img)
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])
            tmp=img.draw_cross(b[5], b[6])
            c=img.get_pixel(b[5], b[6])
            go = 1
            SEND.value(1)
        if count_sensor.value() ==0 and go == 1:
            ENA.value(0)
            IN1.value(1)
            IN2.value(0)
            SEND.value(1)
            YELLOW.value(1)
            while blobs == img.find_blobs([yellow_threshold]):
                SEND.value(1)
                YELLOW.value(1)
        if count_sensor.value() ==1 or go == 0:
            go = 0
            SEND.value(0)
            YELLOW.value(0)
            ENA.value(0)
            IN1.value(1)
            IN2.value(1)
    while countnumber.value() == 0:
        sleep_ms(200)
        if countnumber.value() == 1:
                block = block + 1
                print("There's already: ", block)
'''
while True:
    if block == 8 and blobs == img.find_blobs([yellow_threshold]):
        SEND.value(1)
        YELLOW.value(1)
        ENA.value(0)
        IN1.value(1)
        IN2.value(0)
    else:
        break
'''
sleep_ms(2000)
ADDR = ("192.168.43.73", 10000)
sock = socket.socket()
sock.connect(ADDR)
sock.settimeout(1)
print("connect to server")

def play_music():
    # disable wifi
    fm.register(8, fm.fpioa.GPIO0)
    wifi_en=GPIO(GPIO.GPIO0,GPIO.OUT)
    wifi_en.value(0)

    # register i2s(i2s0) pin
    fm.register(34,fm.fpioa.I2S0_OUT_D1)
    fm.register(35,fm.fpioa.I2S0_SCLK)
    fm.register(33,fm.fpioa.I2S0_WS)

    # init i2s(i2s0)
    wav_dev = I2S(I2S.DEVICE_0)

    # init audio
    player = audio.Audio(path = "/sd/kabuda.wav")
    player.volume(100)

    # read audio info
    wav_info = player.play_process(wav_dev)
    print("wav file head information: ", wav_info)

    # config i2s according to audio info
    wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER,resolution = I2S.RESOLUTION_16_BIT ,cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
    wav_dev.set_sample_rate(wav_info[1])
    while True:
        ret = player.play()
    player.finish()
while 1:
    sock.send("hello\n")
    #data = sock.recv(10) # old maxipy have bug (recv timeout no return last data)
    #print(data) # fix
    try:
      #play_music()
      data = b""
      while True:
        tmp = sock.recv(1)
        print(tmp)
        play_music()
        if len(tmp) == 0:
            raise Exception('timeout or disconnected')
        data += tmp
    except Exception as e:
      print("rcv:", len(data), data)
      play_music()
sock.close()
