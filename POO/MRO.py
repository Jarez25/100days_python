class A:
    def hablar(self):
        print('hola desde la A')

class B(A):
    def hablar(self):
        print('hola desde B')

class C(A):
    def hablar(self):
        print('hola desde C')

class D(B, C):
    def hablar(self):
        print('hola desde D')

d = D()

d.hablar()