# function
# function is a block of organized, resuable code used to preform a single, related action
# built in functions: print(), input(), str(), int()


def sayHello():  # defining the function
    print("Hi!")


sayHello()  # invoking and printing said function


def menu():
    print("1. Chicken Nuggets")
    print("2. Burger")
    print("3. Cheeseburger")
    print("4. Fries")


menu()


def newHello(name):  # making an argument
    print("Hi! My name is " + name + ".")


newHello("Ronaldo")


def increment(x):  # initial value needed to replace
    x += 1
    print(x)


y = 4  # passing y as x, replacing x as 4
increment(y)


def fullName(first, last):
    print("Hello, I am " + first + " " + last + ".")


fullName("Christiano", "Ronaldo")


def additionExample(a, b, c, d):  # values line up with variables below
    print(a + b)
    print(c + d)


additionExample(1, 2, 3, 4)

# return values
# the function will return "None" if there is no return statement in the function


def additionExample(a, b, c, d):  # values line up with variables below
    print(a + b)
    print(c + d)
    return (
        a + b + c + d
    )  # returning the function. will print first two statements, but then return back


x = additionExample(1, 2, 3, 4)  # assigning a variable to the function
print(x)


# comparing two function
def returnFunction(a, b):
    return a + b


d = returnFunction(4, 8)  # have to set a variable to make it function
print(d)


def returnFunctionTwo(a, b):
    print(a + b)


returnFunctionTwo(4, 8)
e = returnFunctionTwo(4, 8)  # will return none if there is no "return" statement
print(e)

# method overloading: defining same name with different parameters. python only takes the latest one, whatever has been executed

# def sayHello(name):
# print("Hello, I am " + name + ".")

# def sayHello(first, last): # will take this code, and throw an error
# print("Hello, I am " + first + last + ".")

# sayHello(Messi)

# limitations


def square(x):
    return x * x


def cube(x):
    return x**3


f = square  # points to function square
g = cube  # points to function cube
h = f  # points to square
f = g  # after the switch, a now points to cube

print(f(2), g(2), h(2))

# anonymous functions
# functions defined without a name


def triangle(x):
    return x * x


def sumTriangles(n):
    total = 0
    for i in range(n + 1):
        total += square(i)
    return total


print(sumTriangles(4))

# with lambda functions


def sumTrianglesTwo(m):
    newtotal = 0
    for i in range(m + 1):
        square = (
            lambda x: x * x
        )  # argument/parameter used is x, used when expressions are small
        newtotal += square(i)
    return newtotal


print(sumTrianglesTwo(4))

# higher order functions


def hi(func, first, last):  # becomes greetings
    message = func(first, last)
    print(message)


def greetings(first, last):  # takes the input, passing the function to the other
    return "Hello, I am " + first + " " + last + "."


hi(greetings, "Bat", "Man")

# dynamic typing allows for more flexibility


def add(w, z):
    return w + z


print((add(3, 9)))
print(add("Hello", "World"))

# variable scopes
# a variable declared in that function is only visible inside that function


def scope(r, t):
    addNum = r + t
    return addNum


# print(addNum) says it is not defined as the variable deletes outside the code

# global variables

l, p = 2, 3


def magic():  # defining magic as "two" and "three"
    global l  # will always define l as "two"
    l = "two"
    p = "three"


print(l, p)  # prints 2,3
magic()
print(l, p)
