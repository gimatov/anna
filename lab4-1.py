string = input()
hash_table = [0]*256
for i in range(len(string)):
    # print(ord(string[i]))
    hash_table[ord(string[i])] += 1
# print(hash_table)

while True:
    symbol = input()
    print(hash_table[ord(symbol[0])])
