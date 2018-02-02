def customer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[Customer] Consuminng %s...' %n)
        r='200 Ok'

def produce(c):
    c.send(None)
    n=0
    while  n<5:
        n=n+1
        print('[PRODUCER] Producing %s...' %n)
        r=c.send(n)
        print('[PODUCER] CUSTOMER return:%s' %r)
    c.close()

c=customer()
produce(c)



#输出结果
{PRODUCER] Producing 1...
[Customer] Consuminng 1...
[PODUCER] CUSTOMER return:200 Ok
[PRODUCER] Producing 2...
[Customer] Consuminng 2...
[PODUCER] CUSTOMER return:200 Ok
[PRODUCER] Producing 3...
[Customer] Consuminng 3...
[PODUCER] CUSTOMER return:200 Ok
[PRODUCER] Producing 4...
[Customer] Consuminng 4...
[PODUCER] CUSTOMER return:200 Ok
[PRODUCER] Producing 5...
[Customer] Consuminng 5...
[PODUCER] CUSTOMER return:200 Ok
