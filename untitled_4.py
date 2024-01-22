from fpioa_manager import fm    # 导入库
from Maix import GPIO

io_led_red = 13
fm.register(io_led_red, fm.fpioa.GPIO0)

led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(1)
print("hi")

