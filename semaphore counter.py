import threading
import time
recipationcet=threading.Semaphore(5)
def exmainationroom(n):
    print(f"patient {n} waiting of the turn")
    recipationcet.acquire()
    print(f"patient {n} in the room")
    time.sleep(3)
    print(f"patient {n} out of the room")
    recipationcet.release()
patientlist=[]
for i in range(6):
    patient=threading.Thread(target=exmainationroom,args=(i,))
    patientlist.append(patient)
    patient.start()    