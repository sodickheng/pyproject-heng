# import the module
import time

# define the countdown func.
def countdown(t):
#This line starts a while loop that will continue to run as long as t is not zero.
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # use terminal to see timer overwrite
        time.sleep(1)
        t -=1

    print("Countdown timer Ended")

# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
