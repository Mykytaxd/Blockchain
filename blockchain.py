blockchain = []


def get_last_block_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1.00]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input('Enter transaction amount'))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = float(input('Enter transaction amount'))
add_value(transaction_amount=tx_amount,
          last_transaction=get_last_block_value())

tx_amount = float(input('Enter transaction amount'))
add_value(tx_amount, get_last_block_value())

print(blockchain)
