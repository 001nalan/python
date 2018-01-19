斐波拉契数列的演变
1.函数打印
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
print(fib(6))
2.普通函数变为generator
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)
		a,b=b,a+b
		n=n+1
for n in fib(6):
	print(n)
3.增加错误捕捉
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)
		a,b=b,a+b
		n=n+1

g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
4.拓展：杨辉三角
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
    L = [1,]
    while True:
        yield L
        L = [0,*L,0]
        L = [a+L[i+1] for i,a in enumerate(L[:-1])]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

