import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time
import random

def StopAndPickNewDirection():
    fc.stop()
    fc.backward(20)
    time.sleep(0.3)
    turnRight = random.randint(0,1)
    if(turnRight):
        fc.turn_right(50)
    else:
        fc.turn_left(50)
    turnTime = random.random() + 0.1
    time.sleep(turnTime)
    fc.stop()

def ObstacleAvoidance():
    power = 0
    maxPower = 40
    while True:        
        scanList = fc.scan_step(35)
        if not scanList:
            continue

        print(scanList)
        if scanList[3:7] != [2,2,2,2]:
            StopAndPickNewDirection()
            power = 0
        
        time.sleep(0.1)
        power += 5
        if(power >= maxPower):
            power = maxPower
        print(power)
        fc.forward(power)
        
if __name__ == '__main__':
    try:
        ObstacleAvoidance()
    finally:
        fc.stop()

