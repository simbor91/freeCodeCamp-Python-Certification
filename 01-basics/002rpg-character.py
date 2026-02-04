# 01 Python Basics
# Lab: Build an RPG Character

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):
        print('The character name should be a string.')
        return

    if name == '':
        print('The character should have a name.')
        return

    if len(name) > 10:
        print('The character name is too long.')
        return
    
    if ' ' in name:
        print('The character should not contain spaces.')
        return


    if not isinstance(strength, int) or not isinstance (intelligence, int) or not isinstance(charisma, int):
        print('All stats should be integers.')
        return
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        print('All stats should be no less than 1.')
        return

    if strength > 4 or intelligence > 4 or charisma > 4:
        print('All stats should be no more than 4.')
        return 
    
    if strength + intelligence + charisma != 7:
        print('The character should start with 7 points.')
        return 

    rpg = {
        'name': name,
        'stats': {
            'STR': strength,
            'INT': intelligence,
            'CHA': charisma
        }
    }
    print(rpg['name'])
    for stat, value in rpg['stats'].items():
        score = full_dot * value + empty_dot * (10 - value) 
        print(stat, score)

create_character('ren', 3, 3, 1)