import difflib
import json
t = open('trendyol.json',encoding='utf8')
g = open('getir.json',encoding='utf8')
getir = json.load(g)
trendyol = json.load(t)
def match_products(arr1, arr2):
    matches = []
    for product1 in arr1:
        name1 = product1["title"]
        price1 = product1["price"]
        for product2 in arr2:
            name2 = product2["title"]
            price2 = product2["price"]
            similarity = difflib.SequenceMatcher(None, name1, name2).ratio()
            if similarity > 0.5:
                price_diff = abs(int(price1) - int(float(price2)))
                matches.append({"name1": name1, "price1": price1, "name2": name2, "price2": price2, "price_diff": price_diff, "similarity": similarity})
        print(matches) 

match_products(getir,trendyol)

