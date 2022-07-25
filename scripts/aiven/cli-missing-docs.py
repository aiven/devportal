import os
from aiven.client import argx
from aiven.client import cli
from docutils.core import publish_doctree


# This function parses the CLI document folder and retrieves all the titles (matching the aiven command)
def find_cli_docs():
    list_of_commands = []
    dirname = os.path.dirname(__file__).replace('scripts/aiven','') + "docs/tools/cli"
    print(dirname)
    for dirpath, dirnames, filenames in os.walk(dirname):
        for name in filenames:
            with open(os.path.join(dirpath, name)) as f:
                text = f.read()
                titles = publish_doctree(text).traverse(condition=section_title)
                for t in titles:
                    list_of_commands.append(t.astext())
    # Remove from the titles the avn prefix to match it with the functions
    list_of_commands = list(map(lambda x: x.replace('avn ', ''), list_of_commands))
    
    return sorted(list_of_commands)

# This function parses the CLI and returns all the functions
# See https://github.com/aiven/aiven-client/blob/main/aiven/client/cli.py
# and the `help` method for what we are trying to do
def find_cli_func():
    # Each `avn` command is implemented by a method annotated with `@arg`
    # Those are listed in `argx.ARG_LIST_PROP`
    # At the moment, they're only on the AivenCLI class
    cmds = []
    for prop_name in dir(cli.AivenCLI):
        # Ignore private values/methods
        if prop_name.startswith("_"):
            continue
        # Get the value/method with that name
        prop = getattr(cli.AivenCLI, prop_name)
        # And see if it has an argument list defined on it
        arg_list = getattr(prop, argx.ARG_LIST_PROP, None)
        # If it doesn't, then it's not a command and we can ignore it
        if arg_list is None:
            continue
        # Replace double underscores with spaces, single underscores with hyphens,
        # to get the actual command
        cmd = prop_name.replace("__", " ").replace("_", "-")
        cmds.append(cmd)
    return cmds

# This function retrieves the section titles from a doc
def section_title(node):
    """Whether `node` is a section title.

    Note: it DOES NOT include document title!
    """
    try:
        return node.parent.tagname == "section" and node.tagname == "title"
    except AttributeError:
        return None # not a section title

def main():
    list_of_cli = find_cli_func()
    list_of_docs = find_cli_docs()

    #Uncomment the below to find the matches between doc and cli
    
    #print("FOUND")
    #intersection = sorted(set(list_of_cli).intersection(list_of_docs))
    #print(intersection)
    
    print("---------- MISSING -------------")
    difference = sorted(set(list_of_cli).difference(list_of_docs))
    for i in difference:
        print(i)

if __name__ == "__main__":
    main()
