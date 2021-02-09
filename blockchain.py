import hashlib
from datetime import datetime

MAX_RANGE = 100000000000

class Block:
    def __init__(self, blocknumber, prev_hash, transactions, nonce):
        self.blocknumber = blocknumber
        prefix_str = "0"*nonce
        self.nonce = nonce
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.time_stamp = datetime.now()
        for nonce in range(MAX_RANGE):
            string_to_hash =  str(blocknumber) + str(prev_hash) + "".join(self.transactions) + str(nonce) + str(self.time_stamp) 
            self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
            if self.block_hash.startswith(prefix_str):
                break
        
prefix = 4
genesis_block = Block(0, "", "", prefix)
genesis_block.block_hash = "0"*prefix + "0"*64

# first_block = Block(1, genesis_block.block_hash, ["Tairoon sent 1 BTC to Kiara", "Nancy sent 11 BTC to Meyer"], prefix)
# print(first_block.block_hash)
# second_block = Block(first_block.block_hash, ["Brian sent 8 BTC to Poppy"])

# print("hash of genesis_block:")
# print(genesis_block.block_hash)
# print("hash of first_block:")
# print(first_block.block_hash)
# print("hash of second_block:")
# print(second_block.block_hash)

print("\nThis program is only for adding blocks to the blockchain.")
transaction_list = []
count = 1
latest_hash = genesis_block.block_hash
while(1):
    sender = input("Enter Sender's name: ")
    receiver = input("Enter Receiver's name: ") 
    amount = input("Enter amount of BTC to transfer: ")
    transaction = sender + " sent " + amount + " BTC to " + receiver
    transaction_list.append(transaction)
    add_more = input("Do you want to add more transactions? Enter Yes/No.: ")
    if (add_more == "Yes"):
        continue
    elif (add_more == "No"):
        new_block = Block(count, latest_hash, transaction_list, prefix)
        latest_hash = new_block.block_hash
        print("New block was created and added to the chain!")
        count +=1
        print(new_block.time_stamp)
        print("Press ctrl+c to terminate program!")