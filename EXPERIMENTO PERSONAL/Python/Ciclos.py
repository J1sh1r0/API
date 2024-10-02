adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in (adj, fruits):
#         print(x)

# for x in adj:
#         print(x,y)

for x, y in zip(adj, fruits):
    print(x, y)
