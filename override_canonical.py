def override_canonical_url(app, pagename, templatename, context, doctree):
    context['pageurl'] = "https://docs.aiven.io/{}".format(pagename)

def setup(app):
    app.connect('html-page-context', override_canonical_url)