# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first four.
SPHINXOPTS    ?=
SPHINXBUILD   ?= ./myenv/bin/sphinx-build
AUTOBUILD     ?= ./myenv/bin/sphinx-autobuild
ES_URL        ?=
PG_URL        ?=
SOURCEDIR     = .
BUILDDIR      = _build
PYTHON        = ./myenv/bin/python

# Put it first so that "make" without argument is like "make help".
help: requirements-stamp
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile livehtml livehtmlall spell create-index index-devportal index-helpcenter create-feedback-table

myenv:
	python -m venv myenv

requirements-stamp: requirements.txt myenv
	@echo Installing sphinx dependencies...
	./myenv/bin/pip install -r requirements.txt
	touch $@

# to prevent the catch-all target below from trying to build requirements.txt
requirements.txt: ;

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile requirements-stamp
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml: requirements-stamp
	$(AUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtmlall: requirements-stamp
	$(AUTOBUILD) -a "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) --watch _static

spell:
	vale $(SOURCEDIR)/index.rst
	vale $(SOURCEDIR)/docs

# Create Elasticsearch index
create-index: requirements-stamp
	$(PYTHON) "$(SOURCEDIR)/scripts/create_index.py" \
		--es-url="$(ES_URL)"

# Index Developer Portal pages to Elasticsearch
index-devportal: html requirements-stamp
	$(PYTHON) "$(SOURCEDIR)/scripts/index_developer_portal_pages.py" \
		--es-url="$(ES_URL)" \
		--html-build-dir="$(BUILDDIR)/html"

# Index Help Center pages to Elasticsearch
index-helpcenter: requirements-stamp
	$(PYTHON) "$(SOURCEDIR)/scripts/index_help_center_pages.py" \
		--es-url="$(ES_URL)"

# Create feedback table to PG
create-feedback-table: requirements-stamp
	$(PYTHON) "$(SOURCEDIR)/scripts/create_feedback_table.py" \
		--pg-url="$(PG_URL)"
