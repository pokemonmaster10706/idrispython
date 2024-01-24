with open('textfile.txt','r') as file:
    lines = file.readlines()
    with open('textfile2.txt','a') as file2:
        for i in lines:
            if (i.lower()).startswith('a'):continue
            else:file2.write(i);print(f'the line \n"{i}"\n was added\n')