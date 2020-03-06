import math
import re

#DICIONÁRIO QUE DEFINE A TRADUÇÃO DO NÚMERO POR EXTENSO E SEU RESPECTIVO VALOR.
num_dict = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "três": 3,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "trinta": 30,
    "quarenta": 40,
    "cinquenta": 50,
    "sessenta": 60,
    "setenta": 70,
    "oitenta": 80,
    "noventa": 90,
    "cem": 100,
    "cento": 100,
    "duzentos": 200,
    "trezentos": 300,
    "quatrocentos": 400,
    "quinhentos": 500,
    "seiscentos": 600,
    "setecentos": 700,
    "oitocentos": 800,
    "novecentos": 900,
    "mil": 1000,
    "milhão": 1000000,
    "milhao": 1000000,
    "milhões": 1000000,
    "milhoes": 1000000,
    "bilhão": 1000000000,
    "bilhao": 1000000000,
    "bilhões": 1000000000,
    "bilhoes": 1000000000
    }


def converter(valor: str): 
    '''
    Função que recebe uma "string" com um valor numérico por extenso, 
    transforma esse valor através de um dicionário de dados e retorna
    um número do tipo "float".
    '''
    #VARIAVEIS AUXILIARES E LISTA (valor) CONTENDO OS ELEMENTOS DA "string"
    resultado = 0
    valor = valor.split(" ")
    aux_centavo = 0
    aux_milhar = 0

    #LOOP PARA PERCORRER A LISTA "valor" E INCREMENTAR O RESULTADO
    for i in range(len(valor)):
        #FUNÇÃO ".lower()" PARA NÃO HAVER DISTINÇÃO DE LETRAS MAIUSCULAS
        num_atual = valor[i].lower()

        if num_atual == "e" or num_atual == "centavos" or num_atual == "de":
            continue        
        #INCREMENTA O "aux_centavo" PARA DEFINIR SERÃO SOMADOS OS CENTAVOS. 
        if num_atual in "real reais":
            aux_centavo += 1
            continue

        if num_atual in "mil milhão milhao milhões milhoes bilhão bilhao bilhões bilhoes":
            if aux_milhar == 0:
                aux_milhar = 1
            resultado += aux_milhar * num_dict[num_atual]
            aux_milhar = 0
            continue

        if aux_centavo > 0:
            centavos = num_dict[num_atual] / 100
            resultado += centavos
        
        else:
            aux_milhar += num_dict[num_atual]

    resultado += aux_milhar
    #RETORNA O RESULTADO JÁ CONVERTIDO PARA FLOAT.
    return float(resultado)


def contar_buracos(valor: str): 
    '''
    Função que recebe a "string" do valor por extenso, conta os "buracos" 
    e retorna o valor inteiro do total de "buracos" encontrado.
    '''
    buracos = 0
    #LOOP PARA PERCORRER A "string" E FAZER A CONTAGEM.
    for i in range(len(valor)):
        if valor[i] in "abdeopqADOPQR":
            buracos += 1
        elif valor[i] in "gB":
            buracos += 2
    return buracos


def main():
    '''
    Função que pede um "input" de um valor por extenso, chama as funções
    "converter" e "contar_buracos", mostra a tradução do valor por extenso
    em "float" e o numero de "buracos". 
    '''
    #"valor_extenso" É O PARAMETRO NAS FUNÇÕES "converter" e "contar_buracos".
    valor_extenso = input("Valor por extenso: ")
    resultado = converter(valor_extenso)
    num_buracos = contar_buracos(valor_extenso)
    mostrar_valor = "Valor: R$ %.2f" % resultado
    print(str(mostrar_valor).replace(".",","))
    print("Total de {} buracos.".format(num_buracos))

#INICIAÇÃO DO CÓDIGO E VERIFICA SE ELE ESTÁ SENDO EXECUTADO DIRETAMENTE.
if __name__ == '__main__':
    main()
