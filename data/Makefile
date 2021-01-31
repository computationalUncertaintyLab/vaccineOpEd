#mcandrew;

PYTHON:= python3 -W ignore

run: pullData formatData pullAPIdocs
.PHONY: run

pullData:
	$(PYTHON) pulldatafromserver.py && \
	echo "Data pulled from Census Bur. API"

formatData:
	$(PYTHON) formatpep2019Data.py && \
	echo "PEP 2019 data formatted"

pullAPIdocs:
	$(PYTHON) apiRaceCategories.py && \
	echo "API loaded"
