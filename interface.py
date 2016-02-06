from branch_and_bound import *
from dynamic import Pack
import json
alogirthms = ['branch_and_bound', 'dynamic']


def start(items):
    while True:
        print("Hello there!")
        alg = input('Choose alogirthm: ')
        if alg not in alogirthms:
            print('Try another one')
            continue
        if alg == 'b_and_b':
            print(execute(items))
        if alg == 'dynamic':
            bag = Pack(items)
            print(bag.get_stored_items())
        print('Bye!')
        break


def main():
    items = []
    with open("items.json", 'r') as f:
        data = json.load(f)
        for x in data["items"]:
            asd = (Item(x['name'], x['value'], x['weight']))
            items.append(asd)
    start(items)

if __name__ == '__main__':
    main()
