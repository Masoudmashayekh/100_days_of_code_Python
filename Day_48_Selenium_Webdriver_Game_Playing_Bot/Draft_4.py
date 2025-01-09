dic = {15: 'buyCursor', 100: 'buyGrandma', 500: 'buyFactory', 2000: 'buyMine', 7000: 'buyShipment',
       50000: 'buyAlchemy lab', 1000000: 'buyPortal', 123456789: 'buyTime machine'}

affordable_upgrades = {}
for cost, id in dic.items():
    if 20 > cost:
        affordable_upgrades[cost] = id
print(max(affordable_upgrades))
