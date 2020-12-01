from matplotlib import pyplot as plt
import numpy as np
print(plt.style.available)
plt.style.use('seaborn-darkgrid')

width = .25
dev_x =[1,2,3,4,5,6,7]
indexes_x = np.arange(len(dev_x))

dev_y =[10,24,30,47,50,69,70]
plt.bar(indexes_x-width,dev_y,width= width,label= 'first')

dev_y2 =[12,25,38,40,56,69,75]
plt.bar(indexes_x,dev_y2,width= width ,label= 'second')

dev_y3 =[0,8,10,15,20,60,75]
plt.bar(indexes_x+width,dev_y3,width= width,label= 'second')


plt.xticks(ticks=indexes_x,labels=dev_x)
plt.title('numbers')
plt.xlabel('mono numbers')
plt.ylabel('tens numbers')
plt.legend() #arrenge the line
plt.show()
