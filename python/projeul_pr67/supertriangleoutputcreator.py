file=open('supertriangle.txt','r')
fileoutput=open('supertriangleoutput.txt','w')

vertical, c = [], 0
for i in file:
    i=i.replace('\t','')
    i=i.replace('\n',' \n')
    c, l = 0, len(i)
    try:
        while i[c]==' ' and c<l:
            c+=1
        i=i.replace(' ','',c)
        fileoutput.write(i)
    except:
        pass
        
