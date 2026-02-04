# 07 Objects-Oriented Programming (OOP)
    # OOP and Encapsulation
# Workshop: Build a Salary Tracker

class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    def __init__(self, name, level): # method inside class with parameters

        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")

        self._name = name # assign parameters to the instance attributes with the same name
        self._level = level
        self._salary = Employee._base_salaries[level]
        
    def __str__(self):
        return f'{self.name}: {self.level}'
    # prima scritto self._name, poi self.name dopo che ho definito property sotto (uguale per level)
    # This will call the getters instead of directly accessing the attributes.

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    @property # @property is a decorator to turn a method into a property
    def name(self):
        return self._name
    # it is used to define getter methods = retrieve a value of an attribute

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self._name}'.")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}.")

        # prima del salary setter:
        # self._salary = Employee._base_salaries[new_level] 
        self.salary = Employee._base_salaries[new_level] # chiamando ora il salary setter, stampa un messaggio in più definito dentro il salary setter
        self._level = new_level
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if not isinstance (new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(f"Salary must be higher than minimum salary ${self.salary}.")
        
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')

charlie_brown = Employee('Charlie Brown', 'junior') # create a class instance (passing arguments) and assign it to a variable
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.name = 'Ciccio'
charlie_brown.level = 'mid-level'
# charlie_brown.salary = 3200
# print(charlie_brown)