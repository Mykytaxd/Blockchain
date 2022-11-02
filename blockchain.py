genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Mykyta'


def get_last_block_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {'Sender': sender, 'Recipient': recipient, 'Amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block_hash = ''
    for key in last_block:
        value = last_block[key]
        block_hash = block_hash + str(value)
    print(block_hash)
    block = {'previous_hash': block_hash, 'index': len(
        blockchain), 'transactions': open_transactions}
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Please enter recipient address')
    tx_amount = float(input('Your transaction amount: '))
    return tx_recipient, tx_amount


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
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False

    return is_valid


waiting_for_input = True


while waiting_for_input:
    print('Please choose ')
    print('1: Add a new transaction ')
    print('2: Output the blocks ')
    print('3: Manipulate chain  ')
    print('4: Quit  ')
    print('5: Mine new block  ')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_block()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '4':
        waiting_for_input = False
    elif user_choice == '5':
        mine_block()
    else:
        print('Invalid input')
    # if not verify_chain():
    #     print('Invalid block')
    #     break
else:
    print('User left')
