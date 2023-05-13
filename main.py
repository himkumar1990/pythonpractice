# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    x = lambda a: a + 10
    y = lambda a, b: a * b
    z = lambda a, b, c: a + b + c
    print(x(5))
    print(y(3, 4))
    print(z(3, 4, 5))

    def myFunc(n):
        return lambda a: a*n

    twice_multi = myFunc(2)

    print(twice_multi(2))
    print(twice_multi(3))
    print(twice_multi(4))


