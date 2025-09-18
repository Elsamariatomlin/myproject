import numpy as np
# array=np.array([10,23,45,67,89])
# mask=array>23
# array[mask]=0
# print(array)


# x=np.arange(1,6)
# print(x)
# arr = np.array([0,2,4])      # valid positions
# print("the element at y position is", x[arr])  


# #fancing indexing using python list
# array=np.random.randint(10,59,size=10)
# print(array)
# indices=[1,0,2]
# print("Accessing multiple element using pyhtn list",array[indices])


# array=np.random.randint(10,20,size=7)
# print(array)
# indices=[0,2]
# print("Accessing multiple element using pyhtn list",array[indices])

# x=np.arange(1,10)#convert 1d to aray in fi 
# indice=np.array([[5,3],[4,5]])
# new_2D_array=x[indice]
# print(new_2D_array)

# x=np.arange(12)
# x_2D=x.reshape(3,4)
# row_indices=[1,2]
# col_indices=[0,2]
# selected_indices=x_2D[row_indices,col_indices]
# print("2D",x_2D)
# print("selected elemnet",selected_indices)

a=np.arange(25)
a_2D=a.reshape(5,5)
rows=[1,3,4]
cols=[2,4,0]
selected=a_2D[rows,cols]
print("2D",a_2D)
print("selectd part",selected)