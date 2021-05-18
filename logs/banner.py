#!/usr/bin/python3
# This code write by Ms.nope
import os
import time
import sys
class color:
      red = '\033[92m'
      green = '\033[92m'
      End = '\033[0m'
      blue = '\033[96m'
def cls():
    os.system("clear")
def about():
    os.system("printf '\033]2;About\a'")
    cls()
    os.system("figlet Ms.programmer")
    time.sleep(0.1)
    print(color.red + "\nThis code write by " + color.green + "Ms.nope" + color.End)
    time.sleep(0.3)
    print(color.red + "\nGithub: " + color.blue + "https://github.com/msprogrammer2938" + color.End)
    print("\nCode Name: 20")
    time.sleep(2)
    try1()
def try1():
    try2 = input("\npress Enter...")
    if try2 == '':
      os.system("python3 20")
    else:
        os.system("python3 20")
