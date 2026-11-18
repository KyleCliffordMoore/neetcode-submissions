/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {

private:
    size_t getLength(ListNode* head) {
        size_t count{};
        while (head) {
            head = head->next;
            ++count;
        }
        return count;
    }

public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        size_t target = getLength(head) - n;
        std::cout << target << '\n';

        // Edge Case: Remove Head
        if (target == 0)
            return head->next;

        // Normal Case
        ListNode* curr = head;
        while (curr) {

            if (target == 1) {
                ListNode* next1 = curr->next;
                ListNode* next2 = next1->next;

                curr->next = next2;
                return head;
            }

            --target;
            curr = curr->next;
        }

        // This should never happen
        return nullptr;

    }
};
