.SUFFIXES: .xls .txt .sorted .parsed

%.txt: %.xls
	python3 xls_convert_txt.py $< > $@

%.sorted: %.txt 
	sort $< > $@

%.parsed: %.sorted
	python3 homd_read.py $< > $@

