# import the time module
import time

# define the countdown func.
def countdown(t):
    while t>=1:
        min,sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format (min, sec)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1

    print('time over')

t = input ("Enter the time in second: ")

countdown(int(t))
