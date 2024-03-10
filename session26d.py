def upgrade_to_meal(func):

    def inner(amount, taxes,meal_plan):
        if meal_plan == 1:
            print("Upgrading to Medium Meal...")
            print("+ Added Coke...")
            print("+ Added fries...")
            amount += 100
            taxes = 0.10
        elif meal_plan == 2:
            print("Upgrading to Large meal...")
            print("+ Added Large Coke...")
            print("+ Added Large fries...")
            print("+ Added Ice cream...")
            amount += 200
            taxes = 0.20
        else:
            print("Thank you for your purchase")

        return func(amount, taxes,meal_plan)

    return inner

@upgrade_to_meal
def buy_burger(amount, taxes, meal_plan=0):
    return amount + (amount*taxes)

amount_to_pay = buy_burger(100, 0.19,0)
print("Mcdonalds Final charge:",amount_to_pay)