mining_reward = 10
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Mykyta'
participants = {'Mykyta'}


def get_last_block_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def mine_block():
    last_block = blockchain[-1]
    block_hash = hash_block(last_block)
    reward_transaction = {
        'sender': 'mining',
        'recipient': owner,
        'amount': mining_reward
    }
    open_transactions.append(reward_transaction)
    block = {'previous_hash': block_hash, 'index': len(
        blockchain), 'transactions': open_transactions}
    blockchain.append(block)
    return True


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True


while waiting_for_input:
    print('Please choose ')
    print('1: Add a new transaction ')
    print('2: Output the blocks ')
    print('3: Manipulate chain  ')
    print('4: Quit  ')
    print('5: Mine new block  ')
    print('6: Output participants  ')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Transaction added')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        print_block()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
                             'index': 0, 'transactions': [{'sender': 'Chris', 'recipient': 'Mykyta', 'amount': 100.0}]}
    elif user_choice == '4':
        waiting_for_input = False
    elif user_choice == '5':
        if mine_block():
            open_transactions = []
    elif user_choice == '6':
        print(participants)
    else:
        print('Invalid input')
    if not verify_chain():
        print('Invalid block')
        break
    print(get_balance('Mykyta'))
else:
    print('User left')
