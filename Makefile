
_APP = app

help:
	@echo "\tmake test\t\t-> \trun test:"

test:
	$(MAKE) --directory=$(_APP) test


