print("Welcome to my girst VS Code program!")
hours = input("How many hours did you exercise today? ")
hours = int(hours)
avg_calories_burnt = hours*300
print(f"You have burnt {avg_calories_burnt} calories on average today! Well done!")
try:
    hours = int(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

