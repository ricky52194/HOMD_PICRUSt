def create_table():
    bacteriaList = []
    enzymeList = []
    data = []
    with open("names.txt") as rows:
        for bacteria in rows:
            bacteria = bacteria.split("\t")
            shortName = bacteria[0]
            with open("NameMap2.txt") as nameMap:
                for line in nameMap:
                    lineSplit = line.split("\t")
                    checkShort = lineSplit[1].replace("\n","")
                    if(shortName == checkShort):
                        shortName = lineSplit[0]
                bacteriaList.append(shortName)
    with open("enzyme_columns.txt") as col:
        for enzyme in col:
            enzyme = enzyme.replace("\n","")
            enzymeList.append(enzyme)
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
    for i in range(0,459):
        print bacteriaList[i] + "\t",
        for k in data[i]:
            print k + "\t",
        print "\n"
       
create_table()
