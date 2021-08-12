from datetime import datetime
import time
then = datetime.now()

time.sleep(10)


now  = datetime.now()

duration = now - then 
duration_in_s = duration.total_seconds()
x=int(str(duration_in_s).split(".")[0])
print(x)
print(time.strftime('%H:%M:%S', time.gmtime(x)))
