# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first three.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
ES_URL		  ?=
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtml:
	sphinx-autobuild -a "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) --watch _static

spell:
	vale $(SOURCEDIR)/index.rst
	vale $(SOURCEDIR)/docs

# Create Elasticsearch index
create-index:
	python "$(SOURCEDIR)/scripts/create_index.py" \
		--es-url="$(ES_URL)"

# Index Developer Portal pages to Elasticsearch
index-devportal: html
	python "$(SOURCEDIR)/scripts/index_developer_portal_pages.py" \
		--es-url="$(ES_URL)" \
		--html-build-dir="$(BUILDDIR)/html"

# Index Help Center pages to Elasticsearch
index-helpcenter:
	python "$(SOURCEDIR)/scripts/index_help_center_pages.py" \
		--es-url="$(ES_URL)"
