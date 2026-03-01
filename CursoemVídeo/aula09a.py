frase = 'Curso em Vídeo Python'
#Fatiamento: print(frase[onde começa:onde termina:pulando de quanto em quanto])
#Análise len(frase) quantidade de caracteres; frase.count('o',0,13) contar quantos "o" tem na frase do começo até o caracter 12
# frase.find('deo') quantas vezes ele encontrou e onde "deo", se não existe o computador retornará o valor '-1'
# 'Curso' in frase ; é uma pergunta de resposta true ou false
# frase.replace('Python', 'Android') substituição de termos
#frase.upper() escrever em maiúsculo; 'lower' faz o mesmo em minuscula
#frase.capitalize() só o primeiro caracter fica maiusculo
#frase.title() quantas palavras tem na string
fras = '   Aprenda Python  '
#fras.strip() tira os espaços desnecessários
#fras.rstrip() tira só os espaços da direita, só os da esquerda é fras.lstrip
#frase.split() divide a frase considendo os espaços criando novas variaveis
#'-'.join(frase) rejuntar a frase
print(frase.upper().count('o'))
print(len(frase.strip()))
print(""""Welcome are comple...    hhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh""")
# as aspás triplas servem para não precisar usar outros comandos para quebrar a linha
dividido = (frase.split())
print(dividido[2][3]) #primeiro termo é a palavra e o segundo o caracter



