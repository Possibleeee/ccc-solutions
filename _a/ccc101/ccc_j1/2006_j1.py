burgers = [461, 431, 420, 0]
sides = [100, 57, 70, 0]
drinks = [130, 160, 118, 0]
desserts = [167, 266, 75, 0]

categories = [burgers, sides, drinks, desserts]
calories = 0

for i in range(4):
    user_input = int(input()) - 1
    calories += categories[i][user_input]

print(f"Your total Calorie count is {calories}.")