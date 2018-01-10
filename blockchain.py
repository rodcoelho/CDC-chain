#! usr/bin/env python3

import datetime as date
import json

import hashlib as hasher

class Chain:
    def __init__(self):
        self.apponly = []

    def addinfo(self,data):
        self.apponly.append(data)

    def size(self):
        return len(self.apponly)

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey I am block # " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create blockchain and genesis
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
chain = Chain

while True:
    doctorID = input("What is your Unique Physician Identification number?\n")
    outbreak = input("What Outbreak ID would you like to PERMANENTLY log to the OutbreakChain?\n")
    patientID = input("Type Patient's ID\nFirst_Last_DOB\nEx: John_Doe_09121992\n")
    zipcode = input("What is the current zipcode?\n")
    symp1 = input("First symptom: ")
    symp2 = input("Second symptom: ")
    symp3 = input("Third (last) symptom: ")
    days = input("Number of infected days: ")

# for i in range(10):
#     block_to_add = next_block(previous_block)
#     blockchain.append(block_to_add)
#     previous_block = block_to_add
#     print("Block {} has been added to the blockchain".format(block_to_add.index))
#     print("Hash {}".format(block_to_add.hash))
#     print("Time: {}".format(block_to_add.timestamp))
#     print()
