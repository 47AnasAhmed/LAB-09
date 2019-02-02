print('Anas Ahmed')
print('18B-116-cs')
print('LAb 09')
print('P.EX 03')

def duplicate(file_name):
    count = 0
    infile = open(file_name,'r')
    words = infile.read()
    lst = words.split()
    infile.close()
    duplicates = {}
    for word in lst:
        count = words.count(word) # count occurrences of each word
        if count > 1:
            duplicates[word] = count
    if duplicates:
        print (duplicates)
        return True
    return False
        
def uplicate(fname):

    with open(fname, 'r') as f:
        text = f.read() # auto closes file after reading

    split_text = text.split()# create list of all the words
    
    duplicates = {}
    for word in split_text:
        count = text.count(word) # count occurrences of each word
        if count > 1:
            duplicates[word] = count
    if duplicates:
        print(duplicates)
        return True
    return False           
    

