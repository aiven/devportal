# The canonical tags of docs.aiven.io are pointing to redirected URL versions 
# ending with .html causing a redirect-canonical loop and makes the pages non-indexable.
# This will overwrite the canonical tag defined in furo base.html template
# Note that this method might not work if the Furo theme or Sphinx changes how they handle 
# the canonical URL in future releases.
def override_canonical_url(app, pagename, templatename, context, doctree):
    context['pageurl'] = "https://docs.aiven.io/{}".format(pagename)

def setup(app):
    app.connect('html-page-context', override_canonical_url)