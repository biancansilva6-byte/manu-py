# print("Ola, voce!")

# nome = "Joao"

# variavel que recebe um valor input
# senha = input("Digite uma senha: ")

# if senha == "grau moranguete":
#     print("Senha correta!&")
# elif senha == "abobora":
#     print("Senha correta!")
# else:
#     print("Senha errada!")

print("bem-vindo ao bot da Manu ;p")
opcao = input("Digite um valor de 1 a 10: ")

match opcao:
    case "1":
        print("Setor de atendimento")
        print("Qual atendente voce deseja falar? SAC ou RH")
        atendente = input ("Digite o atendimento desejado: ")

        if atendente == "SAC":
            print("Voce vai ser direcionado para o SAC")
        elif atendente == "RH":
            print("Voce vai ser direcionado para o RH")
        else:
            print("Não existe esse atendimento")

    case "2":
        print("Pagamento do curso")
        print("Segunda via de boleto...")
        curso = input ("Qual a forma de pagamento") 

        if curso == "boleto":
           print("Voce escolheu pagamento por boleto ")
        elif curso == "cartão":
            print("Voce escolheu a forma de pagamento por cartão")
        else:
            print("Forma de pagamento invalida")
        

    case "4":
         print("Fale como foi seu final de semana...")
         final = input("Foi bom, ruim ou normal? ")

         if final == "bom": 
          print("Que bom! Parece que você aproveitou bastante!")
         elif final == "ruim":
          print("Poxa, espero que o próximo seja melhor!")
         elif final == "normal":
          print("Entendi, foi um final de semana tranquilo.")
         else:
            print("Obrigado por compartilhar!")

    case "5":

        print("Qual curso você faz no SENAI?")
        curso = input("Digite o nome do seu curso: ")

        if curso == "Manufatura Digital":
         print("Que legal! Manufatura Digital é uma ótima área!")
        elif curso == "mecanica":

         print("Muito legal! Mecânica é uma área interessante!")
        else:
         print("Legal! Você faz o curso de", curso)

    case "6":
        print("Comente como foi a praia...")
        praia = input("Você gostou da praia? ")

        if praia == "sim":
         print("Que bom! Deve ter sido muito divertido!")
        elif praia == "sim, mas estava chovendo":
         print("Poxa! Talvez na próxima seja melhor.")
        else:
         print("Obrigado por contar como foi!")

    case "7":
         print("Que dia você irá fazer sua unha?")
         unha = input("Digite o dia: ")

         if unha == "trça- feira, depois do curso":
          print("Você vai fazer sua unha na terça- feira!")
         elif unha == "sexta":
          print("Sexta é um ótimo dia para fazer a unha!")
         else:
          print("Você fará sua unha na Gaby")

    case "8":
      
       print("Qual o nome do seu professor?")
       professor = input("Digite o nome: ")

        if professor == "Lucas":
          print("O professor Lucas é muito legal!")
        elif professor == " Lucas":
          print("O professor Lucas é muito legal!")
        else:
          print("Seu professor é", professor)

    case "9":
      
         print("Você anda de moto com seu namorado?")
         moto = input("Digite sim ou não: ")

         if moto == "sim":
          print("Que legal! ")
         elif moto == "não":
          print("Entendi!")
         else:
          print("Responda apenas sim ou não.")

    case "10":
        print("Não existe opção, digite de 1 a 9")