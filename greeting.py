# Greeting program using current time
# Author: Muhammad Anis Nawab

import time


hour=int(time.strftime('%H'))
name=input("enter your name:")
# hour=int(input("enter your time: "))we also used a user time

if(hour >=0 and hour < 12):
    print("Good Morning !",name)

elif(hour >=12 and hour < 19):
    print("Good after noon !",name)

else:
    print("Good night",name)
    
