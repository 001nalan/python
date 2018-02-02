import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#输出结果：
wget www.sina.com.cn...
wget www.sohu.com...
wget www.163.com...
www.sina.com.cn header > HTTP/1.1 200 OK
www.sina.com.cn header > Server: nginx
www.sina.com.cn header > Date: Fri, 02 Feb 2018 11:43:32 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Content-Length: 605189
www.sina.com.cn header > Connection: close
www.sina.com.cn header > Last-Modified: Fri, 02 Feb 2018 11:41:54 GMT
www.sina.com.cn header > Vary: Accept-Encoding
www.sina.com.cn header > Expires: Fri, 02 Feb 2018 11:44:19 GMT
www.sina.com.cn header > Cache-Control: max-age=60
www.sina.com.cn header > X-Powered-By: shci_v1.03
www.sina.com.cn header > Age: 13
www.sina.com.cn header > Via: http/1.1 ctc.nanjing.ha2ts4.118 (ApacheTrafficServer/6.2.1 [cHs f ])
www.sina.com.cn header > X-Cache: HIT.118
www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.nanjing.ha2ts4.59.nb.sinaedge.com,c=36.4.107.110;f=Edge,s=ctc.nanjing.ha2ts4.118,c=202.102.94.59
www.sina.com.cn header > X-Via-Edge: 15175718121606e6b04247c5e66ca08c389a0
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Fri, 02 Feb 2018 11:43:32 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.sohu.com header > HTTP/1.1 200 OK
www.sohu.com header > Content-Type: text/html;charset=UTF-8
www.sohu.com header > Connection: close
www.sohu.com header > Server: nginx
www.sohu.com header > Date: Fri, 02 Feb 2018 11:42:38 GMT
www.sohu.com header > Cache-Control: max-age=60
www.sohu.com header > X-From-Sohu: X-SRC-Cached
www.sohu.com header > Content-Encoding: gzip
www.sohu.com header > FSS-Cache: HIT from 9777038.17117080.11551742
www.sohu.com header > FSS-Proxy: Powered by 3944245.5451583.5718860


#总结：
多进程，多线程，一个进程可以进行协程操作
两个任务用到同一变量，想要同时进行时：
多线程的方法：用锁，释放锁，一个线程进行操作时，另一个线程停下等待
单一线程协程的方法：yield from 在几个任务之间跳转，保证线程不会停歇
