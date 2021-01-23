# CSCO leetcode

## 468. Validate IP Address
- [python implementation](./lc468_valid_IP_addr.py)
- String process in Python
    - `str.startswith(str)`, check if the string starts with 
    - `str.split(token)` split the string into several elements in a list with a token
- `list.count()` to search for the number of element in the list

## 48 Rotate Image
- [python implementation](./lc48_rotate_iamge.py)
- First swap the horizontal with center row as the axis 
- Then swap the diagonal from top to up

## 191 Number of 1 Bits
- [python implementation](./lc191_num_1_bits.py)
- Use AND bit operation to get the last bit 
- Use >> to right shift by 1 to next bit as the last bit

## 1235 Maximum Profit in Job Scheduling
- [python implementation](./lc1235_max_profit_job_schedule.py)
- Understand the what DP means in this case
- Know how to use `bisect.bisect` module with this [notebook](./biset_module.ipynb)
- How to find the earlier endtime than current start time with the highest profit

