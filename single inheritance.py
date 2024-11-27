#inheritance
#types of inheritance
'''
1.single inheritance
2.multi level inheritance
3.multiple inheritence
4.hiearchial inheritance
'''
#single inheritance
class parent:
    def display(self):
        print("I AM A PARENT CLASS")
class child(parent):
    def get(self):
        print("I AM A CHILD CLASS")

obj=child()
obj.display()
obj.get()


#multilevel inheitance
'''
class grandparent:
    def gdisplay(self):
        print("This is grandparent class")
class parent(grandparent):
    def pdisplay(self):
        print("This is parent class")
class child(parent):
    def cdisplay(self):
        print("This is child class")

obj=child()
obj.gdisplay()
obj.pdisplay()
obj.cdisplay()
'''


