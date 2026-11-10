class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item["amount"]

        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")

        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        title = f"{self.name.center(28, '*')}"
        title = f"*{title}*"

        output = title + "\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]

            output += f"{description:<23}{amount:>7.2f}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    spending = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])

        spending.append(total)

    total_spent = sum(spending)

    percentages = []

    for amount in spending:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spent) * 100)

        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Create the vertical bar chart.
    for level in range(100, -1, -10):
        output += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                output += "o  "
            else:
                output += "   "

        output += "\n"

    # Create the horizontal line.
    output += "    " + "-" * (len(categories) * 3 + 1)

    # Find the longest category name.
    max_length = max(
        (len(category.name) for category in categories),
        default=0
    )

    # Display category names vertically.
    for i in range(max_length):
        output += "\n     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "

    return output


# Example usage
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)

    print(food)
    print()

    print(create_spend_chart([food, clothing]))
    