from blockbasics import create_genesis_block, next_block

# Create blockchain and genesis
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

for i in range(10):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block {} has been added to the blockchain".format(block_to_add.index))
    print("Hash {}".format(block_to_add.hash))
    print("Time: {}".format(block_to_add.timestamp))
    print()