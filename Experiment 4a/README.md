Experiment 4a
Aim of the experiment - Write a program to perform the following operations:
4a)Insert an element into a Min-Max heap

procedure for the experiment Insertion of a key
Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. 
If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.
