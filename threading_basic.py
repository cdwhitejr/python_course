#threading

import time, random, os
from threading import Thread

def example():

    def countdown(n):
        while n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

    # create and launch a thread
    t = Thread(target=countdown, args=(10,))

    t.start()



def worker(num):
    print('I am worker',num,'my ppid is',os.getpid())
    time.sleep(random.randint(1,3))
    print

threads = []
for i in range(11):
    t = Thread(target=worker,args=(i,))
    threads.append(t)
    
    t.start()
    t.join()