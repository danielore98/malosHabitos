# Función para calcular el área de un rectángulo
def AreaRectangulo(base, altura):
    resultado = base * altura
    return resultado

# Función para calcular el área de un triángulo
def AreaTriangulo(base, altura):
    resultado = 0.5 * base * altura
    return resultado

# Función principal
def FuncionPrincipal():
    base = float(input("Base del Rectangulo: "))
    altura = float(input("Altura del Rectangulo: "))
    rect_area = AreaRectangulo(base, altura)
    print(f"{base} * {altura} = {rect_area}")

    base = float(input("Base del Triangulo: "))
    altura = float(input("Altura del Triangulo: "))
    tri_area = AreaTriangulo(base, altura)
    print(F"{base} * {altura} = {tri_area}")

FuncionPrincipal()
