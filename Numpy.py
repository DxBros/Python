>>> a = np.array([[1,1],[0,1]])
>>> b = np.array([[2,0],[3,4]])
>>> a*b
array([[2, 0],
       [0, 4]])
>>> a@b
array([[5, 4],
       [3, 4]])
>>> a.dot(b)
array([[5, 4],
       [3, 4]])
>>> a == b
array([[False, False],
       [False, False]])
>>> a<=b
array([[ True, False],
       [ True,  True]])
>>> a>=b
array([[False,  True],
       [False, False]])
>>> a += b
>>> a
array([[3, 1],
       [3, 5]])
>>> a>= b
array([[ True,  True],
       [ True,  True]])
>>> rg = np.random.default_rng(1)
>>> a = np.ones((2,3),dtype = int)
>>> b = rg.random((2,3))
>>> a *=3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b
array([[0.51182162, 0.9504637 , 0.14415961],
       [0.94864945, 0.31183145, 0.42332645]])
>>> b
array([[0.51182162, 0.9504637 , 0.14415961],
       [0.94864945, 0.31183145, 0.42332645]])
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> a = np.ones(3,dtype = np.int32)
>>> b - np.linspace(0,pi,3)
array([[ 0.51182162, -0.62033263, -2.99743304],
       [ 0.94864945, -1.25896487, -2.7182662 ]])
>>> b = np.linspace(0,pi,3)
>>> b
array([0.        , 1.57079633, 3.14159265])
>>> b.dtype.name
'float64'
>>> c = a+b
>>> c
array([1.        , 2.57079633, 4.14159265])
>>> c.dtype.name
'float64'
>>> d=np.exp(c*1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
>>> d+=1
>>> d
array([1.54030231+0.84147098j, 0.15852902+0.54030231j,
       0.45969769-0.84147098j])
>>> d+=j
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'j' is not defined
>>> d+=1j
>>> d
array([1.54030231+1.84147098j, 0.15852902+1.54030231j,
       0.45969769+0.15852902j])
>>> a = rg.random((2,3))
>>> a
array([[0.82770259, 0.40919914, 0.54959369],
       [0.02755911, 0.75351311, 0.53814331]])
>>> a.sum()
3.1057109529998157
>>> a.min()
0.027559113243068367
>>> a.max()
0.8277025938204418
>>> b = np.arange(13).reshape(3,4)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: cannot reshape array of size 13 into shape (3,4)
>>> b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> b.sum(axis =0)
array([12, 15, 18, 21])
>>> b.sum(axis =1)
array([ 6, 22, 38])
>>> b.min(axis =1)
array([0, 4, 8])
>>> b.cumsum(axis=1)
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]], dtype=int32)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> np.invert(b)
array([[ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12]], dtype=int32)
>>> np.all(b)
False
>>> np.any(b)
True
>>> np.argsort(b)
array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [0, 1, 2, 3]], dtype=int32)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> np.corrcoef(b)
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
>>> 
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729], dtype=int32)
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64], dtype=int32)
>>> a[:6:2]
array([ 0,  8, 64], dtype=int32)
>>> a[:6:2] = 1000
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729],
      dtype=int32)
>>> a[::-1]
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000],
      dtype=int32)
>>> for i in a:
    print(i**3)

1000000000
1
1000000000
19683
1000000000
1953125
10077696
40353607
134217728
387420489
>>> def f(x,y):
    return 10*x+y

>>> b = np.fromfunction(f,(5,4),dtype =int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[0:5,3]
array([ 3, 13, 23, 33, 43])
>>> b[-1]
array([40, 41, 42, 43])
>>> b[:-1]
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33]])
>>> b[,-1]
  File "<pyshell>", line 1
    b[,-1]
      ^
SyntaxError: invalid syntax
>>> b[3,-1]
33
>>> c= np.array([[[0,1,2],[10,12,13]],[[100,101,102],[110,112,113]]])
>>> c
array([[[  0,   1,   2],
        [ 10,  12,  13]],

       [[100, 101, 102],
        [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
>>> c[...,2]
array([[  2,  13],
       [102, 113]])
>>> #It is same as c[:,:,2]
>>> c[1,...]
array([[100, 101, 102],
       [110, 112, 113]])
>>> for row in b:
    print(row)

[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
>>> 
>>> for element in b.flat:
    print(element)

0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
>>> ###########SHAPE MANIPULATION
>>> a = np.floor(10*rg.random((3,4)))
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.shape
(3, 4)
>>> a.ravel()
array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
>>> a.T
array([[3., 1., 7.],
       [7., 4., 2.],
       [3., 2., 4.],
       [4., 2., 9.]])
>>> a.reshape(6,2)
array([[3., 7.],
       [3., 4.],
       [1., 4.],
       [2., 2.],
       [7., 2.],
       [4., 9.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
>>> a.reshape((12,-1))
array([[3.],
       [7.],
       [3.],
       [4.],
       [1.],
       [4.],
       [2.],
       [2.],
       [7.],
       [2.],
       [4.],
       [9.]])
>>> 
