import itertools
import random


def gerar_wordlists(palavras_chave):
    
    permutacoes = []
    combinacoes = []
    mesclagens = []
    
    for i in range(1, len(palavras_chave) + 1):
        permutacoes += list(itertools.permutations(palavras_chave, i))
        
    for i in range(1, len(palavras_chave) + 1):
        combinacoes += list(itertools.combinations(palavras_chave, i))
    
    for i in range(1, len(palavras_chave)):
        mesclagens += list(itertools.combinations(palavras_chave, i))
   
    wordlist = permutacoes + combinacoes + mesclagens
    wordlist = [''.join(item) + str(random.randint(0, 9999)) for item in wordlist]
    
    return wordlist

palavras_chave = ['Computacao', 'SAS', 'Materia', 'UFT','Texto','Invalido']
wordlist = gerar_wordlists(palavras_chave)

for palavra in wordlist:
    print(palavra)