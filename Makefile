# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first four.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
ES_URL		  ?=
PG_URL		  ?=
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
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

livehtmlall:
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

# Create feedback table to PG
create-feedback-table:
	python "$(SOURCEDIR)/scripts/create_feedback_table.py" \
		--pg-url="$(PG_URL)"

# (Re)Generate config listing for a service type
service-type-config-pg:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "pg" "includes/config-pg.rst"

service-type-config-kafka:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "kafka" "includes/config-kafka.rst"

service-type-config-cassandra:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "cassandra" "includes/config-cassandra.rst"

service-type-config-opensearch:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "opensearch" "includes/config-opensearch.rst"

service-type-config-mysql:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "mysql" "includes/config-mysql.rst"

service-type-config-m3db:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "m3db" "includes/config-m3db.rst"

service-type-config-redis:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "redis" "includes/config-redis.rst"

service-type-config-flink:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "flink" "includes/config-flink.rst"

service-type-config-grafana:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "grafana" "includes/config-grafana.rst"

service-type-config-influxdb:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config.py" "influxdb" "includes/config-influxdb.rst"

service-type-config-all:
	python "$(SOURCEDIR)/scripts/aiven/service_type_config_all.py"
# (Re)Generate cloud listing
cloud-list:
	python "$(SOURCEDIR)/scripts/aiven/clouds.py" "includes/clouds-list.rst"