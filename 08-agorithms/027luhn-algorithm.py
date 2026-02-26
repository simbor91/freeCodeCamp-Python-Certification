# Algorithms
# Lab 027: Implement the Luhn Algorithm

def verify_card_number(card_number):
    card_number = [int(digit) for digit in card_number if digit.isdigit()] # pulisci da spazi o trattini
    # card_number = card_number[::-1] # inverti
    card_number.reverse()
    # print(card_number)

    n = len(card_number)
    sum_2char = []
    reworked_digit = 0
    
    for i in range(n):
        # print(f'{card_number[i]} a indice {i}')
        if i%2 == 1: # indice dispari    
            reworked_digit = int(card_number[i])*2
            if reworked_digit >= 10:
                reworked_digit -= 9
            sum_2char.append(reworked_digit)
        else:
            reworked_digit = int(card_number[i])
            sum_2char.append(reworked_digit)
    # print(f'intermedial check array moltiplicato: {sum_2char}')
    
    sum_numbers = 0
    for digit in sum_2char:
        sum_numbers += digit
    # print(f'intermedial check somma digit: {sum_numbers}')
    
    if sum_numbers % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

print(verify_card_number('453914889'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
print(verify_card_number('4111-1111-1111-1111'))