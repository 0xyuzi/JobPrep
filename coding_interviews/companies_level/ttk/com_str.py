from collections import defaultdict
def com_str(nums1, nums2):
    if not nums1 or not nums2:
        return []

    counter_1 = defaultdict(int)
    counter_2 = defaultdict(int)
    for num in nums1:
        counter_1[num] += 1 

    for num in nums2:
        if num in counter_1:
            counter_2[num] += 1

    
    res = []

    for key in counter_2.keys():
        num1, num2 = counter_1[key], counter_2[key]
        val = min(num1, num2)

        res += [key]*val 

    return sorted(res)


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = []

    print(com_str(nums1, nums2)) 

    

    