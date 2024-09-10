import food_search as fs

food_name = str(input("Enter food name: "))

found = fs.search_food_by_name(food_name)
if found:
    nutritional_info = fs.get_nutritional_info(food_name)
    print(nutritional_info)