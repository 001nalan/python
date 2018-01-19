1.首字母大写
def normalize(name):
  return name[:].Upper()+name[1:].lower
  
 L1=['sdad','dfsads','feeads']
 L2=list(map(normalize,L1))
 2.求队列的积
 def prod(L):
     return reduce(lambda x,y:x*y,L)
     
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
 
