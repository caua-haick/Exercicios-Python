from transporte import *

def main():
    dist = int(input("Digite a distância do frete em km: "))

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}km = [cyan]{entrega.calc_frete()}[/]")

if __name__ == "__main__":
    main()