#Shopping cart in oops
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.menu = {
            "dal": MenuItem("dal", 300),
            "parantha": MenuItem("parantha", 40),
            "noodles": MenuItem("noodles", 250),
            "burger": MenuItem("burger", 150),
            "fries": MenuItem("fries", 100),
            "cola": MenuItem("cola", 50)
        }
        self.item_names = []
        self.quantities = []
        self.food_cart = []

    def display_menu(self):
        print("MENU:")
        for item in self.menu.values():
            print(f"{item.name}: {item.price}")

    def add_to_cart(self):
        while True:
            item_name = input("Enter Dish Name to add in Cart: ")
            quantity = int(input("Enter Dish Quantity: "))
            item = self.menu.get(item_name)
            if item:
                self.item_names.append(item_name)
                self.quantities.append(quantity)
                price = item.price * quantity
                self.food_cart.append(price)
            else:
                print("Invalid item name. Please try again.")

            choice = input("Do you wish to add more items? (yes/no) ")
            if choice.lower() == "no":
                break

    def calculate_total_amount(self):
        amount = sum(self.food_cart)
        print("TOTAL AMOUNT: ₹", amount)
        return amount

    def apply_promo_code(self, amount, promo_code):
        if promo_code == "WELCOME50":
            if amount >= 159:
                print("Promo Code Applied Successfully...")
                discount = 0.50 * amount
                if discount >= 100:
                    discount = 100
                amount_to_pay = amount - discount
                print("Please Pay: ₹", amount_to_pay)
            else:
                print("Amount is Lesser for Promo Code...")
                print("Please Pay: ₹", amount)
        elif promo_code == "ZOMPAYTM":
            if amount >= 299:
                print("Promo Code Applied Successfully...")
                discount = 0.20 * amount
                if discount >= 50:
                    discount = 50
                amount_to_pay = amount - discount
                print("Please Pay: ₹", amount_to_pay)
                print("You will get a cashback of: ₹ 25")
            else:
                print("Amount is Lesser for Promo Code...")
                print("Please Pay: ₹", amount)
        else:
            print("Promo Code Invalid")
            print("Please Pay: ₹", amount)


def main():
    shopping_cart = ShoppingCart()

    shopping_cart.display_menu()
    shopping_cart.add_to_cart()

    amount = shopping_cart.calculate_total_amount()

    message = """
        Welcome to Zomato
        OFFERS FOR TODAY

        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.


        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.
    """

    promo_code = input("Enter Promo Code: ")
    shopping_cart.apply_promo_code(amount, promo_code)


if __name__ == "__main__":
    main()
