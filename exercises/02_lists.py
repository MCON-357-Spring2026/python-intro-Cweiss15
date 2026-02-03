"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""

foods = ["meat", "potatoes", "sweet potatoes"]
print("First:",foods[0], "Last:", foods[-1])
foods.append("bagels")
foods.remove("potatoes")
for food in foods:
    print(food)
food_lengths = []
for food in foods:
    food_lengths.append(len(food))
print(food_lengths)