Eat = True
drink = False


def food():
    # when one condition is True

    if Eat:
        print("I will eat Pizza. ")
    else:
        print("I am Good.")

    # For 2 Conditions. When both are true the print statement will run.

    if Eat and drink:
        print("I will eat pizza and drink soda.")
    else:
        print("I am Good.")

    # For 2 Conditions. When one condition is True the print statement will run.

    if Eat or drink:
        print("I will eat pizza or drink soda.")
    else:
        print("I am Good.")

    # Else if Statements

    if Eat:
        print("I will eat pizza.")
    elif drink:
        print("I will drink soda.")
    else:
        print("I am Good.")

    # Not statement
    if not Eat:
        print("I am Good.")


# calling the Function
food()

var1 = 123
var2 = 54
if var1 == var2:
    print("YES")
else:
    print("NO")

if var1 == var2 != var3:
    print("YES")
else:
    print("NO")

    # Greater than condition
if var1 > var2:
    print("YES")
else:
    print("NO")

    # Comparison of strings
var1 = "Blue"
var2 = "Red"
var3 = "Yellow"

if var1 == var2:
    print("Same Colors.")
elif var1 == var3:
    print("Same Colors.")
else:
    print("Not same.")
