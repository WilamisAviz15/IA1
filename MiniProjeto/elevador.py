def SearchOnBase():
    fileR = open("base_de_regras.txt","r")
    for i in fileR:
        rules = i.split()
        #print(rules)
    fileR.close()

def main():
    while(1):
        current_floor = 1
        button = 1
        SearchOnBase()
        print('Você está no', current_floor, 'andar')
        button = input('Você deseja ir para qual andar? Digite de 1 a 6 \n')
        print('Você digitou', button)
main()