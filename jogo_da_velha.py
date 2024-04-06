# Jogo da Velha

import time
import random

# Método com uma lista de 'strings' como argumento para mostrar o tabuleiro

def tabuleiro(escolha: list) -> None:
    """Imprime o tabuleiro do jogo da velha"""
    print()
    print(f" {escolha[6]} │ {escolha[7]} │ {escolha[8]} ")
    print("───┼───┼───")
    print(f" {escolha[3]} │ {escolha[4]} │ {escolha[5]} ")
    print("───┼───┼───")
    print(f" {escolha[0]} │ {escolha[1]} │ {escolha[2]} ")

def nomear_jogador(simbolo: str, numero: int) -> str:
    """Solicita o nome do jogador"""
    while True:
        nome_jogador = input(f"\nDigite o nome do {numero}° jogador que será ► {simbolo} ◄: ").strip().title()
        if nome_jogador:
            return f"{simbolo} {nome_jogador} {simbolo}"

def checar_vitoria(escolha: list) -> bool:
    """Método que checa se há vitória a partir de uma lista de 'strings'"""
    # Checar vitória na horizontal
    for i in range(0, 9, 3):
        if escolha[i] == escolha[i+1] == escolha[i+2] != " ":
            return True

    # Checar vitória na vertical
    for i in range(3):
        if escolha[i] == escolha[i+3] == escolha[i+6] != " ":
            return True

    # Checar vitória na diagonal
    if escolha[0] == escolha[4] == escolha[8] != " ":
        return True
    if escolha[2] == escolha[4] == escolha[6] != " ":
        return True

    return False

def checar_empate(escolha: list) -> bool:
    """Verifica se há empate"""
    return " " not in escolha and not checar_vitoria(escolha) or escolha.count(" ") == 1

def jogada_valida(escolha: list, jogada: int) -> bool:
    """Verifica se a jogada é válida"""
    return 1 <= jogada <= 9 and escolha[jogada - 1] == " "

def rodada(escolha: list, jogador: str) -> None:
    """Executa uma rodada do jogo"""
    tabuleiro(escolha)
    while True:
        jogada_str = input(f"\n{jogador}, escolha uma posição entre \033[1;30m(1-9)\033[m: ")
        if not jogada_str.isdigit():
            print("\nEntrada inválida! Digite apenas números.")
            continue
        jogada = int(jogada_str)
        if not jogada_valida(escolha, jogada):
            print("\nJogada inválida! Escolha uma posição disponível.")
            continue
        escolha[jogada - 1] = jogador.split()[0]
        break

def jogo_da_velha():
    """Função principal para o jogo da velha"""
    print("\n ► \033[1;031m○\033[m ◄ \033[1;030mJogo da Velha\033[m ► \033[1;034mx\033[m ◄\n")
    input("Pressione \033[1;032mENTER\033[m para iniciar:")
    print("\033[1;030mCarregando...\033[m")
    time.sleep(1)
    jogador1 = nomear_jogador("\033[1;031m○\033[m", 1)
    jogador2 = nomear_jogador("\033[1;034m×\033[m", 2)
    print("\nComo jogar:")
    print("Cada campo do jogo está associado a um número. Conforme ilustração abaixo.")
    tabuleiro([str(i) for i in range(1, 10)])
    print("\nPara ganhar é necessário obter \033[1;30m03\033[m símbolos iguais e consecutivos.")
    print("\033[1;030mCarregando...\033[m\n")
    time.sleep(4)

    # Escolher aleatoriamente quem será o primeiro jogador
    primeiro_jogador = random.choice([jogador1, jogador2])
    jogadores = [primeiro_jogador, jogador1 if primeiro_jogador != jogador1 else jogador2]

    print(f"{jogadores[0]} ► \033[1;30mvs\033[m ◄ {jogadores[1]}\n")
    
    escolha_do_jogo = [" "] * 9

    for num_rodada_atual in range(1, 10):
        jogador_atual = jogadores[num_rodada_atual % 2]
        rodada(escolha_do_jogo, jogador_atual)
        if checar_vitoria(escolha_do_jogo):
            tabuleiro(escolha_do_jogo)
            print(f"\nParabéns {jogador_atual} você venceu, na {num_rodada_atual}ª rodada!")
            break
        if checar_empate(escolha_do_jogo):
            tabuleiro(escolha_do_jogo)
            print("\nOpa, houve um empate! Sem estresse, jogue novamente")
            break
        time.sleep(0.5)
    print("\nObrigado por jogar!\n")

if __name__ == "__main__":
    jogo_da_velha()