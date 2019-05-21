from mpi4py import MPI
import numpy
import time

def computeprime (num) :
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return 0
            else:
                return num
        
start=time.time()
end=start
comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm. Get_rank ( )
if myrank == 0 :
    samples=numpy.empty(3)
    filler=numpy.arange(0,3,1)
    ind=numpy.arange(len(samples))
    numpy.put(samples,ind,filler)
else :
    samples = None
samples = comm.scatter( samples , root=0)

for number in samples:
    sendPrime = computeprime(number)

newdata=comm.gather(mypi , root=0)

if myrank == 0 :
    #print (" pi i s approximately %.16f , error %.16f " % ( pi , error ) )
    print "newdata",newdata
    end=time.time()
print "time ",(end-start)