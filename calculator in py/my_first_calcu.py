# starting the studies to see what I need - step one: create two input

number_one = float(input("Write the first number: "))
number_two = float(input("Write the second number to make the math operation: "))

operador = input("What type of operation will work? +; - / and x: ")

resultado_add = number_one + number_two
resultado_less = number_one - number_two
resultado_division = number_one//number_two
resultado_x = number_one * number_two

if operador == "+":
    print(resultado_add)
    if operador== "-":
        print(resultado_less)
        if operador== "/":
            print(resultado_division)
        elif operador == "X":
            print(resultado_x)
            