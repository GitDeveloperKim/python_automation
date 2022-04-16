class Calculator():
    def my_sum (self, a, b):
        return a+b
    def my_minus (self, a, b):
        return a-b
    def my_multiply (self, a,b):
        return a*b
    def my_divide (self, a,b):
        return a/b

if __name__ == '__main__':
    a = Calculator()
    print(a.my_sum(10,20))