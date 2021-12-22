import random
from colorama import init
init()
from colorama import Fore, Back, Style

n = 30
for i in range(0, n) : 
    if i == 0:
        print(Fore.GREEN +' ' *((n-1 - i )//2) +'|'*i)
    elif i % 2 ==0:
         print(' ' *((n-1 - i )//2) +'/'*i)
    else :
        print(Fore.GREEN +' ' *((n-1 - i )//2) +'|'*i)
print("💎🎀🌺")
 #💎🎀🌺🔒🎁🔔💞
init(autoreset=True)
print(Back.RED + "MERRY".center(n+2,' '))
print(Back.GREEN + "CHRISTMAS!".center(n+2, ' '))