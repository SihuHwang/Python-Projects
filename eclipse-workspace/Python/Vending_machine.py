'''
Created on Nov 16, 2019

@author: sihuh
'''

def vend():

    a = {'item': 'choc', 'price': 1.5, 'stock': 2}
    b = {'item': 'pop', 'price': 1.75, 'stock': 1}
    c = {'item': 'chips', 'price': 2.0, 'stock': 3}
    d = {'item': 'gum', 'price': 0.50, 'stock': 1}
    e = {'item': 'mints', 'price': 0.75, 'stock': 3}
    items = [a, b, c, d, e]
    cim = 0 # cash in machine

    print('welcome to vending machine! \n***************')

    # show items, prices
    def show(items):
        print('\nitems available \n***************')

        for item in items:      
            if item.get('stock') == 0:
                items.remove(item)
        for item in items:
            print(item.get('item'), item.get('price'))

        print('***************\n')

    # have user choose item
    while True:
        show(items)
        selected = input('select item: ')
        for item in items:
            if selected == item.get('item'):
                selected = item               
                price = selected.get('price')
                while cim < price:
                    cim = float(input('insert ' + str(price - cim) + ': '))   
                else:
                    print('you got ' + selected.get('item'))
                    selected['stock'] -= 1
                    cim -= price
                    print('cash remaining: ' + str(cim))
                    a = input('buy something else? (y/n): ')
                    if a == 'n':
                        if cim != 0:
                            print(str(cim) + ' refunded')
                            cim = 0
                            print('thank you, have a nice day!\n')
                            break                        
                        else:
                            print('thank you, have a nice day!\n')
                            break                        
                    else:
                        continue
                    



vend()