# * The Code
"""Budget calculator app for freecodec(x.spent for x inbamp assignm)ent."""
import itertools

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
        self.spent = 0

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
            self.spent += witamount
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
            self.spent += tranamount
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
    categories = list(filter(None, (cat1, cat2, cat3, cat4)))
    total = sum(x.spent for x in categories)
    percentages = {x.name: int(round((100 * x.spent/total), -1)) for x in categories}
    bars = {"hunds": "100| ", "nineties": " 90| ", "eighties": " 80| ", "seventies": " 70| ", "sixties": " 60| ", "fifties": " 50| ", "fourties": " 40| ", "thirties": " 30| ", "twenties": " 20| ", "tens": " 10| ", "zeroes": "  0| "}
    for i in percentages.values():
        if i == 100:
            bars["hunds"] = bars["hunds"] + "o "
        if i > 89:
            bars["nineties"] =  bars["nineties"] + "o "
        if i>79:
            bars["eighties"] = bars["eighties"] + "o "
        if i>69:
            bars["seventies"] = bars["seventies"] + "o "
        if i>59:
            bars["sixties"] = bars["sixties"] + "o "
        if i>49:
            bars["fifties"] = bars["fifties"] + "o "
        if i>39:
            bars["fourties"] = bars["fourties"] + "o "
        if i>29:
            bars["thirties"] = bars["thirties"] + "o "
        if i>19:
            bars["twenties"] = bars["twenties"] + "o "
        if i>9:
            bars["tens"] = bars["tens"] + "o "
        if i>0:
            bars["zeroes"] = bars["zeroes"] + "o "

    divider = "    " + ("-" * (len(bars["zeroes"]) - 3))
    counter = 0
    namessplit = list((list(x) for x in percentages.keys()))

    match len(categories):
        case 1:
            names = namessplit
        case 2:
            names = (list(itertools.zip_longest(namessplit[0], namessplit[1])))
        case 3:
            names = (list(itertools.zip_longest(namessplit[0], namessplit[1], namessplit[2])))
        case 4:
            names = (list(itertools.zip_longest(namessplit[0], namessplit[1], namessplit[2], namessplit[3])))
        case _:
            print("Graph function only supports up to 4 categories!")
            exit()

    namesclean = []
    for i in names: namesclean += [" " if x is None else x for x in i]

    i = len(categories)
    while i < len(namesclean):
        namesclean.insert(i, "\n    ")
        i += (len(categories)+1)
    namesclean = ' '.join(namesclean)

    graph = "Percentage spent by categories\n"
    for x in bars:
        graph += (bars[x]) + "\n"
    graph += divider + "\n     " + namesclean

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
clothing.withdraw(20)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)
create_spend_chart(food, clothing, auto)
#  LocalWords:  Init
