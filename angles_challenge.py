#!/usr/bin/env micropython

import sys
import time
import random

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button

import os
#os.system('setfont Lat15-TerminusBold14')
#os.system('setfont Lat15-TerminusBold32x16')
ml=MediumMotor(OUTPUT_A)
mr=MediumMotor(OUTPUT_D)
but = Button()
g=GyroSensor(INPUT_2)
target=g.angle
m=MoveSteering(OUTPUT_B, OUTPUT_C)
#c=ColorSensor(INPUT_1)
#m.on_for_rotations(10,10,5)

def GoStraightGyro (gain,target,speed,rot):
    m.left_motor.position = 0
    while RunForRotations(rot):
        a=g.angle
        difference=(a-target)*gain
        m.on(difference, speed)
    m.off()

def RunForRotations(rotations):
    return abs(m.left_motor.position)<360*rotations
        

#GoStraightGyro(3, target, -10, RunForRotations)

#GoStraightGyro(3, target, -10, RunAgain)

def TurnWithGyro(target):
    c=g.angle
    if target > 0:
        m.on(100, 10)
        while c + target > g.angle:
            pass
    else:
        m.on(-100, 10)
        while c + target < g.angle:
            pass 
    m.off()

def GoStraightForward(rotation):
    GoStraightGyro(-5, g.angle, 10, rotation)

def GoStraightBackward(rotation):
    GoStraightGyro(5, g.angle, -10, rotation)

GoStraightBackward(4.5)
mr.on_for_seconds(10, 2)
GoStraightBackward(1.4)
mr.on_for_seconds(-10, 2)
TurnWithGyro(-80)
GoStraightForward(2.2)
# read color here
TurnWithGyro(60)
GoStraightForward(3)
TurnWithGyro(-90) # -90 degrees for yellow
GoStraightForward(2.5)
ml.on_for_seconds(-30, 2)
ml.on_for_degrees(30, 30)
GoStraightBackward(7)
TurnWithGyro(-90)
GoStraightBackward(1.5)