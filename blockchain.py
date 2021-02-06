import hashlib

class Block:
    def __init__(self, prev_hash, transactions):
        self.transactions = transactions
        self.prev_hash = prev_hash
        string_to_hash = "".join(transactions) + prev_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

genesis_block = Block("Chancellor on Brink of Second Bailout for Banks", ["Austin sent 1 BTC to Skeeter", "Zara sent 5 BTC to James"])
first_block = Block(genesis_block.block_hash, ["Tairoon sent 1 BTC to Kiara", "Nancy sent 11 BTC to Meyer"])
second_block = Block(first_block.block_hash, ["Brian sent 8 BTC to Poppy"])

# print("hash of genesis_block:")
# print(genesis_block.block_hash)
# print("hash of first_block:")
# print(first_block.block_hash)
# print("hash of second_block:")
# print(second_block.block_hash)

print("\nThis program is only for adding blocks to the blockchain.")
while(1):
    transaction_list = []
    latest_hash = genesis_block.block_hash
    sender = input("Enter Sender's name: ")
    receiver = input("Enter Receiver's name: ") 
    amount = input("Enter amount of BTC to transfer: ")
    transaction = sender + " sent " + amount + " BTC to " + receiver
    transaction_list.append(transaction)
    add_more = input("Do you want to add more transactions? Enter Yes/No.: ")
    if (add_more == "Yes"):
        continue
    elif (add_more == "No"):
        new_block = Block(latest_hash, transaction_list)
        latest_hash = new_block.block_hash
        print("New block was created and added to the chain!")
        print("Press ctrl+c to terminate program!")