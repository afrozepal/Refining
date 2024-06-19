class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        ch=1
        # print(len(s))
        i=0
        while i < (len(s)-1):
            print("num is " , num ," i is " ,i)
            if (s[i]=="I" and s[i+1]=="V"):
                i+=2
                num+=4
                ch=0
            elif (s[i]=="I" and s[i+1]=="X"):
                i+=2
                num+=9
                ch=0
            elif (s[i]=="X" and s[i+1]=="L"):
                i+=2
                num+=40
                ch=0
            elif (s[i]=="X" and s[i+1]=="C"):
                i+=2
                num+=90
                ch=0
            elif (s[i]=="C" and s[i+1]=="D"):
                i+=2
                num+=400
                ch=0
            elif (s[i]=="C" and s[i+1]=="M"):
                i+=2
                num+=900
                ch=0
                # print("num is " , num ," u i is " ,i)
            elif(s[i]=="I"):
                num+=1
                i+=1
            elif(s[i]=="V"):
                num+=5
                i+=1
            elif(s[i]=="X"):
                num+=10
                i+=1
            elif(s[i]=="L"):
                num+=50
                i+=1
            elif(s[i]=="C"):
                num+=100
                i+=1
            elif(s[i]=="D"):
                num+=500
                i+=1
            elif(s[i]=="M"):
                num+=1000
                i+=1
            # print("ss " , i+2)
            if (i+1)==len(s):
                ch=1

        if ch==1:
            # print("here")
            i=len(s)-1
            if(s[i]=="I"):
                num+=1
            elif(s[i]=="V"):
                num+=5
            elif(s[i]=="X"):
                num+=10
            elif(s[i]=="L"):
                num+=50
            elif(s[i]=="C"):
                num+=100
            elif(s[i]=="D"):
                num+=500
            elif(s[i]=="M"):
                num+=1000
        print(num)
        return num