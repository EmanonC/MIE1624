import numpy
from matplotlib import pylab

t=numpy.arange(0.0,0.1,0.00001)
w=1000
t1=0.02
td=numpy.arange(0.0,0.1,0.001)
ymin=[0 for _ in range(len(td))]
ymax=[0 for _ in range(len(td))]

for i in range(len(td)):
    t1=td[i]
    ans=[numpy.cos(w*ti)*numpy.cos(w*(ti+t1)) for ti in t]
    ymin[i]=min(ans)
    ymax[i]=max(ans)
yd=[ymax[_]-ymin[_] for _ in range(len(ymin))]
# pylab.plot(td,ymin)
# pylab.plot(td,ymax)
pylab.plot(td,yd)
pylab.show()