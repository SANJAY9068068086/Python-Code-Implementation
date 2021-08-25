# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:00:08 2021

@author: SANJAY PANCHAL
"""

import time

print("Do you want to restart your system")
print('''
      ''')
#print("What will you do ???")
#print("Your have only 2 option : YES & NO")
print("Your answer is case-sensitive , please press carefully")
a1=input("Press YES or NO : ")
print(''' ''')
#seconds=int(input("Enter seconds to remain : "))
if a1=='YES':
    seconds=int(input("Enter seconds to remain : "))
    print("Your Time is Start : ")
    print('''
          ''')
    for i in range(seconds):
        print(str(seconds-i)+" : seconds remaining\a")
        time.sleep(1)
    #print("April Fool, HA ! HA ! HA ! HA !!!!!\f")
    import os;
    os.system("shutdown /s /t 0")
elif a1=='NO':
        print("You STOPPED restart command......")
        print('''
          ''')
else:
    print('''Your Entered Wrong Key !!!!!
Please restart the programm''')
#print("April Fool, HA ! HA ! HA ! HA !!!!!") 
    
