# The canonical tags of docs.aiven.io are pointing to redirected URL versions 
# ending with .html causing a redirect-canonical loop and makes the pages non-indexable.
# This will overwrite the canonical tag defined in furo base.html template
# Note that this method might not work if the Furo theme or Sphinx changes how they handle 
# the canonical URL in future releases.
def override_canonical(app, pagename, templatename, context, doctree):
    final_pagename = pagename
    if pagename != 'genindex' and pagename.endswith('index'):
        final_pagename = pagename[:-5]  # remove 'index' from the pagename 
    context['pageurl'] = "https://docs.aiven.io/{}".format(final_pagename)

def setup(app):
    app.connect('html-page-context', override_canonical)