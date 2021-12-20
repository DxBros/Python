>>> a = np.arange(1,5).reshape((2,2))
>>> b = np.arange(6,10).reshape((2,2))
>>> a,b
(array([[1, 2],
       [3, 4]]), array([[6, 7],
       [8, 9]]))
>>> np.vstack((a,b))
array([[1, 2],
       [3, 4],
       [6, 7],
       [8, 9]])
>>> np.hstack((a,b))
array([[1, 2, 6, 7],
       [3, 4, 8, 9]])
>>> np.column_stack((a,b))
array([[1, 2, 6, 7],
       [3, 4, 8, 9]])
>>> a = np.array([2.,4.])
>>> b = np.array([3.,5.])
>>> np.column_stack((a,b))
array([[2., 3.],
       [4., 5.]])
>>> c = np.column_stack((a,b))
>>> c
array([[2., 3.],
       [4., 5.]])
>>> del c
>>> a[:,np.newaxis]
array([[2.],
       [4.]])
>>> c = np.column_stack((a[:,np.newaxis],b[:,np.newaxis]))
>>> c
array([[2., 3.],
       [4., 5.]])
>>> ### column_stack == hstack and row_stack == vstack
>>> np.column_stack is np.hstack
False
>>> np.row_stack is np.vstack
True
>>> #hence row_stack acts as an alias for vstack
>>> # In complex cases ,r_ and c_ are useful for creating arrays by stacking numbers along one axis.They allow the use of range literals:
>>> np.r_[1:4,0,4]
array([1, 2, 3, 0, 4])
>>> # When used with arrays as arguments ,r_ and c_ are similar to vstack and hstack in their default behaviour , but allow for an optional argument giving the number of the axis along which to concatenate
>>> #Splitting one array into several smaller ones
>>> a = np.arange(1,25).reshape((2,12))
>>> a
array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
>>> np.hsplit(a,3)
[array([[ 1,  2,  3,  4],
       [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
       [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
       [21, 22, 23, 24]])]
>>> a = np.arange(12).reshape((3,4))
>>> b = a
>>> b is a
True
>>> # Python passes mutable objects as references ,so function calls make no copy.
>>> def f(x):
    print(id(x))
    
>>> id(a)
9541728
>>> f(a)
9541728
>>> #VIEW OR SHALLOW COPY
>>> c =a.view()
>>> c
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> c is a
False
>>> c.flags.owndata
False
>>> c = c.reshape((2,6))
>>> a.shape
(3, 4)
>>> c[0,4] = 1234
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
>>> s = a[:,1:3]
>>> s[:]= 10
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
>>> #DEEP COPY
>>> d = a.copy()
>>> d is a
False
>>> d.base is a
False
>>> d[0,0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
>>> a = np.arange(int(1e8))
>>> b = a[:100].copy()
>>> del a
>>> b
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>> # if b = a[:,100] is used instead ,a is referenced by b and will persist in memory even if del a is executed.
>>> # Indexing with array of indices
>>> a = np.array(12)**2
>>> i = np.array([1,1,3,8,5])
>>> a[i]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
IndexError: invalid index to scalar variable.
>>> a = np.arange(12)**2
>>> a[i]
array([ 1,  1,  9, 64, 25], dtype=int32)
>>> j = np.array([[3,4],[9,7]])
>>> a[j]
array([[ 9, 16],
       [81, 49]], dtype=int32)
>>> a = np.arange(12).reshape(3,4)
>>> i = np.array([[0,1],[1,2]])
>>> j = np.array([[2,1],[3,3]])
>>> a[i,j]
array([[ 2,  5],
       [ 7, 11]])
>>> a[i,2]
array([[ 2,  6],
       [ 6, 10]])
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> a[:,j]
array([[[ 2,  1],
        [ 3,  3]],

       [[ 6,  5],
        [ 7,  7]],

       [[10,  9],
        [11, 11]]])
>>> a[i,j] is a[(i,j)]
False
>>> a[i,j] == a[(i,j)]
array([[ True,  True],
       [ True,  True]])
>>> # Indexing with boolean
>>> a = np.arange(50).reshape(10,5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34],
       [35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44],
       [45, 46, 47, 48, 49]])
>>> a[a>30]
array([31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
       48, 49])
>>> a>30
array([[False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False, False, False, False, False],
       [False,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True],
       [ True,  True,  True,  True,  True]])
>>> 
