问题;在一个既有字符串又有整数和非字符的list中，使用lower()生成一个新的list
解题思路：先生成一个字符串的list,再使用lower()方法

L1=['Hello','World',18,'Apple',None]
L2=[]
for s in L1:
	if isinstance(s,str)==True:
		L2.append(s)
L2=[q.lower()for q in L2]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
