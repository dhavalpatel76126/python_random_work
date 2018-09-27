dict1=dict(name='bob',ss='',aa='')
print dict1
print dict1['ss']
if not 'name1' in dict1:
    print "missing"
s=dict(sa=1,b=2,c=3,qc=4)
print list(s.keys())
print sorted(list(s.keys()))
for key in sorted(s):
    print key,'=>',s[key]