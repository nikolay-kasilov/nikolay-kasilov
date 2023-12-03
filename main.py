'''
*
**
***
****
'''
def f(size):
    for i in range(1,size+1):
        print(i*"*")
f(4)
f(7)
f(6)
'''
5
*****
*   *
*   *
*   *
*****
'''
def f(size):
    if size <= 0:
        return
    if size == 1:
        print("#")
        return
    print((size  )*'#')
    for _ in range(size -2 ):
        print((size -2)* '#')* " "+ "*"
    print(size *'#')
print('_')
f(0)
f(1)
f(2)
f(4)

