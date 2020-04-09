#! python3
# pell-trainer.py - a training program for use with pell practice.
#
#

import time, subprocess
from os import listdir
from random import randint, choice


fullTime = 50
shortest = 1
longest = 8

def populateSounds():
    return listdir(path='audio')

def playSound():
    sound = choice(soundList)
    subprocess.Popen(['start', 'audio\\'+sound], shell=True)

def soundTimer(sounds):
    return randint(shortest, longest), choice(sounds)

soundList = populateSounds()
strike = fullTime - randint(shortest, longest)
while fullTime > 0:
    print(fullTime, end=' ')
    if strike == fullTime:
        playSound()
        strike = fullTime - randint(shortest, longest)
    time.sleep(1)
    fullTime -= 1
playSound()
    
