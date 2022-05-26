orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2,3,5]

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2,3,4]

dic = {}
str_orders = []
for i in orders1:
    for j in i:
        str_orders.append(j)
        dic[j]=0    
    globals()["count_{}".format(j)] = 0


print(str_orders)

for i in str_orders:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in course1:
    for k,v in dic.items():
        if v == i:
            print(i,":",k)

