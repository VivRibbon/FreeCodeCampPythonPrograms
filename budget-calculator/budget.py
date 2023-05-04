# * The Code
"""Budget calculator app for freecodecamp assignment."""

# ** The class


class Category:

    """The budget app class containing its functions."""

    def __init__(self, name):
        """Init name, ledger, and balance variables shared by the class."""
        self.name = name
        self.ledger = []
        self.print = []
        self.descriptions = []
        self.amounts = []
        self.balance = 0

    def __str__(self):
        """Show formatted budget when printed."""
        budget = (
            ("*" * int(((30 - len(self.name))) / 2))
            + (self.name)
            + ("*" * int(((30 - len(self.name))) / 2))
            + ("\n")
            + ("\n".join([a[0:22] + (" " * int(30 - len(a[0:22]) - len(b))) + b for a,b in zip(self.print[0::2], self.print[1::2])])) # noqa
            + ("\n" + "Total: " + str(self.balance))
        )
        return budget

    def check_funds(self, chkamount):
        """Check if there's enough funds to perform an operation."""
        if chkamount > self.balance:
            return False
        elif chkamount <= self.balance:
            return True

    def deposit(self, depamount, depdescription = ""):
        """Add funds with an optional description."""
        self.balance += depamount
        self.print.append(depdescription)
        self.print.append(str(depamount))
        if depdescription is None:
            self.ledger.append({"amount: " + str(depamount) + ", description:" + ""})
        else:
            self.ledger.append(
                {"amount: " + str(depamount) + ", description: " + depdescription}
            )

    def withdraw(self, witamount, witdescription = ""):
        """Withdraw funds with an optional description."""
        if self.check_funds(witamount) is False:
            print("")

        else:
            witamount = -abs(witamount)
            self.balance += witamount
            self.print.append(witdescription)
            self.print.append(str(witamount))
            if witdescription is None:
                self.ledger.append(
                    {"amount: " + str(witamount) + ", description:" + ""}
                )
            else:
                self.ledger.append(
                    {"amount: " + str(witamount) + ", description: " + witdescription}
                )

    def transfer(self, tranamount, destination):
        """Transfer funds from one ledger to another."""
        if self.check_funds(tranamount) is False:
            print("Not enough funds")
        else:
            destination.ledger.append(
                {"amount: " + str(tranamount) + ", transfer from: " + self.name}
            )
            destination.balance += tranamount
            destination.print.append("Transfer from" + self.name)
            destination.print.append(str(tranamount))
            tranamount = -abs(tranamount)
            self.ledger.append(
                {"amount: " + str(tranamount) + ", transfer to: " + destination.name}
            )
            self.balance += tranamount
            self.print.append("Transfer to " + destination.name)
            self.print.append(str(tranamount))

    def get_balance(self):
        """Return the current balance of a ledger."""
        return self.balance


# ** The bar function
def create_spend_chart(cat1, cat2=None, cat3=None, cat4=None): 
    """Create a bar graph accepting up to four categories."""
    graph = (
        ("Percentage spent by category\n")
        + "test"


    )

    return print(graph)


# ** The test code

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing) 
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)
create_spend_chart(food)
#  LocalWords:  Init
