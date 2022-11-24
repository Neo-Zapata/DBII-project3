from sequential_search import *
from main import *

cwd = os.getcwd() # current working directory

 

def test():
    smt = some_class()
    # smt.PROCESS_IMAGES()
    smt.RANGE_SEARCH("tom_hanks.jpeg", 0.5)
    print()
    smt.KNN_SEARCH("tom_hanks.jpeg", 10)
test()