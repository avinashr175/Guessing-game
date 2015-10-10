import random
import time
time1=time.time()


    

ans = random.randint(1,10)
count=0
while True:
    c=int(raw_input('Guess the number.'))
   
    if c<ans:
            print'too low!'
            count=count+1
    elif c>ans:
            print 'too high'
            count=count+1
    elif c==ans:
            break

print ("Congrats u got it.")
time2=time.time()
totaltime=time2-time1
print 'the total time taken is', totaltime,  'seconds and the number of times u tried is',count


