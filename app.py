print("Welcome to my first VS Code program!") # Welcome message
hours = input("How many hours did you exercise today? ") #Input
try: #Error handling
    hours = int(hours)
except ValueError:
    print("Please enter a valid number.")
    raise SystemExit
avg_calories_burnt = hours*300 #Calculation using an avg number of cal
print(f"You have burnt {avg_calories_burnt} calories on average today! Well done!")



