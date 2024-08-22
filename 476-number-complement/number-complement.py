class Solution:
    def findComplement(self, num: int) -> int:
        # given
        listnum = bin(num)[2:]

        newList =""

        for stt in listnum:
            if stt == '1':
                newList+='0'
            elif stt == '0':
                newList+='1'

        
        return int(newList, 2)
        