import threading
import time

def fun(second):
    print("you have to wait for",second,'second')
    time.sleep(second)
print('\n')
time1 = time.perf_counter()
# normal code
# fun(2)    
# fun(3)    
# fun(2)    
# time2 = time.perf_counter()
# print(time2 - time1)

# same code using thread
t1 = threading.Thread(target=fun ,args=[2])
t2 = threading.Thread(target=fun ,args=[3])
t3 = threading.Thread(target=fun ,args=[2])

t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()
time2 = time.perf_counter()
print(time2 - time1)

# also explore concurrent.features from ThreadPoolExecuter

