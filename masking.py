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

# a=np.arange(25)
# a_2D=a.reshape(5,5)
# rows=[1,3,4]
# cols=[2,4,0]
# selected=a_2D[rows,cols]
# print("2D",a_2D)
# print("selectd part",selected)


# #sort
# a=np.array([[13,14],[11,15]])
# arr1=np.sort(a,axis=0)#sorting along row
# print("sorting along row",arr1)
# arr2=np.sort(a,axis=1)#sorting along col
# print("sorting along col",arr2)
# a=np.array([[21,14],[11,15]])
# arr3=np.sort(a,axis=None)#sorting along all element
# print("sorting along all element",arr3)



#original array
# arr=np.array([21,14,11,15])
# print("original array",arr)
# #get indices
# sort_indices=np.argsort(arr)
# print("sort indices",sort_indices)
# #use the indices to sort the array
# sorted_arr_from_indices=arr[sort_indices]
# print("sorted array from indices",sorted_arr_from_indices)
# #sorted in decending order
# sorted_arr_from_indices_desc=sorted_arr_from_indices[::-1]
# print("sorted array in decending order",sorted_arr_from_indices_desc)
# #ascending order
# sorted_arr_from_indices_asc=sorted_arr_from_indices
# print("sorted array in ascending order",sorted_arr_from_indices_asc)

# names=np.array(["alice","bob","charlie","david"])
# marks=np.array([80,20,80,60])
# #lexsort()
# #lexsort() is used to sort multiple arrays based on the values of one array
# #syntax: lexsort(keys,axis=-1)
# #keys: sequence of arrays to sort by
# #axis: axis along which to sort
# #returns: array of indices that would sort the array
# #sort by marks in ascending order and then by name in ascending order
# indice=np.lexsort((names,marks))
# print("sorted indices",indice)
# print("result")
# for i in indice:
#     print(names[i],marks[i])


#structured array in numpy

# #create a structured array
# dt=np.dtype([("name","S10"),("age","i4"),("height","f4")])
# #create a array with the defined data type
# data=np.array([("alice",25,165.5),("bob",30,170.0),("charlie",22,160.0)],dtype=dt)
# print(data)
# #accessing fields
# print(data["name"])
# print(data["age"])
# print(data["height"])

