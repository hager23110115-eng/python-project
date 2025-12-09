import threading
import time

resource_1=threading.Lock()
resource_2=threading.Lock()

def rec_1():
    with resource_1:
        print("thread 1 acquire resource 1")
        time.sleep(0.02)
        print("thread 1 waiting resource 2")
    with resource_2:
        print("thread 1 acquire resource 2 complete")
        

def rec_2():
    with resource_2:
        print("thread 2 acquire resource 2")
        time.sleep(0.02)
        print("thread 2 waiting resource 1")
        with resource_1:
             print("thread 2 acquire resource 1 complete")
             
             

a=threading.Thread(target=rec_1)  
b=threading.Thread(target=rec_2)

a.start()
b.start()  

a.join()
b.join()
             

        
