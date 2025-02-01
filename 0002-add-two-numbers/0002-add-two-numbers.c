/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* result = (struct ListNode*)malloc(sizeof(struct ListNode));
    int carrier = 0, add = 0, x , y;
    struct ListNode* temp = result;
    while(true){
        if(l1 != NULL){
            x = l1 -> val;
        }
        else{
            x = 0;
        }
        if(l2 != NULL){
            y = l2 -> val;
        }
        else{
            y = 0;
        }
        add = x + y + carrier;
        temp -> val = add % 10;
        carrier = add / 10;

        if(((l1 != NULL && l1 -> next == NULL) || l1 == NULL) && ((l2 != NULL && l2 -> next == NULL) || l2 == NULL) && carrier == 0){
            temp -> next = NULL;
            break;
        }
        else{
            if(l1 != NULL){
                l1 = l1 -> next;
            }
            if(l2 != NULL){
                l2 = l2 -> next;
            }
            temp -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
            temp = temp -> next;
        }
    }
    
    return result;
}