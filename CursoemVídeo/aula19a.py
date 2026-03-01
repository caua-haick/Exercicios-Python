pessoas ={'nome':'Pedro','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#del pessoas['sexo'] apaga o sexo
#pessoas['nome'] = 'leandro' troca o nome no dicionário de pedro para leandro
pessoas['peso'] = 80
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')