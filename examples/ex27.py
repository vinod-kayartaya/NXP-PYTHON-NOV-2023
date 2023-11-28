"""
Example of a complex `dict`
"""
import json


def main():
    c1 = dict(code=123, firstname='Ramesh', lastname='Iyer')
    c1['phones'] = ['9001289012']
    c1['address'] = {'city': 'Chennai', 'state': 'Tamilnadu'}
    c1['is_married'] = True
    print(c1)
    print(json.dumps(c1, indent=4))

    print(f'{c1["firstname"]} {c1["lastname"]} lives in {c1["address"]["city"]}')
    print(f'{c1.get("firstname")} {c1.get("lastname")} lives in {c1.get("address").get("city")}')

    c1["phones"].append('9282711821')
    print(c1)
    c1['address']['country'] = 'India'
    print(c1)


if __name__ == '__main__':
    main()
