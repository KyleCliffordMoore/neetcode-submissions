/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {

public:
    Node* copyRandomList(Node* head) {
        
        // If empty list
        if (!head)
            return head;

        unordered_map<Node*, Node*> oldToNew;

        // Make copies of all the node values and create a
        // map that links the old nodes to the new nodes.
        Node* oldCurr = head;
        Node* newCurr = nullptr;
        while (oldCurr) {

            newCurr = new Node(oldCurr->val);

            // update oldToNew (So we can do randoms on 2nd pass)
            oldToNew[oldCurr] = newCurr;

            newCurr = newCurr->next;
            oldCurr = oldCurr->next;
        }

        // Update the next and random of the new nodes
        oldCurr = head;
        while (oldCurr) {
            newCurr = oldToNew[oldCurr];

            newCurr->next   = oldToNew[oldCurr->next];
            newCurr->random = oldToNew[oldCurr->random];

            oldCurr = oldCurr->next;
        }

        return oldToNew[head];
    }
};
