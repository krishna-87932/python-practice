def merge_the_tools(string:str, k:int):
    for i in range(0, len(string), k):
        temp = string[i:i+k]
        seen = ''
        for x in temp:
            if x not in seen:
                seen+=x
        print(seen)
                
    
a = [i for i in range(10)]      
        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)