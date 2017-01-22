file = open('rosalind_gc.txt', 'r')
txtdata = file.readlines()
data = []
for i in txtdata:
    appendtodata = i.strip('\n')
    data.append(appendtodata)
###extract the txt data and remove the '\n' for each item in the list


fastanames = []
fastanamesindexes = []
dataindexes = []
for i in data:
    dataindexes.append(data.index(i))
    if '>' in i:
        fastanames.append(i)
for i in fastanames:
    index = data.index(i)
    fastanamesindexes.append(index)
###the above block of code to identify the names of the sequences and to locate
#the names in the data list via their corresponding indexes this will be
#important for sorting between name info and actual corresponding sequencing info
#I will be manipulating the index lists while conserving the original data set list
#

dict ={}
for i in fastanamesindexes:             ###scan through all of the name indexes list
                                        #this calls the name of dict key that I want to
                                        #add seq data to for one cycle of the for loop
                                        ###
    y = data[i]                         #call the name by index in the original data set
    dict[y]={'seq':'', 'GCcontent':''}  #the general structure of the embedded dictionary
                                        #and it will iterate through each seq name
                                        ###
    dataindexes.pop(0)                  ###gets rid of first list item called index from
                                        #dataindexes, in this case it is the name indexes
                                        #for origanl data we do not want the first name to#
                                        #iterate in the upcoming for loop because within
                                        #that loop, name related indexes break out of the
                                        #for loop and then I do not end up inserting seq
                                        #data into the dict
                                        ###
    countforpop = 0                     #variable that is used to count the number of loops
                                        #in the for loop below it. This becomes useful in
                                        #getting rid of the data indexes that are correlated
                                        #with seqdata. Think of it as scratching off an item
                                        #in a to do list, you do not want to redo the task
    for i in dataindexes:               #iterate through the remaining data indexes that have
                                        #not been popped off yet
        if i not in fastanamesindexes:  #this checks if an index corresponds to a seq name
                                        #which is not what we want to add to the 'seq section'
                                        #for the name
                                        ###
            dict[y]['seq'] = (dict[y]['seq']) + data[i]
            countforpop +=1             #each time a seq item gets tacked onto the seq key the
                                        #the counter increases by 1 becuase I need to count how
                                        #how many items in the list I need to get rid of/ cross
                                        #off my list
            continue
        if i in fastanamesindexes:
            for i in range(0,countforpop):
                dataindexes.pop(0)      ###the for loop iterates the same number of for loop
                                        #cycles. I do this only when an index that correlates to
                                        #a name gets interating in the for loop because I want
                                        #to move onto the next name and overarching dict key
                                        #which will be the next seq name. Adding the pop function
                                        #in the 'if' condition of the for loop will mess up the
                                        #iteration and skip all around. It is hard to explain.
            break                       #once a name index is detected then I kick out of the
                                        #second for loop and go back to the original for loop
                                        ###


for i in dict:
    X = i
    sequencecalc = dict[i]['seq']
    splitseqcalc = list(sequencecalc)
    nucleotides = {'A': 0,'T':0,'C':0, 'G':0}
    for i in splitseqcalc:
        if i in nucleotides:
            nucleotides[i] += 1
    totalnuc = int(nucleotides['A']) +int(nucleotides['T'])+ int(nucleotides['C'])+ int(nucleotides['G'])
    GC = int(nucleotides['C'])+ int(nucleotides['G'])
    GCpercent = GC/totalnuc
    dict[X]['GCcontent'] = GCpercent


#use max() function
GClist =[]
for i in dict:
    percent = dict[i]['GCcontent']
    GClist.append(percent)
maxGC = max(GClist)
for i in dict:
    Y = dict[i]['GCcontent']
    if Y == maxGC:
        nameofmaxGC = i
        nameofmaxGC = nameofmaxGC.strip('>')
print(nameofmaxGC)
print(maxGC*100)
