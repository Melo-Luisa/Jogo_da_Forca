import turtle, random, tkinter
import tkinter as tk
import easygui

#cor da janela
screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor('purple')

#chamando forca 
t = turtle.Turtle()
t.fillcolor('white')
t.penup()
t.setpos(-190, -150)

#para palavras erradas
erro = turtle.Turtle()
erro.fillcolor('white')
erro.penup()
erro.color('white')
erro.setpos(-200, 250)
erro.pendown()

tentativas = 0
#define os niveis
def chances():
    msg ="Escolha o nível:"
    title = "Nível Forca:"
    global nivel, choice
    nivel = ["Normal", "Tormento", "Inferno", "Nightmare"]
    choice = easygui.choicebox(msg, title, nivel)
    global tentativas
    match choice:
        case 'Normal':
            tkinter.messagebox.showinfo(title="Nível selecionado", message=f"Você selecionou o nível {choice}! Você possui 6 tentativas")
            tentativas = 7
        case 'Tormento':
            tkinter.messagebox.showinfo(title="Nível selecionado", message=f"Você selecionou o nível {choice}! Você possui 4 tentativas")
            tentativas = 5
        case 'Inferno':
            tkinter.messagebox.showinfo(title="Nível selecionado", message=f"Você selecionou o nível {choice}! Você possui 2 tentativas")
            tentativas = 3
        case 'Nightmare':
            tkinter.messagebox.showinfo(title="Nível selecionado", message=f"Você selecionou o nível {choice}! Você possui 1 tentativas")
            tentativas = 2
chances()

#andar
def foward (t, passos) -> None:
    t.fd(passos)
    return

#desenha a forca
def forca():
    forca = turtle.Turtle()
    forca.penup()
    forca.pensize(3)
    forca.setpos(-200,50)
    forca.fillcolor('white')
    #desenhando forca
    forca.color('white')
    forca.pendown()
    foward(forca, 100)
    forca.setpos(-200,50)
    forca.right(90)
    foward(forca, 200)
    forca.hideturtle()
forca()
#desenha a cabeça

def head():
    doll = turtle.Turtle()
    doll.penup()
    doll.setpos(-100, 10)
    doll.color('red')
    doll.pensize(3)
    doll.pendown()
    doll.circle(20)
    doll.hideturtle()
#desenha o corpo
def body():
    body = turtle.Turtle()
    body.penup()
    body.setpos(-100, 10)
    body.color('red')
    body.pensize(3)
    body.right(90)
    body.pendown()
    foward(body, 75)
    body.hideturtle()
#desenha o braço esquerdo
arm = turtle.Turtle()
def arm_left():
    
    arm.penup()
    arm.setpos(-135, -30)
    arm.color('red')
    arm.left(45)
    arm.pensize(3)
    arm.pendown()
    foward(arm, 50)
    arm.hideturtle()
#desenha o braço direito
def arm_right():
    arm.penup()
    arm.setpos(-100, 5)
    arm.color('red')
    arm.right(65)
    arm.pensize(3)
    arm.pendown()
    foward(arm, 50)
    arm.hideturtle()
#desenha a perna esquerda
leg = turtle.Turtle()
def leg_left():
    leg.penup()
    leg.setpos(-135, -100)
    leg.color('red')
    leg.left(45)
    leg.pensize(3)
    leg.pendown()
    foward(leg, 50)
    leg.hideturtle()
#desenha a perna direita
def leg_right():
    leg.penup()
    leg.setpos(-100, -65)
    leg.right(65)
    leg.pensize(3)
    leg.pendown()
    foward(leg, 50)
    leg.hideturtle()

#abre as palavras e escolhe aleatório
with open('word.txt') as arquivo:
    #comando que tira o  \n do arquivo externo
    palavras = [linha.strip() for linha in arquivo.readlines()]
sorteio = random.choice(palavras)

#guarda a posição do traço e desenha o traço
traco_position = []
def traco():
    for letras in sorteio:
        # Cria uma lista vazia para as posições dos traços
        t.color('white')
        t.fd(20)
        traco_position.append(t.pos())
        t.write('_', align='center', font=('Arial', 18, 'normal'))
        t.hideturtle()
traco()

turtle.penup()

#mostra os erros
digitoErrados = []
#será incrementado os acertos
digitoCertos = 0

#enquanto o nivel não for selecionado não rodará o jogo
while True:
    #caixa de pergunta para salvar a letra
    digito = screen.textinput('Digite uma letra','digite:')

    #verifica se letra entra na palavra - funciona
    #ACERTO
    if digito in sorteio:

        #validando a letra
        for i in range(len(sorteio)):
            if sorteio[i] == digito:
                #pega a posição guardada da letra
                t.goto(traco_position[i])
                t.write(digito, align='center', font=('Arial', 18, 'normal')) 
                digitoCertos += 1
        #caso acerte a palavra
        if digitoCertos == len(sorteio):
            print('certo')
            tkinter.messagebox.showinfo(title=None, message='Parabéns! Você acertou!!')
            break
    #ERRO
    else:
        #soma os erros
        tentativas -= 1
        erro.write('Lista de erros: ')
        digitoErrados.append(digito)
        #limpa o anterior para não duplicar
        erro.clear()
        #Imprimi as teclas erradas
        erro.write(', '.join(digitoErrados), align='center', font=('Arial', 18, 'normal') )
        #desenha o corpo
        #case nivel normal
        if choice == 'Normal':
            if tentativas == 6:
                head()
            elif tentativas == 5:
                body()
            elif tentativas == 4:
                arm_left()
            elif tentativas == 3:
                arm_right()
            elif tentativas == 2:
                leg_left()
            elif tentativas == 1:
                leg_right()
        
        #caso o nivel Tormento 
        if choice == 'Tormento':
            if tentativas == 4:
                head()
            elif tentativas == 3:
                body()
            elif tentativas == 2:
                arm_left()
            elif tentativas == 1:
                arm_right()

        #case nivel Inferno
        if choice == 'Inferno':
            if tentativas == 2:
                head()
            elif tentativas == 1:
                body()
        
        #case nivel Nightmare
        if choice == 'Nightmare':
            if tentativas == 1:
                head()

    #caso chegue em ao final das tentativas == 1
        if tentativas == 1:
            print('Você perdeu o jogo! A palavra era', sorteio)
            tkinter.messagebox.showinfo(title=None, message='Você perdeu! palavra era: ' + str(sorteio))
            break
 
    turtle.pendown()
    screen.title('Forca')


#saida
screen.onkeypress(exit, 'q')
screen.listen()
turtle.done()
