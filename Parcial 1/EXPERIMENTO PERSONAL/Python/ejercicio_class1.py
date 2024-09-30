class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name        # Se corrige 'self' para el nombre
        self.age = age          # Se corrige 'self' para la edad
        self.pay = pay
        self.job = job

if __name__ == '__main__':  # Comillas corregidas
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    
    # Imprimir los atributos correctos
    print(bob.name, sue.pay)        # Imprime el nombre de Bob y el salario de Sue
    print(bob.name.split()[-1])     # Esto imprimirá 'Smith', el apellido de Bob
    sue.pay *= 1.10                 # Incrementa el salario de Sue en un 10%
    print(sue.pay)                  # Imprime el nuevo salario de Sue
