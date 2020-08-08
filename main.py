import random


def generateRandom(upper):
    r = random.randint(1, upper)
    return r


def main():

    print("Do the multiplication")
    x = generateRandom(10)
    y = generateRandom(10)
    result = x * y
    run = True

    while run:
        asw = input(str(x) + " * " + str(y) + " =? ")
        if asw.isdigit():
            if int(asw) == result:
                print("Correto!")
                run = False
            else:
                print("Errado, tente novamente!")
        else:
            print("Digite um numero positivo")

if __name__ == '__main__':
    main()