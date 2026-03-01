from ex115.lib.interface import *
def arquivoExiste(arq):
    try:
        a= open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    try:
        a= open(arq, 'wt+') #escrever\criar
        a.close()
    except:
        print('\033[31mErro ao criar arquivo\033[m')
    else:
        print(f'Arquivo {arq} criado com sucesso!')

def lerArquivo(arq):
    try:
        a= open(arq, 'rt') #ler
    except:
        print('\033[31mErro ao ler arquivo\033[m')
    else:
        cabecalho('\033[34mPESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a= open(arq, 'at') #adicionar
    except:
        print('\033[31mHouve um erro ao tentar abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao tentar escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

