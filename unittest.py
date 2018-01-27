mydict.py

class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
		
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r" 'Dict' object has no attribute '%s' "%key)
	
	def __setattr__(self,key,value):
		self[key]=value
    
    
    
    
mydict_test.py
    
    import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
           
运行测试文件的方法
1.在测试文件的末尾加上
if __name__ == '__main__':
    unittest.main()
2.在命令行运行
python -m unittest mydict_test
