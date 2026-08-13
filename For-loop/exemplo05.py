


# for loop com if (condicional)
sucesso = False
for numero in range(3):
    print("tentativa")
    if sucesso: # dentro da variavel 'suceso' está o valor booleano (true ou false)
      print("sucesso!, meu jovem.")
      break
else:
    print("todas as 3 tentativas falharam!!!")