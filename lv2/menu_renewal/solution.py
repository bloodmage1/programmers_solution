orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]

orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2,3,5]

orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2,3,4]


from collections import Counter
from itertools import combinations
from math import comb


answer = []

for num in course1:
    array = []
    for order in orders1:
        order = sorted(order)
       
        array.extend(list(combinations(order, num)))
    count = Counter(array)
    
    if count:
        print(max(count.values()))
        if max(count.values()) >= 2:
            for k, v in count.items():
                if v == max(count.values()):
                    answer.append("".join(k))

print(answer)

# str_answer = ""

# for i in orders1:
#     str_answer += i
    
# a = Counter(str_answer)

# result = []

# for i in course1:
#     result1 = ""
#     for k,v in a.items():
#         if v >= i:
#             result1 += k
    
#     result.append(result1)

# print(result)
