"""Problem 54: Poker hands"""


poker=open('poker.txt')
c=0
for i in range(1000):
    game=poker.readline()[:-1].split(sep=' ')
    for j in range(10):
        if game[j][0]=='A': game[j]=game[j].replace('A','14')
        elif game[j][0]=='K': game[j]=game[j].replace('K','13')
        elif game[j][0]=='Q': game[j]=game[j].replace('Q','12')
        elif game[j][0]=='J': game[j]=game[j].replace('J','11')
        elif game[j][0]=='T': game[j]=game[j].replace('T','10')
    hand_1, player_1=[],0
    if game[0][-1]==game[1][-1]==game[2][-1]==game[3][-1]==game[4][-1]: 
        for j in range(5):
            hand_1.append(int(game[j][:-1]))
        hand_1=sorted(hand_1,reverse=True)
        if hand_1[0]==hand_1[1]+1==hand_1[2]+2==hand_1[3]+3==hand_1[4]+4:
            if hand_1[0]==14: player_1=9
            else: player_1=8
        else:
            player_1=5
    else:
        for j in range(5):
            hand_1.append(int(game[j][:-1]))    
        hand_1=sorted(hand_1,reverse=True)
        pairs_1=[]
        for j in range(4):
            if hand_1[j]==hand_1[j+1]:
                pairs_1.append(j)
                pairs_1.append(j+1)
        pairs_1=sorted(set(pairs_1))
        if pairs_1==[]:
            if hand_1[0]==hand_1[1]+1==hand_1[2]+2==hand_1[3]+3==hand_1[4]+4:
                player_1=4
            else:
                player_1=0
        elif len(pairs_1)==2:
            player_1=1
        elif len(pairs_1)==3:
            player_1=3
        elif len(pairs_1)==5:
            player_1=6                 
        else:
            if hand_1[pairs_1[0]]==hand_1[pairs_1[1]]==hand_1[pairs_1[2]]==hand_1[pairs_1[3]]:
                player_1=7
            else:
                player_1=2

    hand_2, player_2=[],0
    if game[5][-1]==game[6][-1]==game[7][-1]==game[8][-1]==game[9][-1]: 
        for j in range(5,10):
            hand_2.append(int(game[j][:-1]))
        hand_2=sorted(hand_2,reverse=True)
        if hand_2[0]==hand_2[1]+1==hand_2[2]+2==hand_2[3]+3==hand_2[4]+4:
            if hand_2[0]==14: player_2=9
            else: player_2=8
        else:
            player_2=5
    else:
        for j in range(5,10):
            hand_2.append(int(game[j][:-1]))    
        hand_2=sorted(hand_2,reverse=True)
        pairs_2=[]
        for j in range(4):
            if hand_2[j]==hand_2[j+1]:
                pairs_2.append(j)
                pairs_2.append(j+1)
        pairs_2=sorted(set(pairs_2))
        if pairs_2==[]:
            if hand_2[0]==hand_2[1]+1==hand_2[2]+2==hand_2[3]+3==hand_2[4]+4:
                player_2=4
            else:
                player_2=0
        elif len(pairs_2)==2:
            player_2=1
        elif len(pairs_2)==3:
            player_2=3
        elif len(pairs_2)==5:
            player_2=6                 
        else:
            if hand_2[pairs_2[0]]==hand_2[pairs_2[1]]==hand_2[pairs_2[2]]==hand_2[pairs_2[3]]:
                player_2=7
            else:
                player_2=2                


    if player_1>player_2:
        c+=1
    elif player_1==player_2:
        if pairs_1!=[]:
            for m,n in zip(pairs_1,pairs_2):
                if hand_1[m]!=hand_2[n]:
                    if hand_1[m]>hand_2[n]:c+=1
                    break
                hand_1[m]=hand_2[n]=0
            else:
                hand_1,hand_2=sorted(hand_1,reverse=True),sorted(hand_2,reverse=True)
                for j in range(len(pairs_1)):
                    if hand_1[j]!=hand_2[j]:
                        if hand_1[j]>hand_2[j]:c+=1
                        break
        else:
            for j in range(5):
                if hand_1[j]!=hand_2[j]:
                    if hand_1[j]>hand_2[j]:c+=1
                    break
print(c)
