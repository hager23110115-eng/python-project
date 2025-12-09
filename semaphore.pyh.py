import threading 
import time

recpationcet=threading.Semaphore(1)
def examiantionroom(num):
    
    print(f"patient {num} waiting of the turn ")
    recpationcet.acquire()
    print(f"patient {num} in the room")
    time.sleep(2)
    print(f"patient {num} out of the room")
    recpationcet.release()
    
patientlist=[]  
for i in range(5):
    patient=threading.Thread(target=examiantionroom,args= (i,))
    patientlist.append(patient)
    patient.start()
    

    
