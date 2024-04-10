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
