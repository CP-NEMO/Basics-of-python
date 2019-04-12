from sklearn import tree
# x= [height,weight,shoe size]
x=[[150,50,32],[120,67,55],[110,81,44],[190,99,66],[121,100,80]]
y=['male','female','male','male','male']

clf=tree.DecisionTreeClassifire()
clf=clf.fit(x,y)
pre=clf.predict([[190,121,42]])
print(pre)