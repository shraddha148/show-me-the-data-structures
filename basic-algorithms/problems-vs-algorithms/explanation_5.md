<!--
Problem 5: Autocomplete with Tries

## Explanation

I chose a Trie (Prefix Tree) because it is optimized for prefix-based searching, making it ideal for autocomplete.
Words with common prefixes share the same path, reducing unnecessary comparisons and enabling fast lookups.
Each `TrieNode` stores its child nodes in a dictionary for efficient character lookup and a flag to indicate the end of a word.
The `find()` method traverses the Trie character by character to locate the prefix, while the `suffixes()` method recursively collects all valid word completions below that prefix.

## Time Complexity:

Insert: O(m)
Find Prefix: O(m)
Collect Suffixes: O(k), where k is the number of characters traversed in the subtree.

## Space Complexity:

Trie Storage: (N), where N is the total number of characters in all words.
Recursive Search: O(h), where h is the height of the Trie.

Overall, a Trie provides an efficient and scalable solution for implementing autocomplete.
