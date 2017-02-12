import numpy as np
import matplotlib.pyplot as plt
import operator


Times=open("dummyData.txt",'r')
x = Times.read().split('\n')
x = list(map(int, x))
print x

Estimations=[]
for i in range(100):
	Estimations.append(1600)
print Estimations

y = map(operator.sub,Estimations,x)

print y

#definitionsfortheaxes
left,width=0.1,0.65
bottom,height=0.1,0.65
bottom_h=left_h=left+width+0.02

rect_scatter=[left,bottom,width,height]

#startwitharectangularFigure
plt.figure(1,figsize=(8,8))

axScatter=plt.axes(rect_scatter)
axScatter.set_title("UPSOn-TimeGraph")

#thescatterplot:
axScatter.scatter(x,y)

#nowdeterminenicelimitsbyhand:
binwidth=0.25
xymax=np.max([np.max(np.fabs(x)),np.max(np.fabs(y))])
lim=(int(xymax/binwidth)+1)*binwidth

axScatter.set_xlim((0,2359))
axScatter.set_ylim((-lim,lim))

axScatter.set_xlabel("EstimatedTime")
axScatter.set_ylabel("ActualTime")

bins=np.arange(-lim,lim+binwidth,binwidth)

plt.show()
