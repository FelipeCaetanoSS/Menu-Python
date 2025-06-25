lista_itens = ["Prato 1","Prato 2", "Prato 3", "Prato 4", "Prato 5","Prato 6","Prato 7","Prato 8","Prato 9", "Prato 10", "Prato 11","Pedidos","Finaliizar compra"]
lista_preco = [29.99, 29.99, 34.99, 19.99, 23.99, 19.99, 26.99, 32.99, 40.99, 22.99, 27.99,0.0,0.0]
pedidos = []
valor_total = 0
item = -1

print("Seja bem - vindo!!")
print("----------------------------------------------------------------\n")

while item != 13:
    for i in range(len(lista_itens)):
        print(i, lista_itens[i], lista_preco[i])

    escolha = input("\n Adicionar pedido: ")
    item = int(escolha)

    if item < 12:
        pedidos.append(item)
        valor_total += lista_preco[item]
        print("Item adicionado ao pedidos! \n")
        print("----------------------------------------------------------------\n")

    elif item == 12:
        print("PEDIDOS")
        for i in range(len(pedidos)):
            print("Item:", lista_itens[i])
            print("VALOR TOTAL: R$ \n", valor_total)
            print("----------------------------------------------------------------\n")
            
    else:
        print("Erro, tente novante! \n")
        print("----------------------------------------------------------------\n")

print("Compra finalizada.\n")
print("Obrigado pela preferência!\n\n")
print("PEDIDOS: \n")
for i in range(len(pedidos)):
    print(lista_itens[i])
print(f"Valor total: R${valor_total}")