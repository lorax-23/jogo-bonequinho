from pyscript import document, when


# ==================================================
# JOGADOR
# ==================================================

# Posição inicial do jogador
x = 100
y = 100

# Velocidade do jogador
velocidade = 10

# Localiza o jogador no HTML
jogador = document.querySelector("#jogador")


# ==================================================
# ATUALIZAR A POSIÇÃO DO JOGADOR
# ==================================================

def atualizar_jogador():

    jogador.style.left = f"{x}px"
    jogador.style.top = f"{y}px"


# ==================================================
# CONTROLE DO TECLADO
# ==================================================

@when("keydown", "body")
def tecla_pressionada(evento):

    global x, y

    # ----------------------------------------------
    # SETA PARA A DIREITA
    # ----------------------------------------------

    if evento.key == "ArrowRight":
        x += velocidade


    # ----------------------------------------------
    # SETA PARA A ESQUERDA
    # ----------------------------------------------

    elif evento.key == "ArrowLeft":
        x -= velocidade


    # ----------------------------------------------
    # SETA PARA BAIXO
    # ----------------------------------------------

    elif evento.key == "ArrowDown":
        y += velocidade


    # ----------------------------------------------
    # SETA PARA CIMA
    # ----------------------------------------------

    elif evento.key == "ArrowUp":
        y -= velocidade


    # Se não foi uma das setas, não faz nada
    else:
        return


    # ==================================================
    # LIMITES DA ÁREA DO JOGO
    # ==================================================

    if x < 0:
        x = 0

    if x > 650:
        x = 650

    if y < 0:
        y = 0

    if y > 410:
        y = 410


    # Atualiza a posição na tela
    atualizar_jogador()


# ==================================================
# INICIALIZAÇÃO
# ==================================================

atualizar_jogador()