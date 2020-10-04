import random
import time

remember = []
i = 0
while i<10:
        lol = random.randint(1,298)
        if lol not in remember :
            remember.append( lol )
        i= i+1
print(remember)
while True:
    time.sleep(90)