def find_product(param):
    res = []
    for i in range(len(param)):
        prod = 1
        for j in range(len(param)):
            if j != i:
                prod *= lst[j]
        res.append(prod)
    return res


lst = [0, 2, 9, 0, 12, 25]
print(find_product(lst))
