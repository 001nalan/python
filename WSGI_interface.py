#hello.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = bytes(map(ord, environ['PATH_INFO'][1:])).decode('utf-8')

    body = '<h1>Hello, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]
    
    
    
#server.py
#coding=utf-8
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from Item.hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
