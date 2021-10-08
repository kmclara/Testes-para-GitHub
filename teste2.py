#Teste para o GITHUB. 

#Pedindo ao usuário sua idade: 
idade = int(input("Diga-me a sua idade: "))

#Cálculo dos anos que o usuário poderá entrar se for menor que 10 anos: 
cálculo = (10-idade)

#If, Else, Elif
if idade == 10: 
    print("Sua idade está na média. Você poderá entrar no brinquedo!")
elif idade < 10: 
    print("Você não poderá entrar no brinquedo! Ainda faltam {} anos pra você brincar neste brinquedo!".format(cálculo))
elif idade > 10: 
    print("Você já tem mais de 10 anos! Poderá entrar no brinquedo! Boa diversão!")

print("Obrigada por usar nosso programa! Volte sempre!")