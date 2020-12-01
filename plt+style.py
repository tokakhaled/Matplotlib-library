from matplotlib import pyplot as plt
print(plt.style.available)
plt.style.use('seaborn-whitegrid')


dev_x =[1,2,3,4,5,6,7]
dev_y =[10,24,30,47,50,69,70]
plt.plot(dev_x,dev_y,label= 'first')

dev_y2 =[12,25,38,40,56,69,75]
plt.plot(dev_x,dev_y2,linestyle='-',label= 'second')

dev_y3 =[0,8,10,15,20,60,75]
plt.plot(dev_x,dev_y3,label= 'second')

plt.title('numbers')
plt.xlabel('mono numbers')
plt.ylabel('tens numbers')
plt.legend() #arrenge the line
plt.show()
