import machine
from machine import Pin, Timer

intled = machine.Pin("LED", machine.Pin.OUT)
tim = Timer()
def tick(timer):
    intled.toggle()
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)