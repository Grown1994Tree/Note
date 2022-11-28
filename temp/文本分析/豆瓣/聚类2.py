from collections import Counter

# 获取每个cluster的数量
c = Counter(clusters)
print(c.items())

>>>dict_items([(4, 323), (3, 102), (5, 370), (7, 227), (8, 190), (2, 238), (0, 1214), (6, 107), (1, 18), (9, 34)])
