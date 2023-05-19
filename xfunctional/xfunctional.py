from functional import pipeline, seq
from functools import wraps

@pipeline.extend
def expand_with_key(it):
    if type(it) is not seq:
        it = seq(it)
    return it.flat_map(lambda x: seq(x[1]).map(lambda y: (x[0], y)))

@pipeline.extend
def flip(it):
    if type(it) is not seq:
        it = seq(it)
    return it.map(lambda x: seq(x).reverse())

def unpack(f):
    @wraps(f)
    def unpacked(args):
        return f(*args)
    return unpacked

