#! usr/bin/env python3

import datetime as date
import json

import hashlib as hasher

class Chain:
    def __init__(self):
        self.apponly = []

    def addinfo(self,data):
        self.apponly.append(data)

    def printchain(self):
        print(self.apponly)

    def size(self):
        return len(self.apponly)

class Block:
    def __init__(self,index,timestamp,data,previous_hash,
                 doctorID,outbreak,patientID,zipcode,
                 symp1,symp2,symp3,days):
        self.index              = index
        self.timestamp          = timestamp
        self.data               = data
        self.previous_hash      = previous_hash
        self.doctorID           = doctorID
        self.outbreak           = outbreak
        self.patientID          = patientID
        self.zipcode            = zipcode
        self.symp1              = symp1
        self.symp2              = symp2
        self.symp3              = symp3
        self.days               = days
        self.hash               = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.doctorID).encode('utf-8') +
                   str(self.outbreak).encode('utf-8') +
                   str(self.patientID).encode('utf-8') +
                   str(self.zipcode).encode('utf-8') +
                   str(self.symp1).encode('utf-8') +
                   str(self.symp2).encode('utf-8') +
                   str(self.symp3).encode('utf-8') +
                   str(self.days).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        hex = sha.hexdigest()
        chain.addinfo(hex)
        return hex

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0",
                 12345, 00, 00, 94125, 'cough', 'sneeze', 'fart', 0)

def next_block(last_block,doctorID,outbreak,
               patientID,zipcode,symp1,
               symp2,symp3,days):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey I am block # " + str(this_index)
    this_hash = last_block.hash
    return Block(index=this_index,timestamp=this_timestamp,data=this_data,previous_hash=this_hash,
                 doctorID=doctorID,outbreak=outbreak,patientID=patientID,zipcode=zipcode,
                 symp1=symp1,symp2=symp2,symp3=symp3,days=days)

# Create blockchain and genesis
chain = Chain()
blockchain=[create_genesis_block()]
previous_block = blockchain[0]

while True:
    doctorID        = input("What is your Unique Physician Identification number?\n")
    outbreak        = input("What Outbreak ID would you like to PERMANENTLY log to the OutbreakChain?\n")
    patientID       = input("Type Patient's ID\nFirst_Last_DOB\nEx: John_Doe_09121992\n")
    zipcode         = input("What is the current zipcode?\n")
    symp1           = input("First symptom: ")
    symp2           = input("Second symptom: ")
    symp3           = input("Third (last) symptom: ")
    days            = input("Number of infected days: ")
    block_to_add    = next_block(previous_block,doctorID=doctorID,outbreak=outbreak,
                                 patientID=patientID,zipcode=zipcode,symp1=symp1,
                                 symp2=symp2,symp3=symp3,days=days)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("\nMD-{} has reported Outbreak-{} to the public blockchain".format(doctorID,outbreak))
    print("Hash {}".format(block_to_add.hash))
    print("Time: {}".format(block_to_add.timestamp))
    print("Block {} has been added to the blockchain\n".format(block_to_add.index))
    print("Current chain: ")
    chain.printchain()