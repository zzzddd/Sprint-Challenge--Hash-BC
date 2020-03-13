What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

Accessing an item at a certain index in an array is O(1). Adding or removing from the front is O(n) and adding or removing from the back is O(1) best case or O(n) worst case.

What is the worse case scenario if you try to extend the storage size of a dynamic array?

If there isn't enough contiguous memory at the current address, the system will find a new address with sufficient space and copy everything over. Time complexity is O(n)

Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

Each block contains data about transactions (sender, recipient, etc.). Each block also contains a hash of the previous block. This is the 'chain' part of it. It ensures that no one can go back and edit blocks in the chain. The data is organized linearly, in a chain.
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Creating a new block requires adding something (a number, another hash, etc.) to the last block and hashing them together until you find a hash with a certain amount of leading zeroes. This is purposefully difficult and time intensive. This makes it basically impossible to go back and change data in the change, as any change to a block would change the hash entirely. However, if someone were to somehow gain control of 51% of the mining on a certain blockchain, they could prevent transactions from being verified, prevent other people from mining, and even reverse transactions that occurred while they were in control.
Project Set Up