# ---------------------------------------------------------------------------
# PRÁTICA 1 - SISTEMA DE RECOMENDAÇÃO DE VIAGEM [cite: 2]
# Curso: Qualificação em IA Industrial [cite: 1]
# Unidade Curricular: Fundamentos de Python para IA [cite: 1]
# ---------------------------------------------------------------------------

# --- Base de Dados de Destinos ---
# Utilizando uma lista de dicionários para armazenar os destinos e suas características. 
# O sistema pode ser facilmente expandido adicionando novos dicionários a esta lista. [cite: 24]
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

# --- Funções do Sistema ---
# O uso de funções ajuda a organizar o código e evitar repetições. [cite: 19]

def obter_preferencias_do_usuario():
    """
    Esta função interage com o usuário para obter suas preferências de viagem.
    Ela realiza a leitura das preferências conforme solicitado. [cite: 21]
    Inclui validação de entrada para garantir que as respostas sejam válidas. 
    """
    # Pergunta sobre o clima [cite: 9]
    while True:
        clima = input("Você prefere clima quente ou frio? ").lower().strip()
        if clima in ["quente", "frio"]:
            break
        else:
            print("Resposta inválida. Por favor, digite 'quente' ou 'frio'.")

    # Pergunta sobre o ambiente [cite: 10]
    while True:
        ambiente = input("Prefere lugares com natureza ou paisagens urbanas? (digite 'natureza' ou 'urbano') ").lower().strip()
        if ambiente in ["natureza", "urbano"]:
            break
        else:
            print("Resposta inválida. Por favor, digite 'natureza' ou 'urbano'.")

    # Pergunta sobre o orçamento [cite: 11]
    while True:
        try:
            orcamento = float(input("Qual é o seu orçamento disponível para a viagem (em R$)? "))
            if orcamento > 0:
                break
            else:
                print("Por favor, insira um valor positivo para o orçamento.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o orçamento.")

    return {"clima": clima, "ambiente": ambiente, "orcamento": orcamento}


def recomendar_destino(preferencias, lista_de_destinos):
    """
    Compara as preferências do usuário com a lista de destinos disponíveis. [cite: 22]
    Usa um laço 'for' para percorrer os dados e 'if' para tomar decisões. [cite: 18, 30]
    """
    destinos_compativeis = []
    for destino in lista_de_destinos:
        # Estrutura condicional para verificar a compatibilidade
        if (preferencias["clima"] == destino["clima"] and
            preferencias["ambiente"] == destino["ambiente"] and
            preferencias["orcamento"] >= destino["orcamento"]):
            destinos_compativeis.append(destino)

    return destinos_compativeis


def apresentar_recomendacao(recomendacoes):
    """
    Apresenta o resultado da busca ao usuário.
    Retorna a sugestão mais adequada ou uma mensagem de que nada foi encontrado. [cite: 23]
    """
    print("\n--- Resultado da Recomendação ---")
    if not recomendacoes:
        print("Desculpe, não encontramos um destino compatível com suas preferências e orçamento.")
    else:
        # Pega o primeiro destino compatível encontrado
        destino_sugerido = recomendacoes[0]
        print(f"Destino recomendado: {destino_sugerido['nome']} [cite: 13]")

        # Apresenta uma justificativa simples para a recomendação [cite: 14]
        justificativa = (f"Esta é uma ótima opção de viagem com clima {destino_sugerido['clima']}, "
                         f"ambiente de {destino_sugerido['ambiente']} e que se encaixa no seu orçamento!")
        print(f"Justificativa: {justificativa}")

# --- Execução Principal do Script ---
def main():
    """
    Função principal que organiza a execução do programa.
    """
    print("Bem-vindo ao Sistema de Recomendação de Viagem!")
    
    # Chama a função para obter as preferências do usuário
    prefs_usuario = obter_preferencias_do_usuario()
    
    # Chama a função para encontrar destinos compatíveis
    lista_recomendada = recomendar_destino(prefs_usuario, destinos)
    
    # Apresenta o resultado
    apresentar_recomendacao(lista_recomendada)


# Garante que o script será executado apenas quando chamado diretamente
if __name__ == "__main__":
    main()