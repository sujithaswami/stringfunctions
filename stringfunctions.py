#Operator overloading
fname="sujitha"
lname="swami"
print(fname+ " " +lname)
#f string/ interpolation
s = "hello"
k = "world"
m = f"{s} {k}"
print(m)
#join method
s = "sujitha"
m = "swami"
l = (s, m)
print((" ").join (l))
#split
a = "sujitha@gmail.com"
print(a.split("@"))
s = "$123dji"
print(s.split("3"))
#splitlines
a : str = """ 1-1
near kesanupalli, 
dachepalli mandal,
palnadu .
"""
print(a.splitlines())
s : str = """
father : rama saidaiah,
mother : durga,
sister : madhuha, anusha
"""
print(s.splitlines())
#partition
s = "suji@gmail.com"
print(s.partition(".@"))
#
a= "5biryani$"
print(a.partition("5"))
#rpartition
s = "@suji@gmail.com"
print(s.rpartition("i"))



