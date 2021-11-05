item = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
item.insert(1, '"')
item.insert(3, '"')
item.insert(5, '"')
item.insert(7, '"')
item.insert(12, '"')
item.insert(14, '"')
item[2] = '05'
item[13] = '+05'
print(item)
print(" ".join(item))
