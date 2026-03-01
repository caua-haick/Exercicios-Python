aluno = {'nome': str(input('Nome do aluno: ')),
         'media': float(input('Media do aluno: ')),}
print('-='*30)
print(f'- Nome do aluno: {aluno["nome"]}')
print(f'- Média do aluno: {aluno["media"]:.1f}')
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'RECUPERAÇÃO'
print(f'- Situação do aluno: {aluno["situacao"]}')
