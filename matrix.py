m=[[1,2,3],[4,5,6],[7,8,9]]
output=list(map(sum,m))
print output

#
print{i:sum(m[i]) for i in range(3)}

print {x:ord(x) for x in "abcdABCD"}
d={'food':'spam','quantity':4,'colour':2}
d['quantity']+=1
print d['quantity']
d[2]=22
d['23']=22
print d['food']