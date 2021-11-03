def soma():
    return x + y

def subtrai():
    return x - y

def multiplica():
    return x * y

def divide():
    return x / y

print('Bem vindo a calculadora!')
i = 'yes'
while i == 'yes':

    print('1 = +')
    print('2 = -')
    print('3 = *')
    print('4 = /')

    op = input('Escolha uma operação: ')

    if op == '1' or op == '2' or op == '3' or op == '4':

        print('Operação n: ', op)
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
    
        if op == '1':
            print(soma())

        elif op == '2':
            print(subtrai())
        
        elif op == '3':
            print(multiplica())
        
        elif op == '4':
            print(divide())

        i = input('Quer fazer outro calculo? (yes/no) ')
    
    
    else:
        print('Operação inválida')

else:
    print('Entendido, até a proxima!')
     


