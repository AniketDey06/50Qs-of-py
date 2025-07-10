# In a game of tossing a coin, you want to know the number of times getting 'Head' and 'Tail'. You keep
# the record as '1' (one) for getting 'Head' and '0' (zero) for 'Tail'. Write a program to perform the above
# task. Suppose, you have tossed a coin for 20 times in this game.

h=0
t=0
i=0

while i < 20:
    ch = int(input('Enter ''1'' (one) for getting ''Head'' and ''0'' (zero) for ''Tail''- ' ))

    if(ch==1):
        h += 1
    elif(ch==0):
        t += 1
        
    i+=1

print('Number of heads is - ', h)
print('Number of tails is - ', t)

# Code Compiled By - Aniket Dey