from datetime import datetime
from time import sleep

# tsüklite liigid:
# 1. while, 2. for, 3. for in
while True:
    praegu = datetime.now()
    print(praegu.strftime("%H:%M:%S")) # "%H:%M:%S" - https://www.geeksforgeeks.org/python-strftime-function/
    sleep(1)

# programmist saad väljuda, kui vajutad ctrl+C