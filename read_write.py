fpath = r'C:\Windows\system.ini'
fpath1 = r'E:\代码测试\test.txt'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)
with open(fpath1, 'w') as f:
    f.write(s)
    
    
  r的用法使得路径不需要理会格式的问题
  
