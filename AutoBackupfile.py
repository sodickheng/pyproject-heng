import shutil
import schedule
import datetime
import time

def backup_files():
    source = 'testing1.txt'
    destination = 'testing2.txt'
    shutil.copy(source, destination)
    print(f"file copied successfully at {datetime.datetime.now()}")

schedule.every().day.at("21:23").do(backup_files)

while True:
    schedule.run_pending()
    time.sleep(1)

