# material

destinos = [
    {
        "nome": "Floresta Amazônica, Brasil",
        "clima": "quente",
        "ambiente": "natureza",
        "orcamento": 2000
    },
    {
        "nome": "Tóquio, Japão",
        "clima": "frio",
        "ambiente": "urbano",
        "orcamento": 7000
    },
    {
        "nome": "Rio de Janeiro, Brasil",
        "clima": "quente",
        "ambiente": "urbano",
        "orcamento": 2500
    },
    {
        "nome": "Bariloche, Argentina",
        "clima": "frio",
        "ambiente": "natureza",
        "orcamento": 4000
    },
    {
        "nome": "Cancún, México",
        "clima": "quente",
        "ambiente": "natureza",
        "orcamento": 5000
    },
    {
        "nome": "Nova York, EUA",
        "clima": "frio",
        "ambiente": "urbano",
        "orcamento": 8000
    }
]

# FUNÇÕES

def obter_preferencia_usuario():

    while True:
        clima = input("Voce prefere clima quente ou frio: ").lower().strip()
        if clima in ["quente", "frio"]:
            break
        else:
            print("Resposta invalida. por favor digite 'quente' ou 'frio'. ")

    while True:
        ambiente = input("Prefere lugares com natureza ou paisagens urbanas? (digite apenas 'natureza' ou 'urbano') ").lower().strip()
        if ambiente in ["natureza", "urbano"]:
            break
        else:
            print("Resposta invalida. por favor digite 'natureza' ou 'urbano'. ")

    while True:
        try:
            orcamento = float(input("Qual é o orçamento disponivel para viagem? (digite apenas numeros, ex: 9000) "))
            if orcamento > 0:
                break
            else:
                print("Por favor, insira um valor positivo")
        except ValueError:
            print("Entrada invalida. Por favor, digite um número para o orçamento, sem pontos ou vírgulas.")
    

    preferencias = {
        "clima": clima,
        "ambiente": ambiente,
        "orcamento": orcamento
    }
    return preferencias

def recomendar_destino(preferencias, lista_destinos):

    destinos_compativeis = []
    for destino in lista_destinos:

        if (preferencias["clima"] == destino["clima"] and 
            preferencias["ambiente"] == destino["ambiente"] and
            preferencias["orcamento"] >= destino["orcamento"]):
            destinos_compativeis.append(destino)

    return destinos_compativeis

def apresentar_recomendacao(recomendacoes):

    if not recomendacoes:
        print("\nDesculpe, não encontramos um destino compativel com suas preferencias.")
    else:
        
        print("\nCom base nas suas preferências, encontramos os seguintes destinos:")
        for destino_sugerido in recomendacoes:
            print(f"\nDestino recomendado: {destino_sugerido['nome']}")

            justificativa = (f"Esta é uma ótima opção de viagem com clima {destino_sugerido['clima']}, "
                           f"ambiente de {destino_sugerido['ambiente']} e que se encaixa no seu orçamento de R$ {destino_sugerido['orcamento']:.2f}.")
            
            print(f"Justificativa: {justificativa}")

def main():

    print("Bem-vindo ao sistema de recomendação de viagem!")

    prefs_usuario = obter_preferencia_usuario()

    lista_recomendada = recomendar_destino(prefs_usuario, destinos)

    apresentar_recomendacao(lista_recomendada)

if __name__ == "__main__":
    main()