#multiple inheritance(two base one child)
'''
class father:
    def fdisplay(self):
        print("This is father class")
class mother:
    def mdisplay(self):
        print("This is mother class")
class child(father,mother):
    def cdisplay(self):
        print("This is child class")
obj=child()
obj.fdisplay()
obj.mdisplay()
obj.cdisplay()
'''

#hierarchial inheritance(one base multiple child)
'''
class parent:
    def pdisplay(self):
        print("This is parent class")
class child1(parent):
    def c1display(self):
        print("This is first child class")
class child2(parent):
    def c2display(self):
        print("This is second child class")        

obj1=child1()
obj1.pdisplay()
obj1.c1display()
obj2=child2()
obj2.pdisplay()
obj2.c2display()
'''
