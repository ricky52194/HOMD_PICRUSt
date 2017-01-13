#Input is 16s_table.txt
#Creates a table with HOMD Seq ID with 16s Gene Counts

from collections import Counter

def main():
    newList = []
    with open("16s_table.txt") as f:
        for line in f:
            lineSplit = line.split()
            x = lineSplit[1]
            newList.append(x)
        cnt = Counter()
    for i in newList:
        cnt[i] += 1
    countList = cnt.items()
    for pair in countList:
        print pair[0] + "\t" + str(pair[1])
        
main()
