DICTS = retro_identifier.json

.PHONY: all
all: $(DICTS)

%.json: scripts/%.py
	python3 $< $@
