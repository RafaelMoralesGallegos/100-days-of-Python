# *Functiosn inputs/funcitonality/output
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functiona sre firt-class objects, can be passed around as arguments
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


# Nested Functions
# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     nested_function()


def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


if __name__ == "__main__":
    # print(f"Result is: {calculate(multiply, 3, 2)}")
    inner_function = outer_function()
    inner_function()
