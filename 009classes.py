# 06 Classes and Objects
# Lesson 1

class Dog:
    def __init__(self, name, age): # self è l'oggetto stesso, name,age sono i valori che devi passare quando crei l'oggetto
        self.name = name # self. è un attributo dell’oggetto, cioè qualcosa che rimane memorizzato dentro l’istanza
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof! I'm {self.age} years old")

# Create 2 objects using Dog class as blueprint
dog1 = Dog('Jack', 3)
dog2 = Dog('Dolly', 5)

# Call the bark method
dog1.bark()
dog2.bark()

# -------------------------
def deposit(self, amount, description=''):
    entry = {'amount': amount, 'description': description} # dict
    # no self.amount = amount e self.description = description perché:
    # amount e description non sono proprietà permanenti della categoria, ma dati di una singola transazione
    # gli attributi dell'oggetto devono descrivere l'oggetto, non un evento
    self.ledger.append(entry)

# Non ha senso che la categoria abbia un attributo “amount” o “description”, perché:
# - ogni deposito ha un proprio amount
# - ogni deposito ha una propria description
# - se li salvassi in self.amount, verrebbero continuamente sovrascritti e perderesti la storia dei movimenti

# I dati vanno salvati nel ledger, non nell'oggetto. Quando fai:
# self.ledger.append({"amount": amount, "description": description})
# stai dicendo:
# “Questo movimento appartiene alla categoria, ma non è la categoria.”


