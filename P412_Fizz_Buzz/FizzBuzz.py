class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    
        #generate multiples of 3 less than n
        
        i = 1
        mult_3 = 3
        mult_5 = 5
        
        memo = {}
        
        while mult_3 <= n:
            mult_3 = i*3
            memo[mult_3] = "Fizz"
            i += 1
        
        j = 1
        
        #generate multiples of 5 less than n
        while mult_5 <= n:
            mult_5 = j*5
            
            
            if mult_5 in memo:
                memo[mult_5] += "Buzz"
            else:
                memo[mult_5] = "Buzz"
            
            j += 1
            
            
        k = 1
        ans = []
        while k <= n:
            
            if k in memo:
                ans.append(memo[k])
            else:
                ans.append(k)

            k += 1
                
        
        return ans
