import subprocess
import time
t = 1707
while True:
    subprocess.run(["sudo","./adxl345spi","-t","5","-s","0529"+str(t)+"_0_1.5_3200_5_.csv"])
    time.sleep(300)
    t = t + 5 