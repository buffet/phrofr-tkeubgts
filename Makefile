DICTS = retro_identifier.json \
        syms.json

.PHONY: all
all: $(DICTS)

%.json: scripts/%.py
	python3 $< $@
