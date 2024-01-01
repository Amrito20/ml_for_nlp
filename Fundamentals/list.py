price = [20, 30, 40, 50]

discount_price = [i - (i*15)/100 if i>30 else i-(i*10)/100 for i in price]

print (discount_price)


list_2d = [['a', 'b', 'c'], ['d','e','f'], ['g', 'h', 'i']]

#print(list_2d[2][2])

for row in range(len(list_2d)):
    for col in range(len(list_2d[row])):
        print (row,col,list_2d[row][col])

for row in list_2d:
    print (row)
    for col in row:
        print(col)