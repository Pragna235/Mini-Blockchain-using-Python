from Blockchain import Blockchain

print("____________________________________________________________________________________")
block_one_transactions = {"humidity":23.5,"temp": 33.5}
block_two_transactions = {"humidity":27.5,"temp": 37.5}

iot_blockchain = Blockchain()
iot_blockchain.print_blocks()

a=iot_blockchain.add_block(block_one_transactions)
print('Proof for Transaction1: ',a[0])
b=iot_blockchain.add_block(block_two_transactions)
print('Proof for Transaction2: ',b[0])

iot_blockchain.print_blocks()
iot_blockchain.validate_chain()