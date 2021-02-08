import hashlib
import time

MAX_RANGE = 10000000000000000000000000000

def hash_gen(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def mining(Block_Number, transactions, previous_hash, nonce):
    prefix_str = '0'*nonce
    for nonce in range(MAX_RANGE):
        hash_str = str(Block_Number) + transactions + previous_hash + str(nonce)
        new_hash = hash_gen(hash_str)
        if new_hash.startswith(prefix_str):
                return new_hash

    print ('Increase Range!')
    return
            

prefix_zero = 6
start = time.time()
print("Mining Started")
print(mining(9,"Austin sends 10 BTC to Zara, Medusa sends 20 BTC to Zeus", ((prefix_zero*'0')+'2a90a5765df425a4898b542d249852a7a5d599cd6dce4dfdbe0f195b10c65a65'), prefix_zero))
print("Mining took", time.time()-start, "seconds")