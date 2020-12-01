from matplotlib import pyplot as plt

plt.xkcd()  #funny shape

dev_x =[1,2,3,4,5,6,7]
dev_y =[10,24,30,47,50,69,70]
plt.plot(dev_x,dev_y,color='b',linestyle='--',marker='o',label= 'first')

dev_y2 =[12,25,38,40,56,69,75]
plt.plot(dev_x,dev_y2,color='k',linestyle='-',marker='.',label= 'second')

dev_y3 =[0,8,10,15,20,60,75]
plt.plot(dev_x,dev_y3,color='#377777',linewidth= 3,label= 'second')

plt.title('numbers')
plt.xlabel('mono numbers')
plt.ylabel('tens numbers')
plt.legend()
plt.grid()

plt.savefig('first.png')

plt.show()