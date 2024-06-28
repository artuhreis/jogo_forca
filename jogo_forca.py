import random

# Função para escolher uma palavra aleatória da lista
def palavras():
    lista_palavras = ["DEVWEB", "PYTHON", "JAVASCRIPT", "DESENVELOPER", "HTML", "CSS"]
    return random.choice(lista_palavras)

#Função para chutar a palavra inteira
def chutar_palavra(palavra):
    palavra_chutada = input("Digite seu chute de palavra: ").upper() # Recebe uma letra do jogador e converte para maiúsculas
    if palavra_chutada == palavra:
        print("Parabéns! Você acertou a palavra:", palavra)
        return True
    else:
        print("Você errou! Continue.")
        return False
# Função para iniciar o jogo da forcag
def inicio_game():
    palavra = palavras()  # Escolhe uma palavra aleatória
    letras_acertadas = []  # Lista para armazenar as letras acertadas
    tentativas = 7  # Número de tentativas que o jogador tem

    # Inicializa a lista letras_acertadas para cada letra da palavra
    for _ in palavra:
        letras_acertadas.append('_')

    print("Você ínicio o jogo da Forca!")
    print("A palavra esta relacionada com programação, e tem", len(palavra), "letras.") # Uma dica da quantidade de letras para o jogador
    print(" ".join(letras_acertadas))  # Mostra o estado atual das letras acertadas

    # Loop principal do jogo, continua enquanto o jogador tiver tentativas restantes
    while tentativas > 0:
        letra = input("Digite uma letra: (Se desejar chutar a palavra por inteira, Digite 1) ").upper()  # Recebe uma letra do jogador e converte para maiúsculas
        if letra == '1':
            if chutar_palavra(palavra):
                break

        if letra in palavra:  # Verifica se a letra está na palavra
            # Atualiza a lista letras_acertadas com a letra correta nas posições corretas
            for i in range(len(palavra)):  # Itera sobre o comprimento da palavra
                if palavra[i] == letra:  # Verifica se a letra no índice i da palavra é igual à letra digitada
                    letras_acertadas[i] = letra  # Atualiza a lista letras_acertadas na posição i
                    print("Você acertou!")
                    print(" ".join(letras_acertadas))# Imprime a letra correta na sua posição na palavra.

            if '_' not in letras_acertadas:  # Verifica se todas as letras foram acertadas
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            tentativas -= 1  # Diminui o número de tentativas se a letra não estiver na palavra
            print("Você errou! Tentativas restantes:", tentativas)
            if tentativas == 0:
                print("Você perdeu! A palavra era:", palavra)
   
    jogar_novamente = input("Deseja jogar novamente? s/n ").upper() # Recebe uma letra do jogador e converte para maiúsculas
    if jogar_novamente.lower() == 's':
        inicio_game()  # Inicia o jogo novamente
    elif jogar_novamente.lower() == 'n':
        print("Obrigado, volte sempre :)")  # Sai do jogo
    else:
        print("Opção inválida. Tente novamente.")  # Trata uma entrada inválida


# Função para exibir as regras do jogo e apresentar o sub-menu
def regras():
    print("Regras do Jogo da Forca:")
    print("1. Uma palavra secreta será escolhida aleatoriamente.")
    print("2. Você deve adivinhar a palavra letra por letra.")
    print("3. Cada letra errada resulta na perda de uma tentativa.")
    print("4. O jogo termina quando você adivinha a palavra ou perde todas as tentativas.")
    print("5. Você tem 7 tentativas para acertar a Palavra.")
    print("5. Dica: A palavra está relacionado com programação.")
    print("7. Boa sorte!\n")
    print("1 - Jogar")

    print("2 - Voltar ao Menu")
    print("3 - Sair")

    # Recebe a opção do jogador no sub-menu
    opcao2 = int(input("Escolha uma opção: "))
    if opcao2 == 1:
        inicio_game()  # Inicia o jogo
    elif opcao2 == 2:
        menu()  # Volta ao menu principal
    elif opcao2 == 3:
        print("Obrigado volte sempre!")  # Sai do jogo
    else:
        print("Opção inválida. Tente novamente.")  # Trata uma entrada inválida

# Função para exibir o menu principal do jogo
def menu():
    print("Bem vindo ao Jogo da Forca =)")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")

    # Recebe a opção do jogador no menu principal
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        inicio_game()  # Inicia o jogo
    elif opcao == 2:
        regras()  # Exibe as regras e o sub-menu
    elif opcao == 3:
        print("Obrigado, volte sempre :)")  # Sai do jogo
    else:
        print("Opção inválida. Tente novamente.")  # Trata uma entrada inválida

# Chama a função para exibir o menu principal
menu()

