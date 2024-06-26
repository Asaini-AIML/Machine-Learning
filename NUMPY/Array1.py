import numpy as np
arr=np.array([1,2,3,4,5])
print('print array:',arr)
print('print version:',np.__version__)
print('print type of array:',type(arr))
arr2=np.array((1,2,3,4,5,6))
print('print tuple as array',arr2)
#0-D array
arr3=np.array(42)
print('0-D array:',arr3)
#1-D
arr4=np.array([1,2,3,4,5])
print('1-D:',arr4)
#2-D
arr5=np.array([[1,2,3,4],[6,7,8,4]])
print('2-D',arr5)
#3-D
arr6=np.array([[[1,2,3],[3,4,5],[4,6,7]]])
print('3-D',arr6)
#Dimension check
print('Dimension:',arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
print(arr6.ndim)
#higher D-array
arr7=np.array([1,2,3,4],ndmin=5)
print('higher D-array',arr7)
print(arr7.ndim)
#Indexing
arr8 = np.array([1, 2, 3, 4])
print('Indexing:',arr8[3])
print(arr8[1])
print('Indexing with sum',arr8[2]+arr8[3],arr8[1])
#2-D acessing
arr9 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2-D indexing:',arr9[0,1])
print(arr9[0,3],arr9[1,2])
#3-D acessing
arr10 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('3-D acessing',arr10[0,1,2])
print(arr10[1,1,0]+arr10[0,0,1])
#negative indexing
arr11 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr11[-2, -4])
#Array Slicing
arr12 = np.array([1, 2, 3, 4, 5, 6, 7])
print('slice:',arr12[1:5])
print('from index 4',arr12[4:])
print('from 0to 4 ',arr12[:4])
#negative slicing
print('3 from end to 1',arr12[-3:-1])
#using step slicing
print('step=2',arr[1:5:2])
print('every other array:',arr12[::2])
#slicing 2_D
arr13= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('from second to 1to4',arr13[1,1:4])
print('2 from both',arr13[0:2,2])
print('from both 1to 4',arr13[0:2,1:4])
#data type
'''i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )'''
arr14 = np.array([1, 2, 3, 4])
print(arr14.dtype)
arr15= np.array(['apple', 'banana', 'cherry'])
print(arr15.dtype)
#define datatype
arr16=np.array([1,2,3,4],dtype='S')
print(arr16)
print(arr16.dtype)
#with 4 byte integer
arr17=np.array([1,2,3,4],dtype='i4')
print(arr17)
print(arr17.dtype)
#error
# arr18= np.array(['a', '2', '3'], dtype='i')
# print(arr18)
#change datatype
arr19 = np.array([1.1, 2.1, 3.1])
newarr = arr19.astype('i')
print(newarr)
print(newarr.dtype)
#copying
arr20= np.array([1, 2, 3, 4, 5])
x = arr20.copy()
arr20[0] = 42
print(arr20)
print(x)
#viewing
arr21= np.array([1, 2, 3, 4, 5])
y= arr21.view()
arr21[0] = 42
y[1]=41
print(arr21)
print(y)
#check Array owns its data
arr22= np.array([1, 2, 3, 4, 5])
q= arr22.copy()
p = arr22.view()
print(arr22.base)
print(q.base)
print(p.base)
#SHAPE-----------
arr23 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr23.shape)
arr24 = np.array([1, 2, 3, 4], ndmin=5)
print(arr24)
print('shape of array :', arr24.shape)
#NumPy Array Reshaping--------
#1D-2D
arr25= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr25=arr25.reshape(4,3)
print(newarr25)
#1d-3d
newarr25_1= arr25.reshape(2, 3, 2)

print(newarr25_1)
#Returns Copy or View?
arr26= np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr26.reshape(2, 4).base)
#Unknown Dimension
arr27= np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr27 = arr27.reshape(2, 2, -1)
print(newarr27)
#Flattening the arrays
#Flattening array means converting a multidimensional array into a 1D array.
arr28= np.array([[1, 2, 3], [4, 5, 6]])
newarr28 = arr28.reshape(-1)
print(newarr28)
#NumPy Array Iterating----------------
#1-D
arr29 = np.array([1, 2, 3])
for x in arr29:
  print(x)
print("*")
#2-D
arr30 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
print("*")
#n-D
arr31 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr31:
  for y in x:
    print(y)
#3-D
arr32= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr32:
  print(x)
for x in arr32:
  for y in x:
    for z in y:
      print(z)
#Iterating Arrays Using nditer()
for x in np.nditer(arr32):
  print(x)
#Iterating Array With Different Data Types
for x in np.nditer(arr29, flags=['buffered'], op_dtypes=['S']):
  print(x)
#Iterating With Different Step Size
for x in np.nditer(arr30[:, ::2]):
  print(x)
#Enumerated Iteration Using ndenumerate()
arr33 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr33):
  print(idx, x)
arr34 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr34):
  print(idx, x)
#NumPy Joining Array---------
#1-D
arr35_0 = np.array([1, 2, 3])
arr35_1 = np.array([4, 5, 6])
arr35_r = np.concatenate((arr35_0, arr35_1))
print(arr35_r)
#2-D
arr36_0 = np.array([[1, 2], [3, 4]])
arr36_1= np.array([[5, 6], [7, 8]])
arr36_r= np.concatenate((arr36_0, arr36_1), axis=1)
print(arr36_r)
#Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
#Stacking Along Rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
#Stacking Along Columns
arr = np.vstack((arr1, arr2))
print(arr)
#Stacking Along Height (depth)
arr = np.dstack((arr1, arr2))
print(arr)
#NumPy Splitting Array----
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 6)
print(newarr)
#Splitting 2-D Arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 4)
print(newarr)
#2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
#NumPy Searching Arrays--------------
arr37 = np.array([1, 2, 3, 4, 5, 4, 4])
x11 = np.where(arr37 == 4)
print(x11)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)
#Search Sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
x = np.searchsorted(arr, 7, side='left')
print(x)
#Sorting Arrays------------------
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
#Filtering Arrays--------------
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)