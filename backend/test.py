from sequential_search import *
from main import *

cwd = os.getcwd() # current working directory

 

def test():
    smt = some_class()
    # smt.PROCESS_RTREE()
    # smt.PROCESS_IMAGES()
    smt.RANGE_SEARCH("tom_hanks.jpeg", 0.5)
    print()
    smt.KNN_SEARCH("tom_hanks.jpeg", 10)
    print()
    smt.RANGE_SEARCH_RTREE("tom_hanks.jpeg", 1.21) # que radio usamos?
    print()
    smt.KNN_SEARCH_RTREE("tom_hanks.jpeg", 10)

test()