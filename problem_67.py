class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aDecimal = int(a, 2)
        bDecimal = int(b, 2)
        summa = bin(aDecimal + bDecimal).lstrip("0b")
        if summa == "":
            return "0"
        return summa

    def addBinarySlow(self, a: str, b: str) -> str:
        aList = [i for i in a]
        bList = [i for i in b]
        carry = False
        res = []
        while len(aList) > 0 or len(bList) > 0:
            if len(aList) > 0:
                currentA = aList.pop()
            else:
                currentA = "0"
            if len(bList) > 0:
                currentB = bList.pop()
            else:
                currentB = "0"

            if not carry:
                if currentA == "0" and currentB == "0":
                    res.insert(0, "0")
                    carry = False
                elif currentA == "0" and currentB == "1":
                    res.insert(0, "1")
                    carry = False
                elif currentA == "1" and currentB == "0":
                    res.insert(0, "1")
                    carry = False
                else:
                    res.insert(0, "0")
                    carry = True
            elif carry:
                if currentA == "0" and currentB == "0":
                    res.insert(0, "1")
                    carry = False
                elif currentA == "0" and currentB == "1":
                    res.insert(0, "0")
                    carry = True
                elif currentA == "1" and currentB == "0":
                    res.insert(0, "0")
                    carry = True
                else:
                    res.insert(0, "1")
                    carry = True

        if carry:
            res.insert(0, "1")

        return "".join(res)
