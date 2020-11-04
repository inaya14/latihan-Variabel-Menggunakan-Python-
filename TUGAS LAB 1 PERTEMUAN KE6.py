Python 3.9.0b5 (tags/v3.9.0b5:8ad7d50, Jul 20 2020, 18:35:09) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("# penggunaan end")
# penggunaan end
>>> print('A', end='')
A
>>> print('B', end='')
B
>>> print('C', end='')
C
>>> print()

>>> print('X')
X
>>> print('Y')
Y
>>> print('Z')
Z
>>> print("# penggunaan separator")
# penggunaan separator
>>> print("w, x, y, z = 10, 15, 20, 25")
w, x, y, z = 10, 15, 20, 25
>>> print(w, x, y, z)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(w, x, y, z)
NameError: name 'w' is not defined
>>> print("w, x, y, z")
w, x, y, z
>>> print(w, x, y, z, sep=',')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(w, x, y, z, sep=',')
NameError: name 'w' is not defined
>>> print("w, x, y, z, sep=','")
w, x, y, z, sep=','
>>> print(w, x, y, z, sep='')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(w, x, y, z, sep='')
NameError: name 'w' is not defined
>>> print("w, x, y, z, sep=''")
w, x, y, z, sep=''
>>> print(w, x, y, z, sep=':')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(w, x, y, z, sep=':')
NameError: name 'w' is not defined
>>> print("w, x, y, z, sep=':'")
w, x, y, z, sep=':'
>>> print(w, x, y, z, sep='.....')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(w, x, y, z, sep='.....')
NameError: name 'w' is not defined
>>> print("w, x, y, z, sep='.....'")
w, x, y, z, sep='.....'
>>> print("# string format")
# string format
>>> print(0, 10**0)
0 1
>>> print(1, 10**1)
1 10
>>> print(2, 10**2)
2 100
>>> print(3, 10**3)
3 1000
>>> print(4, 10**4)
4 10000
>>> print(5, 10**5)
5 100000
>>> print(6, 10**6)
6 1000000
>>> print(7, 10**7)
7 10000000
>>> print(8, 10**8)
8 100000000
>>> print(9, 10**9)
9 1000000000
>>> print(10, 10**10)
10 10000000000
>>> print("# string format")
# string format
>>> print('{0:>3} {1:>16}'.format(0, 10**0))
  0                1
>>> print('{0:>3} {1:>16}'.format(1, 10**1))
  1               10
>>> print('{0:>3} {1:>16}'.format(2, 10**2))
  2              100
>>> print('{0:>3} {1:>16}'.format(3, 10**3))
  3             1000
>>> print('{0:>3} {1:>16}'.format(4, 10**4))
  4            10000
>>> print('{0:>3} {1:>16}'.format(5, 10**5))
  5           100000
>>> print('{0:>3} {1:>16}'.format(6, 10**6))
  6          1000000
>>> print('{0:>3} {1:>16}'.format(7, 10**7))
  7         10000000
>>> print('{0:>3} {1:>16}'.format(8, 10**8))
  8        100000000
>>> print('{0:>3} {1:>16}'.format(9, 10**9))
  9       1000000000
>>> print('{0:>3} {1:>16}'.format(10, 10**10))
 10      10000000000
>>> 