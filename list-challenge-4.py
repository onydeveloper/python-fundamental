def find_product(lst):
    res = []
    for item in lst:
        itemlst = [item]
        tmpset = set(lst) - set(itemlst)
        prod = 1
        for itemset in tmpset:
            prod *= itemset
        res.append(prod)
    return res

lst = [4,2,1,5,0]
print(find_product(lst))