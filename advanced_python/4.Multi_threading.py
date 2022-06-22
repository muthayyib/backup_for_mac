from threading import Thread
#importing sleep to give some sleep to thread
from time import sleep
#inherit the threading
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(.5)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(.5
            )

t1 = Hello()
t2 = Hi()
t1.start()
#to avoid collision when both thread wakes up simltaneosly
sleep(.1)
t2.start()

#there are 3 threads here t1,t2 and main. main will execute poddddddddda.
#to make wate main to join t1 and t2 to main we use join method
t1.join()
t2.join()
print("podddddddddddddddddaaaaaaaaaaaa")