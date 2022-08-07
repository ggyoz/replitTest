class Solution:
    def reverseBits(self, n: int) -> int:
      
        #n = str(bin(n)[2:])
        
        #print(n)
        #n = n[::-1]
      
        res = 0
        for i in range(32):
            print('i', i)
            
            #bit = (n >> i) & 1
            
            bit = (n >> i)
            print(format(bit & 1, 'b'))
            print(format(bit, 'b'))
            
            #bit = (n >> i) & 1
            #res = res | (bit << (31 - i))
            
        print(res)
        
#         print(str(bin(n)))
        
#         print(f"{format(n, 'd')} ({format(n, 'b')})") 
        
            