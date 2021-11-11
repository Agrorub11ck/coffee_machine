def count_coffe(water1, cofe1, milk1, price1):
    ingridients['water'] -= water1
    ingridients['cofe'] -= cofe1
    ingridients['milk'] -= milk1
    ingridients['money'] += price1
    ingridients['cups'] -= 1


def true_cofe(water, cofe, milk, price):
    if ingridients['water'] - water >= 0 and ingridients['cofe'] - cofe >= 0 and ingridients['milk'] - milk >= 0 and ingridients['cups'] - 1 >= 0:
        print('I have enough resources, making you a coffee!')
        print()
        count_coffe(water, cofe, milk, price)
    else:
        if ingridients['water'] - water < 0:
            print('Sorry, not enough water!')
        elif ingridients['cofe'] - water < 0:
            print('Sorry, not enough cofe!')
        elif ingridients['milk'] - water < 0:
            print('Sorry, not enough milk!')
        elif ingridients['cups'] - 1 < 0:
            print('Sorry, not enough cups!')
    print()
    main()


def fill():
    print('Write how many ml of water you want to add:')
    ingridients['water'] += int(input())
    print('Write how many ml of milk you want to add:')
    ingridients['milk'] += int(input())
    print('Write how many grams of coffee beans you want to add:')
    ingridients['cofe'] += int(input())
    print('Write how many disposable coffee cups you want to add:')
    ingridients['cups'] += int(input())
    main()


def take():
    print('I gave you $' + str(ingridients['money']))
    ingridients['money'] = 0
    print()
    main()


def print_ingredient():
    print('The coffee machine has:')
    print(ingridients['water'], 'of water')
    print(ingridients['milk'], 'of milk')
    print(ingridients['cofe'], 'of coffe beans')
    print(ingridients['cups'], 'of disposable cups')
    print(ingridients['money'], 'of money')
    print()
    main()


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    coffe = input()
    if coffe == '1':
        true_cofe(250, 16, 0, 4)
    elif coffe == '2':
        true_cofe(350, 20, 75, 7)
    elif coffe == '3':
        true_cofe(200, 12, 100, 6)
    elif coffe == 'back':
        main()


def actions(stroke):
    print()
    if stroke == 'buy':
        buy()
    elif stroke == 'fill':
        fill()
    elif stroke == 'take':
        take()
    elif stroke == 'remaining':
        print_ingredient()

def main():
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'exit':
        return
    actions(action)


ingridients = {'water': 400, 'milk': 540, 'cofe': 120,
                'money': 550, 'cups': 9}



main()