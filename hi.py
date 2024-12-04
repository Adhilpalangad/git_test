def main():
    while True:
        print("Menu \n 1)remove i th \n 2) first half to upper \n 3)first and last upper \n 4)print even words \n 5)Check the Palindrom \n 6)Reverse the string" )
        
        ch = int(input("enter the choice"))
        if(ch==1):
            remove()
        elif(ch==2):
            half()
        elif(ch==3):
            first()
        elif(ch==4):
            even()
        elif(ch==5):
            palindrom()
        elif(ch==6):
            reverse()
        else:
            print("invalid choice")
            break
def remove():
    s = input("enter the string")
    i = int(input("enter the position"))
    word = s[:i]+s[i+1:]
    print(word)
def half():
    s = input("enter the string")
    length = len(s)//2
    word = s[:length].upper()+s[length:]
    print(word)
def first():
    s =input("enter the string")
    word = s[:1].upper()+s[1:-1]+s[-1:].upper()
    print(word)  
def even():
    s = input("enter the string")
    word = s.split(" ")
    print(word)
    for words in word:
        if (len(words))%2 == 0:
            print(words)
def palindrom():
    s = input("enter the string")
    pal = s[::-1]
    if(s==pal):
        print (pal)
def reverse():
    s=input("enter the string")
    word = s[::-1]
    print(word)
main()