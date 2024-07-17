import time

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        print(timer, end="\r")
        time.sleep(1)
        t -=1


    print("Countdown timer End")

t = input("Enter the time in seconds ")

countdown(int(t))
