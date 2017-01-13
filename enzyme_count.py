def enzyme_count():
    countList = []
    #Open the file with lines abbreviations and bacteria name
    #Ex:
        # aact  Aggregatibacter actinomycetemcomitans HK1651
    with open("names.txt") as f:
        for line in f:
            line = line.replace("\n","")
            lineSplit1 = line.split("\t")
            #Match abbreviation with specific .parsed file ending
            if(lineSplit1[0] == 'sked' or lineSplit1[0] == 'sflu'):
                filename = lineSplit1[0] + "_kegg-2.parsed"
            else:
                filename = lineSplit1[0] + "_kegg.parsed"
            #Open file with all enzymes 
            enzymeCol = open("enzyme_columns.txt", "r")
            #Open specific .parsed file
            with open(filename) as txtFile:
                for txtFileLine in txtFile:
                    lineSplit2 = txtFileLine.split()
                    #Append all enzymes in second column into a list
                    countList.append(lineSplit2[1])
                for enzyme in enzymeCol:
                    enzyme = enzyme.replace("\n","")
                    #Open files to write to
                    if(lineSplit1[0] == 'sked' or lineSplit1[0] == 'sflu'):
                        countFile = open(lineSplit1[0] + "_kegg-2.count", "a")
                    else:
                        countFile = open(lineSplit1[0] + "_kegg.count", "a")
                    #Count how many times each enzyme from enzyme_columns.txt appears in list and then write to file
                    countFile.write(enzyme + "\t" + str(countList.count(enzyme))+ "\n")
                countList = []
enzyme_count()
