lista = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for n in lista:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for c in n:
        if c.lower() in 'aeiou': print(c, end=' ')