def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'no se puede dividir por 0'


if __name__ == "__main__":
    numero1 = int(input('ingrese el primer numero: '))
    numero2 = int(input('ingrese el segundo numero: '))

    print("Suma:", sumar(numero1, numero2))
    print("Resta:", restar(numero1, numero2))
    print("Multiplicación:", multiplicar(numero1, numero2))
    print("División:", dividir(numero1, numero2))