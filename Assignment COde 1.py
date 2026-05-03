import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()  # generate hash


# -------- Blockchain Class --------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # start with first block

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")  # first block

    def add_block(self, data):
        last_block = self.chain[-1]                         # get last block
        new_block = Block(len(self.chain), data, last_block.hash)  # create new block
        self.chain.append(new_block)                        # add to chain

    def display_chain(self):
        for block in self.chain:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():   # check hash
                return False

            if curr.previous_hash != prev.hash:      # check link
                return False

        return True



bc = Blockchain()   # create blockchain

# add blocks
bc.add_block("Alice pays Bob $50")
bc.add_block("Bob pays Charlie $30")
bc.add_block("Charlie pays Dave $20")
bc.add_block("Dave pays Eve $10")

# show blockchain
bc.display_chain()

# check validity
print("Valid:", bc.is_valid())

 #Tampering
bc.chain[2].data = "Bob pays Charlie $9999"   # change data

# check again
print("Valid after tampering:", bc.is_valid())

# show chain again
bc.display_chain()