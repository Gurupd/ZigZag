'''s="PAYPALISHIRING"
num_of_rows=3
delta=-1
row=0
res=[[] for i in range((num_of_rows))]

for c in s:
    res[row].append(c)
    if row==0 or row==num_of_rows-1:
        delta*=-1
    row+=delta
for i in range(len(res)):
    res[i]=''.join(res[i])
print(''.join(res))'''

a=['1','3','5','6']
res='#'.join(a)
print(res)