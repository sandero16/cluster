from mpi4py import MPI
import numpy
import time

def computeprime (num) :
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return 0
        return num
    

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm. Get_rank ( )
for N in range(1000,10000,1000):
    start=time.time()
    if myrank == 0 :
        samples=numpy.arange(1,N)
        samples=numpy.resize(samples,(3,(N/3)))
    else :
        samples = None
    samples = comm.scatter(samples , root=0)


    sendPrime=[]
    for number in samples:
        sendPrime.append(computeprime(number))

    newdata=comm.gather(sendPrime , root=0)

    if myrank == 0 :
        #print (" pi i s approximately %.16f , error %.16f " % ( pi , error ) )
        #print "newdata",newdata
        end=time.time()
        print "time ",(end-start)
