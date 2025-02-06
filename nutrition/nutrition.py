n=input("Item:").lower()
frdic=[{'fruit':"apple","calorie":"130"},{'fruit':"avocado","calorie":"50"},
       {'fruit':"banana","calorie":"110"},{'fruit':"cantaloupe","calorie":"50"},
       {'fruit':"grapefruit","calorie":"60"}, {'fruit':"grape","calorie":"90"},{'fruit':"honeydew melon","calorie":"50"},
       {'fruit':"kiwifruit","calorie":"90"},{'fruit':"lemon","calorie":"15"},{'fruit':"lime","calorie":"20"},
       {'fruit':"nectarine","calorie":"60"},{'fruit':"orange","calorie":"80"},
       {'fruit':"peach","calorie":"60"},{'fruit':"pear","calorie":"100"},
       {'fruit':"pineapple","calorie":"50"}, {'fruit':"plum","calorie":"70"},{'fruit':"strawberries","calorie":"50"},
       {'fruit':"sweet cherries","calorie":"100"},{'fruit':"tangerine","calorie":"50"},{'fruit':"watermelon","calorie":"80"}]


cal = None

for item in frdic:
    if item['fruit'] == n:
        cal = item['calorie']
        break

if cal is not None:
    print("Calorie:", cal)
else:
    print("")
