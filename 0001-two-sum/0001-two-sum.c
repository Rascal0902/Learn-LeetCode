/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(*returnSize * sizeof(int));

    for(int i = 0; i < numsSize; i++){
        for(int j = i + 1; j < numsSize; j++){
            if (i != j && nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    
    *returnSize = 0;
    return NULL;
}