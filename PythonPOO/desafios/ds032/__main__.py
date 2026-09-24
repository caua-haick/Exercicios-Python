from retangulo import *


def main():
    r = Retangulo(3)
    r.altura=3
    print(r.medidas)
    r.medidas= (4, 9)
    print(r.medidas)



if __name__ == '__main__':
    main()