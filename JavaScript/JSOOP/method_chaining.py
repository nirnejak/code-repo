class MyClass(object):
    def method1(self):
        print('hi there')
        return self
    def method2(self):
        print("hello There")
        return self

obj = MyClass()
obj.method1().method2()