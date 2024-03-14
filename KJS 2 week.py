Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1번문제
>>> print("100")
100
>>> print(100)
100
>>> print(50+50)
100
>>> print("50+50")
50+50
>>> 
>>> #2번 문제
>>> print('%d / %d = %d' % (5, 10, 5/10))
5 / 10 = 0
>>> 
>>> #3번 문제
>>> print ("%04d" % 876)
0876
>>> print ("%5s" % "CookBook")
CookBook
>>> print ("%1.1f" % 123.45)
123.5
>>> 
>>> #4번 문제
>>> print("{2:d} {0:d} {1:d}".format(111, 222, 333))
333 111 222
>>> 
>>> #11번 문제
>>> print(int('1011',2))
11
>>> s="1A"
>>> print(int(s,16))
26
>>> 
>>> #13번 문제
>>> int('1002',2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int('1002',2)
ValueError: invalid literal for int() with base 2: '1002'
>>> ## 2진수는 0과 1로만 구성되어짐
>>> 
>>> int('1008',8)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int('1008',8)
ValueError: invalid literal for int() with base 8: '1008'
>>> ## 8진주세는 8을 포함하지 않음
>>> int('AAFG',16)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int('AAFG',16)
ValueError: invalid literal for int() with base 16: 'AAFG'
>>> ##16진수는 0에서 9까지, A에서 F까지 구성되어져 있다. 그래서 G를 포함하고 있기 때문에 오류 발생
>>> 
