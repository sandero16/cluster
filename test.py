from mpi4py import MPI
import numpy

def computepi (samples) :
    count=0
    for x , y in samples :
        print("working")
        if x**2 + y**2 <= 1 :
            count += 1
            pi = 4*float (count)/ len ( samples )
            return pi

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm. Get_rank ( )
if myrank == 0 :
    N = 10000 // nprocs
    samples = numpy.random.random((nprocs,N,2))
else :
    samples = None
    samples = comm.scatter( samples , root=0)
    
mypi = computepi(samples)/nprocs
pi = comm.reduce(mypi , root=0)

if myrank == 0 :
    error = abs (pi-numpy.pi )
    print (" pi i s approximately %.16 f , e r r o r i s %.16 f " % ( pi , error ) )