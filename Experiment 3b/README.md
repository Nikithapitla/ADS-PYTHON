Experiment 3b:Deletion in Btree


Aim of the Experiment:
Deleting an element on a B-tree consists of three main events:
searching the node where the key to be deleted exists, deleting the key and balancing the tree if required.

Procedure:

1.A node can have a maximum of m children. (i.e. 3)
2.A node can contain a maximum of m - 1 keys. (i.e. 2)
3.A node should have a minimum of ⌈m/2⌉ children. (i.e. 2)
4.A node (except root node) should contain a minimum of ⌈m/2⌉ - 1 keys. (i.e. 1)
