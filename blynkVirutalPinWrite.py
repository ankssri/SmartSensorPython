from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat
import hat

setScreenColor(0x111111)

hat_pir3 = hat.get(hat.PIR)

VC = None



from numbers import Number




setScreenColor(0xff0000)
import BlynkLib
BLYNK_AUTH = 'cZzy_x2WrcU_HXNCkbR2M_UPzcT-YxPw'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@timerSch.event('__blynk_timer')
def __blink_timer():
  blynk.run()
timerSch.run('__blynk_timer', 2, 0x00)

wait(10)
VC = 0
while True:
  if (hat_pir3.state) == 1:
    setScreenColor(0x33ff33)
    VC = (VC if isinstance(VC, Number) else 0) + 1
    blynk.virtual_write(0, (str(VC)))
    wait(5)
    setScreenColor(0x3366ff)
    wait(5)
  wait_ms(2)
