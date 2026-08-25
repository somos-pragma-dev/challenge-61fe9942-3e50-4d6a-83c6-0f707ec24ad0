def calculate_simple_interest(principal, rate, time):
    return principal * rate * time

def main():
    principal = float(input("Ingrese el monto del préstamo: "))
    rate = float(input("Ingrese la tasa de interés anual: ")) / 100
    time = float(input("Ingrese el tiempo en años: "))
    interest = calculate_simple_interest(principal, rate, time)
    print(f'El interés ganado es: {interest}')

if __name__ == '__main__':
    main()