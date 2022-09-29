#!/usr/bin/env python
# coding: utf-8

# In[11]:


a=1
print(id(a))
a=2
print(id(a))


# In[2]:


str1='Python is a programming language.'


# 

# In[12]:


print(str1)


# In[4]:


print(str1[0])


# In[13]:


print


# In[6]:


print(str1[2:10])


# In[14]:


print(str1[]6:18)


# In[15]:


print(str1[6:18])


# In[16]:


print(str1[12:23])


# In[17]:


str1.split()


# In[18]:


str1="{0} {1} {2}".format("I","am","good")
str1


# In[ ]:


str1


# In[19]:


str1="{1} {0} {2}".format("I","am","good")
str1


# In[ ]:


print("\Print string in order of keywords:")
print(str1)


# In[21]:


str1.capitalize()


# In[22]:


L=[1,2,3,"abes",12.5]


# In[ ]:


L


# In[23]:


L[3][2]


# # List
# 

# In[24]:


ks=[1,2,3]
ks+ks


# In[25]:


ls=[7,8,9]
ks+ls


# In[26]:


ks*5


# In[ ]:


L


# In[27]:


L[0]=10


# In[ ]:


L


# In[28]:


print(id(L))


# In[29]:


L[0]=10


# In[ ]:


L


# In[30]:


L2="Sana"
print(id(L2))


# In[31]:


L2[0]="G"


# In[32]:


L2="G"+L2[1:]


# In[ ]:


L2


# In[33]:


id(L2)


# In[34]:


a=input("Enter your age")


# In[ ]:





# In[35]:


a=input("Enter your age")
print(a*2)


# In[36]:


type(a)


# In[37]:


a*2


# In[38]:


a=input("Enter sequence")


# In[ ]:


type(a)



a


# In[39]:


a.split( )


# In[40]:


tuple1 = ('abcd',786,2.23,'john',70.2)
tuple2 =(123,'john')
print(tuple1)


# In[41]:


tuple1[0]="HI"


# In[42]:


tuple1 * 4


# In[43]:


dict1 ={}
type(dict1)


# In[44]:


dict1['one'] = "This is python"
dict1[2] = "This is Java"


# In[45]:


dict1[2]


# In[46]:


dict1[3]


# In[47]:


dict2={'name': 'sana','id': 1234,'dept':'cse'}


# In[49]:


type(dict2)


# In[ ]:


dict2


# In[50]:


dict2['name']


# In[51]:


print(dict2.keys)


# In[52]:


dict2.keys()


# In[ ]:


dict2.values()


# In[53]:


count=0
while(count<10):
    print(count)
    count=count+1


# In[54]:


count=0
while(count<5):
    print(count,"is less than 5")
    count=count+1
else:
        print(count,"is greater than 5")


# In[55]:


a=[1,23,45,6]
for i in a:
    print(i)
    
    
    


# In[56]:


a=input("Enter your name")


# In[ ]:


a


# In[57]:


total=0
for i in a:
    print(i)
    total=total+1
print("count", total)


# # Numpy
# 

# In[58]:


a=[2,3]
a*2


# In[59]:


import numpy


# In[60]:


import numpy as np


# In[61]:


get_ipython().system('pip install numpy')


# In[65]:


a_n=np.array(a)


# In[67]:


a_n


# In[68]:


a_n*2


# In[69]:


marks=[23,22,34,75,85,46,98,70,28,57]
marks=np.array(marks)
np.mean(marks)


# # unit 2 Numpy statistical functions
# 

# In[ ]:


np.amin(marks) #it indicates the lowest data in the list


# In[ ]:


np.amax(marks) #it indicates the largest data in the list


# In[ ]:


np.median(marks)


# In[ ]:


np.ptp(marks)#peakl to peak range of values along axis


# In[ ]:


np.std(marks)#standard deviation


# In[ ]:


np.var(marks)#variance


# In[71]:


x=[34 ,45 ,67 ,78]
x_n=np.array(x)
print(np.std(x_n))


# In[72]:


ss=np.mean((x_n-np.mean(x_n))**2)#variance
ss


# In[10]:


np.sqrt(ss)


# In[73]:


from numpy import random


# In[74]:


random.rand()


# In[77]:


random.seed(12)
for i in range(10):
    print(random.rand())
    


# In[ ]:


for i in range(10):
    x=2.75
    x=1+(1-3.5)*x
x


# In[75]:


x=2.75 #seed
for i in range(10):
    x=1+(1-3.5)*x
    print(x)


# In[79]:


random.seed(12)
for i in range 
print(random.rand())


# In[82]:


a=[ [3,4] , [5,6] ]
a


# In[86]:


a[1][1]


# In[87]:


import numpy as np


# In[88]:


a_n=np.array(a)


# In[89]:


a_n


# In[91]:


a_n[0,:]


# In[92]:


a_n[1,:]


# In[93]:


a_n.dtype #strides= the no of space required by the matrix cell's


# In[94]:


a_n.strides


# In[95]:


a_n


# In[96]:


a_n+1


# In[97]:


a_n.shape


# In[98]:


b_n=np.array([1])


# In[99]:


b_n


# In[100]:


b_n.shape


# In[101]:


import numpy as np


# In[102]:


a=np.loadtxt("https://raw.githubusercontent.com/goradbj/MachineLearning/main/cric.tsv",skiprows=1)


# In[103]:


a


# In[104]:


sachin_runs=a[:,1]


# In[105]:


sachin_runs


# In[106]:


np.mean(sachin_runs)


# In[112]:


dravid_runs=a[:,2]


# In[113]:


dravid_runs


# In[114]:


np.mean(dravid_runs)


# In[115]:


india_runs=a[:,3]


# In[116]:


india_runs


# In[117]:


np.mean(india_runs)


# In[121]:


np.corrcoef(india_runs,sachin_runs)


# In[119]:


np.corrcoef(dravid_runs,india_runs)


# In[120]:


np.corrcoef(sachin_runs,dravid_runs)


# # unit 3-  Data Visualization
# 

# In[130]:


import matplotlib.pyplot as plt #import matplotlib
import numpy as np #import numpy


# In[128]:


x=[1,2,3]  #x-axis
y=[3,4,5] #y-axis
plt.plot(x,y) #call plot function
plt.show() #call show function


# # Plotting graphs

# In[129]:


plt.plot(y)
plt.show()


# In[131]:


import numpy as np


# In[132]:


x=[1,3,7,9]
y=[24,15,78,23]
plt.plot(x,y)
plt.show()


# In[134]:


plt.plot(y)
plt.show()


# In[135]:


plt.plot(x)
plt.show()


# In[164]:


plt.plot(x,y,marker="o",color="r",linestyle="dashed")
plt.show()


# In[165]:


#10matches
india_runs=[920,450,670,800,500,420,389,345,678,120]
pak_runs=[500,345,789,234,875,345,678,780,120,150]
india_runs=np.array(india_runs)
pak_runs=np.array(pak_runs)


# In[166]:


india_runs.size


# In[167]:


pak_runs.size


# In[172]:


matches=np.arange(10)
matches


# # Lineplot
# 

# In[173]:


plt.plot(matches,india_runs)
plt.plot(matches,pak_runs)
plt.show()


# # Barplot

# In[182]:


#Netflix
generics=["Horror","Drama","Comedy","SciFi","Thriller","Suspense"] #categorical list
movies=[156,134,178,230,224,145] #numerical list
plt.bar(generics,movies,color="c")
plt.show()


# # Scatter plot

# In[177]:


x=[1,3,7,9]
y=[24,15,78,23]
plt.scatter(x,y,marker="s",color="r")
plt.show()


# In[179]:


plt.plot(x,y)
plt.xlabel("Prep time")
plt.ylabel("Exam marks")
plt.title("Student condition")
plt.show()


# # Legend

# In[183]:


#a legend helps to determine the plot; which plot is representing what?


# In[193]:


plt.plot(matches,india_runs)
plt.plot(matches,pak_runs)
plt.legend(["India","Pak"], loc="lower left")
plt.show()


# # Histogram

# In[197]:


from numpy import random


# In[208]:


a=random.randint(1,7,size=(20000000,))


# In[209]:


a


# In[210]:


plt.hist(a)
plt.show()


# # sin graph
# 

# In[215]:


theta1=np.arange(360)
theta1_r=np.deg2rad(theta1)
sintheta=np.sin(theta1_r)
plt.plot(theta1,sintheta)
plt.xlabel("Radians")
plt.ylabel("Degrees")
plt.show


# # cos graph

# In[220]:


theta1=np.arange(360)
theta1_r=np.deg2rad(theta1)
costheta=np.cos(theta1_r)
plt.plot(theta1,costheta)
plt.xlabel("Radians")
plt.ylabel("Degrees")
plt.show()


# # sin-cos graph

# In[241]:


theta1=np.arange(360)
theta1_r=np.deg2rad(theta1)
sintheta=np.sin(theta1_r)
costheta=np.cos(theta1_r)
plt.figure(figsize=(10,10))
plt.plot(theta1,sintheta,linestyle="dotted")
plt.plot(theta1,costheta)
plt.xlabel("Radians",)
plt.ylabel("Degrees")
plt.legend(["sin","cos"], loc="lower left")
plt.annotate("Maxima",xy=(90,1))
plt.savefig("myplot.pdf")

plt.show


# In[ ]:




