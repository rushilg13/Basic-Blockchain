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

print("hash of genesis_block:")
print(genesis_block.block_hash)
print("hash of first_block:")
print(first_block.block_hash)
print("hash of second_block:")
print(second_block.block_hash)

