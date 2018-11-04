import sys
import os

#sys.path.append(os.getcwd()+'/python/common')
#print("\n".join(sys.path))

#from test_module import test as tst
from ..common.test_module import test as tst


if __name__ == '__main__':
    print(tst.__name__)

    print(tst())

