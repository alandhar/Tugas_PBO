def list_sum (lst):
    S = 0
    for elem in lst:
          S += elem
    return S
print (list_sum ( [5, 4, 3]))

def list_sum (lst):
    S = 0
    for elem in lst:
        S += elem
    return S
print(list_sum(5))

def strange_list_fun (n) :
    strange_list = []
    for i in range (0, n) :
         strange_list.insert (0, i)
    return strange_list
print(strange_list_fun(5))