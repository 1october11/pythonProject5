item = 'Привет, {}!'

workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй', 'директор аэлита']

for worker in workers:
    print(item.format(worker.split()[-1].title()))
