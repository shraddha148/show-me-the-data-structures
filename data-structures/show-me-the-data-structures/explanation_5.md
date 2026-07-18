## Reasoning Behind Decisions:
A list is used to store the blockchain because blocks are added sequentially.
Each block stores its timestamp, data, previous hash, and its own SHA-256 hash.
The blockchain starts with a Genesis Block, which is the first block and has a previous hash of "0".
Whenever a new block is added, its previous_hash is set to the hash of the last block in the chain, ensuring that all blocks are linked together.
SHA-256 hashing is used to uniquely identify each block and help maintain the integrity of the blockchain.
Edge cases such as adding a block with empty data and a blockchain containing only the Genesis Block are included in the test cases.

## Time Efficiency:
Creating the Genesis Block: O(1)
Adding a new block: O(1), since the previous block is accessed directly from the end of the list and the hash calculation is constant time for small block data.
Printing the blockchain: O(n), where n is the number of blocks.

## Overall Time Complexity:

add_block() → O(1)
Printing the blockchain → O(n)
Space Efficiency:
Each new block is stored in the blockchain list.
The total memory used grows linearly with the number of blocks.

## Overall Space Complexity: O(n)

where n is the total number of blocks stored in the blockchain.