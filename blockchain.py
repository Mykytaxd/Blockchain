blockchain = []


def get_last_block_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_block():
    for block in blockchain:
        print('Outputting block ')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True


while waiting_for_input:
    print('Please choose ')
    print('1: Add a new transaction ')
    print('2: Output the blocks ')
    print('3: Manipulate chain  ')
    print('4: Quit  ')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_block_value())
    elif user_choice == '2':
        print_block()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '4':
        waiting_for_input = False
    else:
        print('Invalid input')
    if not verify_chain():
        print('Invalid block')
        break
else: 
    print('User left')