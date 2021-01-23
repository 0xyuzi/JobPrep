class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3:
            return self.check_ipv4(IP)
        elif IP.count(":") == 7:
            return self.check_ipv6(IP)
        else:
            return "Neither"
        
    
    def check_ipv4(self, IP):
        nums = IP.split(".")
        print(nums)
        # len > 4, or len <1: false
        # no leading zero, should be all digits
        for num in nums:
            if len(num) < 1 or len(num)>4:
                return "Neither"
            if not num.isdigit():
                return "Neither"
            if len(num) > 1 and num.startswith("0"):
                return "Neither"
            if int(num)>255:
                return "Neither"
        return "IPv4"
    
    def check_ipv6(self, IP):
        valid_str = "0123456789abcdefABCDEF"
        nums = IP.split(":")
        print(nums)
        for num in nums:
            if len(num) < 1 or len(num) > 4:
                return "Neither"
            
            for ch in num:
                if ch not in valid_str:
                    return "Neither"
        
        return "IPv6"
        
        