def main():
    #write your code below this line
    first = int(input("Give the first number:"))
    second = int(input("Give the second number:"))

    sum = first + second
    difference = first - second
    product = first * second
    quotient = first / second

    print(str(first) + " + " + str(second) + " = " + str(sum))
    print(str(first) + " - " + str(second) + " = " + str(difference))
    print(str(first) + " * " + str(second) + " = " + str(product))
    print(str(first) + " / " + str(second) + " = " + str(quotient))

if __name__ == '__main__':
    main()
