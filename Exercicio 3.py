# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:35:11 2023

@author: Raquel Fernandes
"""

#Exercício 1: Criador de Perfil de Personagem
#Objetivo: O seu desafio é desenvolver um programa Python que permita ao utilizador criar e
#personalizar perfis de personagens fictícios. Para cada perfil, deve incluir, pelo menos, as
#seguintes informações: nome, idade, profissão, hobbies e uma breve descrição.
#O programa deve ter as seguintes funcionalidades:
#1. Adicionar um novo perfil de personagem;
#2. Modificar um perfil de personagem existente;
#3. Remover um perfil de personagem;
#4. Visualizar a lista completa de personagens;
#5. Pesquisar um personagem específico pelo nome.



personagem_1 = {"nome": "João" , "idade":"30" , "profissão": "programador" , "hobbies": ["ciclismo","jogos de video"] , "descrição": "João é um programador talentoso que adora o que faz..."}
personagem_2 = {"nome": "Eva" , "idade":"35" , "profissão": "programador" , "hobbies": ["artes","ballet"] , "descrição": "Eva é um programador talentoso que adora o que faz..."}

Lista_personagens = ["personagem_1", "personagem_2"]

#def adicionar_personagem(lista_personagens):
#    nome = input("Digite o nome do personagem: ")
 #   idade = int(input("Digite a idade do personagem: "))
#    profissao = input("Digite a profissão do personagem: ")
#    hobbies = input("Digite os hobbies do personagem, separados por vírgula: ").split(",")
#    descricao = input("Digite uma breve descrição do personagem: ")

#personagem = {"nome": nome,"idade": idade, "profissão": profissao, "hobbies": hobbies, "descrição": descricao}

#lista_personagens.append(personagem)

#def visualizar_personagens(lista_personagens):
#    for personagem in lista_personagens:
 #       print("---------------------------")
#        print("Nome:", personagem["nome"])
#        print("Idade:", personagem["idade"])
#        print("Profissão:", personagem["profissão"])
#        print("Hobbies:", ", ".join(personagem["hobbies"]))
#        print("Descrição:", personagem["descrição"])

#lista_personagens = []

#while True:
#    print("1. Adicionar personagem")
#    print("2. Visualizar personagens")
#    print("3. Sair")
#opcao = int(input("Escolha uma opção: "))
#if opcao == 1:
#    adicionar_personagem(lista_personagens)
#elif opcao == 2:
#    visualizar_personagens(lista_personagens)
#elif opcao == 3:
#break
#else:
#    print("Opção inválida. Tente novamente.")
    
    
    
    
    ################################
    
    
def adicionar_personagem(lista_personagens):
    nome = input("Digite o nome do personagem: ")
    idade = int(input("Digite a idade do personagem: "))
    profissao = input("Digite a profissão do personagem: ")
    hobbies = input("Digite os hobbies do personagem, separados por vírgula: ").split(",")
    descricao = input("Digite uma breve descrição do personagem: ")

    personagem = {"nome": nome, "idade": idade, "profissão": profissao, "hobbies": hobbies, "descrição": descricao}
    lista_personagens.append(personagem)

def modificar_personagem(lista_personagens):
    nome = input("Digite o nome do personagem que deseja modificar: ")
    encontrado = False

    for personagem in lista_personagens:
        if personagem["nome"] == nome:
            encontrado = True
            campo = input("Digite o campo que deseja modificar (nome, idade, profissão, hobbies, descrição): ")
            if campo in personagem:
                novo_valor = input("Digite o novo valor para o campo {}: ".format(campo))
                personagem[campo] = novo_valor
                print("Perfil do personagem modificado com sucesso.")
            else:
                print("Campo inválido.")
            break

    if not encontrado:
        print("Personagem não encontrado.")

def remover_personagem(lista_personagens):
    nome = input("Digite o nome do personagem que deseja remover: ")
    removido = False

    for personagem in lista_personagens:
        if personagem["nome"] == nome:
            lista_personagens.remove(personagem)
            print("Personagem removido com sucesso.")
            removido = True
            break

    if not removido:
        print("Personagem não encontrado.")

def visualizar_personagens(lista_personagens):
    for personagem in lista_personagens:
        print("---------------------------")
        print("Nome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", ", ".join(personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])

lista_personagens = []

while True:
    print("1. Adicionar personagem")
    print("2. Modificar personagem")
    print("3. Remover personagem")
    print("4. Visualizar personagens")
    print("5. Pesquisar personagem pelo nome")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_personagem(lista_personagens)
    elif opcao == 2:
        modificar_personagem(lista_personagens)
    elif opcao == 3:
        remover_personagem(lista_personagens)
    elif opcao == 4:
        visualizar_personagens(lista_personagens)
    elif opcao == 5:
        nome = input("Digite o nome do personagem que deseja pesquisar: ")
        encontrado = False

        for personagem in lista_personagens:
            if personagem["nome"] == nome:
                encontrado = True
                print("---------------------------")
                print("Nome:", personagem["nome"])
                print("Idade:", personagem["idade"])
                print("Profissão:", personagem["profissão"])
                print("Hobbies:", ", ".join(personagem["hobbies"]))
                print("Descrição:", personagem["descrição"])
                break

        if not encontrado:
            print("Personagem não encontrado.")
    elif opcao == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")

    
    
    
    
    
    