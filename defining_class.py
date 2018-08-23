class emp:
  def __init__(self,name,age,salary):
      self.name=name
      self.age=age
      self.salary=salary

  def empprint(self):
      print("Name:",self.name,'\n',"Age:",self.age,'\n',"Salary: $",self.salary)

Tim=emp("Tim",50,500000)
RZ=emp('Rodrigo',51,250000)
Tim.empprint()


class histo:
    def __init__(self,n,i,lbl_x,lbl_y):
        self.n=n
        self.i=i
        self.lbl_x=lbl_x
        self.lbl_y=lbl_y

    def grp(self):
       import matplotlib.pyplot as plt, numpy as np
       plt.hist(np.random.randn(self.n), bins=self.i)
       plt.xlabel(self.lbl_x)
       plt.ylabel(self.lbl_y)
       plt.show()
    def print(self):
        print("N:",self.n,"Bins:",self.i)

h1=histo(30,6,"value","pctn")
h2=histo(100,8,"value","pctn")
h3=histo(1000,12,"value","pctn")
h4=histo(10000,12,"value","pctn")

h1.print()

h1.grp()
h2.grp()
h3.grp()
h4.grp()
