lista_itens = ["Prato 1","Prato 2", "Prato 3", "Prato 4", "Prato 5","Prato 6","Prato 7","Prato 8","Prato 9", "Prato 10", "Prato 11"]
lista_preco = [29.99, 29.99, 34.99, 19.99, 23.99, 19.99, 26.99, 32.99, 40.99, 22.99, 27.99] 
pedidos = []
valor_total = 0.0
item = -1

print("    Seja bem - vindo!!")
print("----------------------------\n")

while item != 0:
    print("\tCARDÁPIO\n")
    for i in range(len(lista_itens)):
      print(f"{i + 1}. {lista_itens[i]} - R${lista_preco[i]}")
    
    print("\n0 para finalizar a compra!")
    print("12 para exibir os pedidos!")
    print("\n----------------------------\n")

    try:
        escolha = int(input("Adicionar pedido: "))
        item = escolha 
    except ValueError:
        print("Entrada inválida.")
        print("Por favor, digite um número.\n")
        print("----------------------------\n")
        continue

    if item > 0 and item < 12:
        pedidos.append(item - 1)
        valor_total += lista_preco[item - 1]
        print(f"\n{lista_itens[item - 1]}")
        print("Item adicionado aos pedidos! \n")
        print("----------------------------\n")

    elif item == 12:
        print("\nPEDIDOS:")
        for i in range(len(pedidos)):
          print(f"Item: {lista_itens[pedidos[i]]}.\n") 
        print("Valor total: R$", valor_total)
        print("\n----------------------------\n")

    elif item == 0:
        print("Finalizando compra...")
        print("\n----------------------------\n")
        break 

    else:
        print("Erro!")
        print("Tente números que estão no cardápio\n")
        print("----------------------------\n")

print("Compra finalizada.\n")
print("Obrigado pela preferência!\n")
print("PEDIDOS: \n")
for item_index in pedidos: 
    print(lista_itens[item_index])
print(f"Valor total: R${valor_total}")
