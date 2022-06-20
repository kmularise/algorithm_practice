a=['*']
a=['***', '*   *', '***']
L=[]
for i in a:
    L.append(i*3)
for i in a:
    L.append(i+' '*3*len(a)+i)
for i in a:
    L.append(i*3)
print(L)