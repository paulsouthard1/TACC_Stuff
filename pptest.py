import pypar as pp 

ncpus = pp.size() 
rank = pp.rank() 
node = pp.get_processor_name() 

print 'I am rank %d of %d on node %s' % (rank, ncpus, node) 

if rank == 0: 
    msg = 'P0' 
    pp.send(msg,1) 
    msg = pp.receive(ncpus-1) 
    print 'Processor 0 received message "%s" from rank %d' % (msg, ncpus-1) 
else: 
    source = rank-1 
    destination = (rank+1) % ncpus 
    msg = pp.receive(source) 
    msg = msg + 'P' + str(rank) 
    pp.send(msg, destination) 

pp.finalize() 