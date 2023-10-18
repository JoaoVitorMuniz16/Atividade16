Situação = input("Você é idoso, gestante, cadeirante ou nenhum destes? Digite 'gestante', 'idoso', 'cadeirante', ou nenhum: ")

if Situação == "idoso" or Situação == "gestante" or Situação == "cadeirante":
    print ("Você tem acesso a fila de prioridade")
else:
    print ("Você não tem acesso a fila de prioridade")