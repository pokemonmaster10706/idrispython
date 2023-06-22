def capitalise_odd_indices(l):
    newl = []
    for i in l:
        newstr = ''
        for j in range(0,len(i)):
            if j%2 == 0:
                newstr += i[j]
            else:
                newstr += i[j].upper()
        newl.append(newstr)
    return newl

testl = ['jajaja','hahahah','hohoh','hehehe']

output = capitalise_odd_indices(testl)
print(output)
