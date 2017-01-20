.SUFFIXES: .xls .txt .sorted .parsed

%.sorted: %.txt 
	sort $< > $@

%.parsed: %.sorted
	python3 homd_read.py $< > $@

