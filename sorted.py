l = [10, 20, 14]
ls = sorted(l)

print(l)
print(ls)

l = [10, -15, -2, 1]
ls = sorted(l,key=abs,reverse=True)
print(ls)

t = (10,12,5,1)
print(sorted(t))

s= {'gfg','courses','python'}
print(sorted(s))

st = 'gfg'
print(sorted(st))

d = {10:'gfg',15:'ide',5:'courses'}
print(sorted(d))

l = [(10,15),(1,8),(2,3)]
print(sorted(l))