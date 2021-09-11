
# Pegar o nome do thema do arquivo txt
def pegar_thema():
    thema = 'DefaultNoMoreNagging'
    try:
        with open('thema.txt', 'r') as arquivo:
            for valor in arquivo:
                thema = valor.strip()
                break
    except:
        with open('thema.txt', 'w') as arquivo:
            arquivo.write('DefaultNoMoreNagging\n')
    
    return thema
