import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return (
            f"Block(\n"
            f"  Timestamp: {self.timestamp},\n"
            f"  Data: {self.data},\n"
            f"  Previous Hash: {self.previous_hash},\n"
            f"  Hash: {self.hash}\n"
            f")\n"
        )


class Blockchain:
    """
    A class to represent a blockchain.
    """

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(datetime.datetime.now(), "Genesis Block", "0")
        self.chain.append(genesis)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

    def __repr__(self):
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str


if __name__ == "__main__":

    # Test Case 1: Basic blockchain functionality
    print("Test Case 1")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    # Test Case 2: Empty data (Edge Case)
    print("Test Case 2")
    blockchain2 = Blockchain()
    blockchain2.add_block("")
    print(blockchain2)

    # Test Case 3: Only Genesis Block (Edge Case)
    print("Test Case 3")
    blockchain3 = Blockchain()
    print(blockchain3)