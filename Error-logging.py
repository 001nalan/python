import logging
def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:',e)
		logging.exception(e)
	finally:
		print('finally')
		
main()

print('END')
