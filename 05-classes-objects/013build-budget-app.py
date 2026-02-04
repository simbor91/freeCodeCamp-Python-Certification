# 06 Classes and Objects
# Lab: Build a Budget App

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        entry = {'amount': amount, 'description': description} # dict
        # amount e description non sono proprietà permanenti della categoria, ma dati di una singola transazione
        self.ledger.append(entry)

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        amount = -amount
        entry = {'amount': amount, 'description': description}
        self.ledger.append(entry)
        return True
    
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        # Titolo in mezzo a 30 asterischi
        half = int((30 - len(self.name)) / 2)
        ast = ''
        for _ in range(0, half):
            ast += '*'
        output = ast + self.name + ast
        if len(output) < 30:
            output += '*\n'
        else:
            output += '\n'
        # Formattare correttamente ogni riga del ledger (23 caratteri + 7 caratteri)
        for entry in self.ledger:
            description = entry['description']
            amount = entry['amount']
            amount = '%.2f' % amount # questo me la rende una stringa quindi dopo nella stampa non devo fare str(amount)
            if len(description) > 23:
                description = description[:23]
            space_left = int(23 - len(description))
            left = ''
            for _ in range(0, space_left):
                left += ' '

            space_right = int(7 - len(amount))
            right = ''
            for _ in range(0, space_right):
                right += ' '

            output += description + left + right + amount + '\n'
        # Final line
        output += f'Total: {self.get_balance()}'
        return output
        
def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    # numero categorie, mi serve per i trattini orizzontali
    num_categ = 0
    # dict = {'category'=category.name, 'withdraws'=sum}
    expenses = {}
    for category in categories:
        sum = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                sum += entry['amount']
        expenses[category.name] = sum
        num_categ += 1
    # total withdraws per category
    total_expenses = 0
    for expense in expenses:
        total_expenses += expenses[expense]
    # list = [% food, % clothin, ...]
    percentages = []
    for category in categories:
        percentage = int((expenses[category.name] / total_expenses * 100) // 10)*10
        percentages.append(percentage)

    for y_label in range(100,-1,-10):
        len_space = 3 - len(str(y_label))
        chart += ' ' * len_space # +3
        chart += f'{y_label}| ' # Spazio dopo il pipe | --> +1
        for percentage in percentages:
            if percentage >= y_label:
                chart += 'o  ' # "o" seguita da DUE spazi (totale 3 caratteri) --> +3
            else:
                chart += '   '
        if y_label > 0:
            chart += '\n'
    chart += '\n' # +1 tot 8
    chart += '    ' + '---' * num_categ + '-' + '\n' # 4 + 3 + 1 tot 8 torna con sopra

    # nomi verticali
    max_len = len(categories[0].name)
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    for i in range(0,max_len):
        chart += '     ' # +5
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  ' # +3 tot 8 torna con sopra
            else:
                chart += '   '
        if i+1 < max_len:
            chart += '\n'
    return chart

        
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))

# categories è una lista di oggetti Category --> create_spend_chart([food, clothing])
# categories[0] = oggetto Category = stringa
# categories[0].ledger = lista di movimenti, ogni movimento è un dizionario = lista di dizionari
#         ogni dizionario ha {'amount': 1000, 'description': 'deposit', 'category': 'food'}

# Category
#  ├── name: "Food"
#  └── ledger: [
#         {"amount": 1000, "description": "deposit"},
#         {"amount": -10.15, "description": "groceries"},
#         {"amount": -15.89, "description": "restaurant and more food for dessert"},
#         {"amount": -50, "description": "Transfer to Clothing"}
#     ]