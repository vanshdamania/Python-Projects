print("-" * 50)
print("\t Welcome to Damania's Pizza")
print("-" * 50)

SmallPizza = 15
MediumPizza = 20
LargePizza = 25
PepperoniSmallPizza = 2
PepperoniMLPizza = 3 
ExtraCheese = 1
Bill = 0

print("Small size pizza: $15")
print("Medium size pizza: $20")
print("Large size pizza: $25\n")

print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
print("Extra cheese for any size pizza: + $1\n")

Size = str(input("Enter the size of the pizza: ")).lower()
Pepperoni = str(input("You want to add pepperoni in your pizza: ")).lower()
Cheese = str(input("You want to add extra cheese in your pizza: ")).lower()


if Size == 's' or Size == 'small':
    Bill = SmallPizza
elif Size == 'm' or Size == 'medium':
    Bill = MediumPizza
elif Size == 'l' or Size == 'large':
    Bill = LargePizza

if Pepperoni == 'Y' or Pepperoni == 'y':
    if Size == 's' or Size == 'small':
        Bill += PepperoniSmallPizza
    else:
        Bill += PepperoniMLPizza

if Cheese == 'y' or Cheese == 'yes':
    Bill += ExtraCheese

print(f"Your final bill is: $ {Bill}")
