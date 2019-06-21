def purchases():
    return [(i//2, 'item%s'%i) for i in xrange(1,10)]

def accounts():
    return [(i, 'bob%s@gmail.com'%i) for i in xrange(0,5)]

# def accounts():
#     for i in xrange(1,500):
#         yield (i, 'bob%s@gmail.com'%i) 
