
import os
from aiven.client import cli
from docutils.core import publish_doctree


# This function parses the CLI document folder and retrieves all the titles (matching the aiven command)
def find_cli_docs():
    list_of_commands = []
    dirname = os.path.dirname(__file__).replace('scripts/aiven','') + "docs/tools/cli"
    print(dirname)
    folderlist = []
    folderlist.append(dirname)
    for folder in folderlist:
        files = os.listdir(folder)
        for filename in files:
            if os.path.isdir(folder + "/" + filename) and filename != '/':
                folderlist.append(folder + "/" + filename)
            elif filename != '/':
                with open(os.path.join("files", folder + "/" + filename), 'r') as f:
                    text = f.read()
                    titles = publish_doctree(text).traverse(condition=section_title)
                    for t in titles:
                        list_of_commands.append(t.astext())
    
    list_of_commands = list(map(lambda x: x.replace('avn ', ''), list_of_commands))
    
    return sorted(list_of_commands)

# This function parses the CLI and returns all the functions
def find_cli_func():
    l = list(map(lambda x: x.replace('__', '@'), dir(cli.AivenCLI)))
    l = list(map(lambda x: x.replace('_', '-'), l))
    l = list(map(lambda x: x.replace('@', ' '), l))
    l = [idx for idx in l if idx[0] != ' ' and idx[0] != '-']
    return l

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
