
class Solution():
    def convertTemperature(self, celsius):
        
        return [celsius + 273.15, (celsius * 1.80) + 32.00]
                
          
s = Solution()
celsius = 122.11

print(s.convertTemperature(celsius))


