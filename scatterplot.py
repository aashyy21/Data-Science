import matplotlib.pyplot as plt
Roll_no=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Marks=[22,87,5,43,56,73,55,54,11,20,61,5,79,31,27]
plt.figure(figsize=(9,5))
plt.scatter(Roll_no,Marks,color='red',s=60,edgecolors='black',label='students')
plt.title("Student  marks vs Roll number")
plt.xlabel("Roll number")
plt.ylabel("Marks obtained")
plt.yticks(range(0,100,10))
plt.grid(True,linestyle='--',alpha=0.3)
plt.legend()
plt.show()