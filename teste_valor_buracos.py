import math
import re

#DECLARANDO UM DICIONÁRIO QUE DEFINE A TRADUÇÃO DO NÚMERO POR EXTENSO E SEU RESPECTIVO VALOR.
num_dict = {
    "zero":0,
    "um":1,
    "dois":2,
    "três":3,
    "tres":3,
    "quatro":4,
    "cinco":5,
    "seis":6,
    "sete":7,
    "oito":8,
    "nove":9,
    "dez":10,
    "onze":11,
    "doze":12,
    "treze":13,
    "quatorze":14,
    "quinze":15,
    "dezesseis":16,
    "dezessete":17,
    "dezoito":18,
    "dezenove":19,
    "vinte":20,
    "trinta":30,
    "quarenta":40,
    "cinquenta":50,
    "sessenta":60,
    "setenta":70,
    "oitenta":80,
    "noventa":90,
    "cem":100,
    "cento":100, 
    "duzentos":200,
    "trezentos":300,
    "quatrocentos":400,
    "quinhentos":500,
    "seiscentos":600,
    "setecentos":700,
    "oitocentos":800,
    "novecentos":900,
    "mil":1000,
    "milhão":1000000,
    "milhões":1000000,
    "bilhão":1000000000,
    "bilhões":1000000000
    }

def converter(valor:str):
    '''
    Função que recebe uma "string" com um valor numérico por extenso, 
    transforma esse valor através de um dicionário de dados e retorna
    um número do tipo "float".
    '''

    #DECLARO DUAS VARIAVEIS (resultado e aux_centavo) COM O VALOR "0" PARA AUXILIAR COM AS OPERAÇÕES MATEMÁTICAS
    #DEFINO "valor" COMO UMA LISTA CONTENDO TODAS AS PALAVRAS SEPARADAS POR UM ESPAÇO VAZIO.
    resultado = 0
    valor = valor.split(" ")
    aux_centavo = 0

    #FAÇO UM LOOP PARA PERCORRER A LISTA "valor" E ASSIM FAZER AS OPERAÇÕES E INCREMENTAR O RESULTADO
    for i in range(len(valor)):
        #UTILIZO A FUNÇÃO ".lower()" PARA NÃO HAVER DISTINÇÃO DE LETRAS MAIUSCULAS
        num_atual = valor[i].lower()

        if num_atual == "e" or num_atual == "centavos":
            continue
        
        #ESTE TRECHO INCREMENTA O "aux_centavo" PARA DEFINIR QUE OS PRÓXIMOS VALORES SERÃO SOMADOS EM CENTAVOS. 
        if num_atual in "real reais":
            aux_centavo += 1
            continue

        if resultado > 0 and num_atual in "mil milhão milhões bilhão bilhões":
            resultado = resultado * num_dict[num_atual]
            continue

        if aux_centavo > 0:
            centavos = num_dict[num_atual] / 100
            resultado += centavos
        
        else:
            resultado += num_dict[num_atual]

    #RETORNA O RESULTADO JÁ CONVERTIDO PARA FLOAT.
    return float(resultado)

def contar_buracos(valor:str):
    '''
    Função que recebe a "string" do valor por extenso, conta os "buracos" 
    e retorna o valor inteiro do total de "buracos" encontrado.
    '''

    #DEFINO "buracos" COM O VALOR "0" E FAÇO UM LOOP PARA PERCORRER TODAS AS LETRAS DA "STRING" E SOMANDO COM 1 OU 2 "buracos"
    buracos = 0
    for i in range(len(valor)):
        if valor[i] in "abdeopqADOPQR":
            buracos += 1
        elif  valor[i] in "gB":
            buracos += 2
    return buracos

def main():
    '''
    Função que pede um "input" de um valor por extenso, chama as funções "converter" e
    "contar_buracos", mostra a tradução do valor por extenso em "float" e o numero de "buracos". 
    '''
    #"valor_extenso" RECEBE O "INPUT" QUE É USADO COMO PARAMETRO NAS FUNÇÕES "converter" e "contar_buracos"
    valor_extenso = input("Valor por extenso: ")
    resultado = converter(valor_extenso)
    num_buracos = contar_buracos(valor_extenso)
    mostrar_valor = "Valor: R$ %.2f" % resultado
    print(str(mostrar_valor).replace(".",","))
    print("Total de {} buracos.".format(num_buracos))

#REALIZA A INICIAÇÃO DO CÓDIGO E VERIFICA SE ELE ESTÁ SENDO EXECUTADO DIRETAMENTE.
if __name__ == '__main__':
   main()
