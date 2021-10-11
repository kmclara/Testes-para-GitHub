 #Prática teorica aula 12 - Mundo 02 

#Perguntando nome ao usuário: 
nome = str(input("Qual seu nome? ")).title()
print(nome)
nome_em_maiusculo = nome.capitalize()

#Se, senão se, senão
if nome == "Maria Clara":
    print("Seu nome é lindo!")
elif nome == "Jovesrbardo":
    print("Seu nome não é muito legal! Tente mudar no cartorio, {}!".format(nome))
elif nome == "Luiz" or nome == "Marcos" or nome == "Tiago": 
    print("Seu nome é normal, incremente algo, {}!".format(nome))
elif nome == "Lisa" or nome == "Elisiane" or nome == "Elton" or nome == "Eunice" or nome == "Adailton":
    print("Seu nome não é muito comum, porém, muito interessante!")

print("Tenha um bom dia, {}!".format(nome))