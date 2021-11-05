
price = [57.8, 46.51, 97.9, 48.7, 78.9, 69.8, 10.7, 11.9, 99.8, 33.6]
for idx in range(len(price)):
    price[idx] = str(price[idx])
    price[idx] = price[idx].split('.')
    price[idx] = f'{int(price[idx][0]):.0f} руб {int(price[idx][1]):02d} коп'

price = ', '.join(price)
print(price)

price = price.split(', ')
my_price = sorted(price, reverse=True)
my_price = ', '.join(my_price)
print(my_price)


my_prices1 = sorted(price)
print(my_prices1)


my_price = my_price.split(', ')
my_price = my_price[:4]
my_price = ', '.join(my_price)
print(my_price)

