

def main():

    num = int(input("Digite o numero de nomes :"))

    names=[]
    aux=[]

    for i in range(num):
        names.append(input("Digite o " + str(i) + "º nome :"))

    cont=0

    for o in range(num-1):
        for i in range (0,num-o-1):
            if names[i]>names[i+1]:
                aux.append(names[i+1])
                names[i+1]=names[i]
                names[i]=aux[cont]
                cont = cont + 1

    for i in range(num):
        print(str(i + 1) + "º nome =" + names[i])

if __name__ == '__main__':
    main()