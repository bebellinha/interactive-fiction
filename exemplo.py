from random import choices, randint
import json

# Site para construir diagramas: https://www.drawio.com/

def read_json(input_file):
    '''Função para ler um arquivo json'''
    # Read JSON data.
    try:
        with open(input_file, encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception(f"Arquivo {input_file} não encontrado.")
    return data

lista_inimigos = read_json('inimigos.json')
print(lista_inimigos)

class Inimigo:
    def __init__(self, nome:str, ataques:dict):
        '''Método construtor para a classe Inimigo

        # Parametros:

        - nome (str): O nome do inimigo
        - ataques (dict): Um dicionário que contenha um ou mais ataques, o ataque é um dicionário que contenha descricao (str com o texto descritivo sobre o ataque) e o dado (texto que vai ser convertido em dano)
        '''
        # Digitando self antes do atributo para salvar aquela variavel como parte da classe
        self.nome = nome
        self.ataques = ataques
        pass

    def atacar(self):
        '''
        # Descrição

        Método que vai escolher um ataque aleatório
        '''
        print(list(self.ataques.keys()))
        ataque_escolhido = choices(list(self.ataques.keys()), k=1)[0]
        return self.ataques[ataque_escolhido]

    def __str__(self) -> str:
        '''Método padrão do python que torna possível converter uma instancia de objeto em texto, através de um print(objeto) ou str(objeto) 
        '''
        str_ataques = ''
        for nome_ataque, atributos in self.ataques.items():
            str_ataques += f'\n  {nome_ataque}\n' + \
                           f'    Descrição: {atributos["descricao"]}, Dado: {atributos["dado"]}'
        return(f'Nome: {self.nome}, com os ataques: {str_ataques}')

class Mesa:
    def __init__(self) -> None:
        pass

    def rolar_dado(self, dado:str):
        # Separar o texto do dado em uma lista ex.: 'd4+2' -> ['d4','2']
        etapas = dado.split('+')
        # Resultados acumulados do dado
        acumuluado = 0
        # Iterar por cada etapa que foi separada no split
        for etapa in etapas:
            # Se a etapa tiver um 'd' ele vai entrar aqui, ex.: '2d20'
            if 'd' in etapa:
                # Primeiro conjunto de digitos será a quantidade de dados, segundo conjunto de digitos será o dado rodado
                quantidade_dados, dado = etapa.split('d')
                # Iterar N vezes de acordo com a quantidade de dados a serem rolados
                for _ in range(int(quantidade_dados) if quantidade_dados != '' else 1):
                    # Remove e converte para inteiro a primeira letra da etapa que seria o 'd' do 'd20'
                    maximo = int(dado)
                    # Escolhendo um numero aleatorio entre 1 (minimo que o dado pode dar) até o maximo do dado (4 em um 'd4')
                    resultado = randint(1,maximo)
                    print(f'Dado d{maximo} rolado: {resultado}')
                    # Somando os resultados da rolagem do dado
                    acumuluado += resultado
            else:
                # Apenas convertendo um número que interfere no resultado do dado, ex.: '+2'
                resultado = int(etapa)
                # Somando os resultados da rolagem do dado
                acumuluado += resultado
        # Retorna o resultado acumulado da ação
        return acumuluado

    def processar_ataque(self, ataque:dict, ):
        '''Método que coleta o ataque escolhido pelo jogador ou inimigo e vai rolar o dado, retornando o resultado.

        No futuro daria para incluir a origem e o destino do ataque para colocar em um print
        e rodar um método de remover HP da classe do Inimigo ou do Jogador.
        '''
        # Ataque escolhido
        print(ataque)
        # Rolar o dado (d4) e aplicar os modificadores do ataque (+2)
        dano = self.rolar_dado(ataque['dado'])
        return dano

# inimigo = Inimigo(lista_inimigos['Jorge']['nome'], lista_inimigos['Jorge']['ataques'])
inimigo = Inimigo(**lista_inimigos['Esqueleto'])
mesa = Mesa()
# Printa o inimigo e a versão texto dele
print(inimigo)
# Retornar um ataque aleatorio
print(inimigo.atacar())
# Processar o ataque (rolar o dado e retornar o dano)
print('Dano igual a ', mesa.processar_ataque(inimigo.atacar()))
