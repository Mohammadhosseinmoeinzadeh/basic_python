from datetime import datetime
import time
sec = -1
while sec != 0:
    timer = datetime.now()
    print(timer.hour,timer.minute,timer.second)
    sec = timer.second
    time.sleep(1)
