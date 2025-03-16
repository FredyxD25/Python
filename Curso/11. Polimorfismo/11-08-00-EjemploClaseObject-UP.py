class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre, apellido):
        self.nombre = nombre  # Inicializa el atributo nombre
        self.apellido = apellido  # Inicializa el atributo apellido

    # Sobreescribir el método __str__ para definir cómo se representa el objeto como cadena
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}'''  # Muestra la dirección de memoria del objeto

# Código principal
persona1 = Persona('Ana', 'Martinez')  # Se crea un objeto de la clase Persona
print(persona1)  # El método __str__ se llama automáticamente cuando se usa print
#print(persona1.__str__())  # Llamada explícita al método __str__, es opcional