def create_table():
    bacteriaList = []
    enzymeList = []
    data = []
    #open file with bacteria abbreviations and names
    with open("names.txt") as rows:
        for bacteria in rows:
            bacteria = bacteria.split("\t")
            shortName = bacteria[0]
            #open file with name mapping in order to match correct seq ID with bacteria abbreviation
            with open("NameMap2.txt") as nameMap:
                for line in nameMap:
                    lineSplit = line.split("\t")
                    checkShort = lineSplit[1].replace("\n","")
                    if(shortName == checkShort):
                        shortName = lineSplit[0]
                bacteriaList.append(shortName)
    #open file with list of all enzymes found within files
    with open("enzyme_columns.txt") as col:
        for enzyme in col:
            enzyme = enzyme.replace("\n","")
            enzymeList.append(enzyme)
    #open each count file and get counts of each enzyme into a list
    #then append that list into another list
    with open("count_files.txt") as countfiles:
        for File in countfiles:
            File = File.replace("\n","")
            counts = []
            with open(File) as currentfile:
                for line in currentfile:
                    lineSplit = line.split("\t")
                    num = lineSplit[1].replace("\n","")
                    counts.append(num)
                data.append(counts)
                counts = []
    print "\t", 
    for enzyme in enzymeList:
        print enzyme + "\t",
    print "\n"
    for i in range(0,460):
        print bacteriaList[i] + "\t",
        for k in data[i]:
            print k + "\t",
        print "\n"
       
create_table()
