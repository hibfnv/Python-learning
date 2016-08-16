#!/usr/bin/env python
nested=[[1,2],[3],[4],[5,6,7],[8,9],[0]]
def rollnum(nested):
        for i in nested:
            for k in i:
                print k
print '\033[34m=\033[0m' * 30
rollnum(nested)
print '\033[34m=\033[0m' * 30
