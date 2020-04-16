#! python3
# pell-trainer.py - a training program for use with pell practice.
#
#

import time, subprocess
from os import listdir
from random import randint, choice
from pathlib import Path


fullTime = 172 # how many counts the program lasts, each 0.7s
shortest = 1
longest = 5

def populateSounds():
    return listdir(path='audio')

def playSound():
    sound = choice(soundList)
    subprocess.Popen(['start', Path('audio',sound)], shell=True)

def soundTimer(sounds):
    return randint(shortest, longest), choice(sounds)

soundList = populateSounds()
strike = fullTime - randint(shortest, longest)
while fullTime > 0:
    #print(fullTime, end=' ')
    if strike == fullTime:
        playSound()
        strike = fullTime - randint(shortest, longest)
    time.sleep(0.7)
    fullTime -= 1
time.sleep(2)
playSound()
    
