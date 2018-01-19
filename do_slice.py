题目：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
解题思想：如何最后一位为空格，切片除去最后一位s=s[:-1]
如果首位为空格，切片除去首位s=s[1:]




def trim(s):
    if s.isspace() or  not s:
        return ''
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
	
