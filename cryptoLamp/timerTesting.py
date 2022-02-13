from threading import Timer
import time

"""
links:
    https://stackoverflow.com/questions/3433559/python-time-delays

"""
def hello():
    for x in range(10):
        print("hi")

def bye():
    print("BYE") 

count = 0
while count <= 4:
    if keyboard.is_pressed('q'):
        break
    hello()
    time.sleep(10)
    bye()
    count+=1





















































