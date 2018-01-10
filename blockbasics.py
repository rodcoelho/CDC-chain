# Allows for mining of the coin

# from flask import Flask, request, render_template
# node = Flask(__name__)


# Store transactions by this node in a list
#
# this_node_transactions = []
#
#
# @node.route('/')
# def home():
#     return render_template('home.html')
#
# @node.route('/txion', methods = ['POST'])
# def transaction():
#     if request.method == 'POST':
#         submitted_from = request.form['from']
#         submitted_to = request.form['to']
#         submitted_amount = request.form['amount']
#         return "Transaction submission successful"
#
# # Simple Proof-of-Work algorithm
# # To create a new block, a miner’s computer will have to increment a number.
# # When that number is divisible by 9 and the proof number of the last block,
# # a new coin block will be mined and the miner will be given a brand new coin.
#
# miner_address = "some_address_TBD"
#
# def proof_of_work(last_proof):
#     incrementor = last_proof + 1
#     while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
#         incrementor += 1
#     return incrementor
#
# @node.route('/mine')
# def mine():
#     # get last PoW
#     last_block = blockchain[len(blockchain) - 1]
#     last_proof = last_block.data['proof-of-work']
#     proof = proof_of_work(last_proof)
#     # reward minder for doing proof
#     this_node_transactions.append(
#         {"from": "network", "to": miner_address, "amount": 1}
#     )
#
#     #now create new block
#     new_block_data = {
#         "proof-of-work":proof,
#         "transactions": list(this_node_transactions)
#     }
#     new_block_index = last_block.index + 1
#     new_block_timestamp = this_timestamp = date.datetime.now()
#     last_block_hash = last_block.hash
#
#     # empty the trasaction list
#     this_node_transactions[:] = []
#     #now create the new block
#     mined_block = Block(
#         new_block_index,
#         new_block_timestamp,
#         new_block_data,
#         last_block_hash
#     )
#     blockchain.append(mined_block)
#     return json.dumps({
#         "index": new_block_index,
#         "timestamp": str(new_block_timestamp),
#         "data": new_block_data,
#         "hash": last_block_hash
#     })
#
# @node.route('/blocks', methods = ['GET'])
# def get_blocks():
#     chain_to_send = blockchain
#     # convert blocks in to dicts to later send as json objects
#     for block in chain_to_send:
#         block_index = str(block.index)
#         block_timestamp = str(block.timestamp)
#         block_data = str(block.data)
#         block_hash = block.hash
#         block = {
#             "index": block_index,
#             "timestamp": block_timestamp,
#             "data": block_data,
#             "hash": block_hash
#         }
#     # Send the chain to whomever requested it
#     return json.dumps(chain_to_send)
#
# node.run()