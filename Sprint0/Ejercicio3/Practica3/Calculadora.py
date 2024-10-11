from Operaciones import sumar,restar,dividir,multiplicar

def menu():
    print('Elija un tipo de operacion: ')
    print('1) suma')
    print('2) resta')
    print('3) mulplicacion')
    print('4) division')


if __name__ == '__main__':
    respuesta = 'S'

    while respuesta=='S':
        numero1 = int(input('ingrese el primer numero: '))
        numero2 = int(input('ingrese el segundo numero: '))

        menu()
        operacion_tipo = input('ingrese la operacion que desea realizar: ')
        while operacion_tipo!='1' and operacion_tipo!='2'and operacion_tipo!='3'and operacion_tipo!='4':
            print('la opcion ingresada es incorrecta')
            menu()
            operacion_tipo = input('ingrese la operacion que desea realizar: ')

        if operacion_tipo=='1':
            print(sumar(numero1,numero2))
        elif operacion_tipo=='2':
            print(restar(numero1,numero2))
        elif operacion_tipo=='3':
            print(multiplicar(numero1,numero2))
        else:
            print(dividir(numero1,numero2))

        respuesta = (input('para seguir realizando operacion ingrese s para salir ingrese n:')).upper()