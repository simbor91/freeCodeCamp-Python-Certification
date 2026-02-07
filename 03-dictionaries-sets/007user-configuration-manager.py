# 03 Dictionaries and Sets
# Lab: Build a User Configuration Manager

test_settings = {
    'theme': 'light', 
    'notifications': 'enabled', 
    'volume': 'low',
    'brightness': 50
}

def add_setting(settings: dict, pair: tuple):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        print(f"F.ADD: Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        print(f"F.ADD: Setting '{key}' added with value '{value}' successfully!")
    
    settings[key] = value 

def update_setting(settings: dict, pair: tuple):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        print(f"F.UPDATE: Setting '{key}' updated to '{value}' successfully!")
        settings[key] = value
    else:
        print(f"F.UPDATE: Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings: dict, key):
    key = key.lower()

    if key in settings:
        settings.pop(key)
        print(f"F.DELETE: Setting '{key}' deleted successfully!")
    else:
        print(f"F.DELETE: Setting not found!")
    
def view_settings(settings: dict):
    if not settings:
        print('No settings available')
    else:
        print('Current User Settings:')
        for key in settings:
            print(key.capitalize() + ': ' + str(settings[key]))

# versione con i 'return' e na roba strana 'end with a newline character.' per passare l'esercizio
# def view_settings(settings: dict):
    # if not settings:
    #     return 'No settings available.'
    # else:
    #     lines = ['Current User Settings:']
    #     for key, value in settings.items():
    #         lines.append(f'{key.capitalize()}: {value}')
    #     return '\n'.join(lines) + '\n'

add_setting(test_settings, ('THEME', 'dark'))
add_setting(test_settings, ('volume', 'high'))
update_setting(test_settings, ('theme', 'dark'))
update_setting(test_settings, ('volume', 'high'))
delete_setting(test_settings, 'brightness')
delete_setting(test_settings, 'name')
view_settings(test_settings)

