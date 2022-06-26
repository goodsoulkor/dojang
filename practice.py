# keys = input().split()
# values = input().split()

# scores = {}

# for i in range(len(keys)):
#     scores[keys[i]] = int(values[i])

# print(scores)

keys = input().split()
valuse = map(int, input().split())

result = dict(zip(keys, valuse))
print(result)
