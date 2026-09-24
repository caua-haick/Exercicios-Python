from contabancaria import *

def main():
    c1 = ContaBancaria(112, 'Gustavo', 3000)
    c1.depositar(500)
    c1.sacar(2000)
    print(c1)
if __name__ == "__main__":
    main()