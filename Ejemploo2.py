def calcular(multiplicando, multiplicador, sumando):
    resultado = multiplicando * multiplicador + sumando
    return resultado

def FuncionPrincipal():
    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicador: "))
    sumando = float(input("Sumando: "))
    resultado = calcular(multiplicando, multiplicador, sumando)
    print(f"{multiplicando} * {multiplicador} + {sumando} = {resultado}") 


if __name__== "__main__":
    FuncionPrincipal()
