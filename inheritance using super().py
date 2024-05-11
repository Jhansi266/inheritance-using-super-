class employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showdetails(self):
        print("role =", self.role)
        print("dep=",self.dep)
        print("salary=",self.salary)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        print("name=",self.name)
        self.age=age
        print("age=",self.age)
        super().__init__("finance","account","70000")
em1=engineer("yeswanth",23)
em1.showdetails()
