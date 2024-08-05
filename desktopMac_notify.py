import os
import time

def notify_me(title, message):
    os.system(f"""
              osascript -e 'display notification "{message}" with title "{title}"'
              """)

if __name__ == "__main__":
    while True:
        notify_me("Time to take a break!", "Remember to rest your eyes for a few minutes.")
        time.sleep(10)  # Notify every hour (60 * 60)
