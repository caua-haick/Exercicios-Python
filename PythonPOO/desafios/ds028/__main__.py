from rich import print, inspect
from termostato import *

def main():
    t = Termostato()
    t.temperatura = 29
    inspect(t, methods=True, private = True)
    print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == "__main__":
    main()