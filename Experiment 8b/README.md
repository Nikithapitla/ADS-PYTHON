Experiment 8

Aim of the program:Deletion in red-black tree.


procedure:

Following are detailed steps for deletion.
1) Perform standard BST delete. When we perform standard delete operation in BST, 
    we always end up deleting a node which is an either leaf or has only one child
    (For an internal node, we copy the successor and then recursively call delete 
    for successor, successor is always a leaf node or a node with one child).
    So we only need to handle cases where a node is leaf or has one child.
   Let v be the node to be deleted and u be the child that replaces v 
   (Note that u is NULL when v is a leaf and color of NULL is considered as Black).
2) Simple Case: If either u or v is red, we mark the replaced child as black (No change in black height).
   Note that both u and v cannot be red as v is parent of u and two consecutive reds are not allowed in red-black tree. 
 3) If Both u and v are Black.
3.1) Color u as double black.  Now our task reduces to convert this double black to single black.
    Note that If v is leaf, then u is NULL and color of NULL is considered black. So the deletion of a black leaf also causes a double black.
3.2) Do following while the current node u is double black, and it is not the root. Let sibling of node be s. 
   If sibling s is black and at least one of sibling’s children is red, perform rotation(s). Let the red child of s be r. 
    This case can be divided in four subcases depending upon positions of s and r.
…………..(i) Left Left Case (s is left child of its parent and r is left child of s or both children of s are red). This is mirror of right right case shown
       in below diagram.
…………..(ii) Left Right Case (s is left child of its parent and r is right child). This is mirror of right left case shown in below diagram.
…………..(iii) Right Right Case (s is right child of its parent and r is right child of s or both children of s are red) 
