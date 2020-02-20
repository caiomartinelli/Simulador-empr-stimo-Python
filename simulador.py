# Simulador parcelas de um empréstimo bancario.
# O aplicativo somente libera para o cliente um valor cuja prestação não ultrapasse 1/3 de sua renda líquida


print("Simulador Empréstimo")

def simulador():
    
    nome = input ("Nome: ")
    print(nome)
    renda = float(input("Renda mensal: "))
    desejado = float(input("Valor Desejado: "))
    parcelas = int(input("Número de parcelas: "))
    total = desejado / parcelas
    
    if total >= renda / 3:
        print("Valor acima do permitido")
    else:
        print("Valor liberado")
        
    
simulador()