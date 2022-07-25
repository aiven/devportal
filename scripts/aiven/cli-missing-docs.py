
import os
from aiven.client import cli
from docutils.core import publish_doctree


# This function parses the CLI document folder and retrieves all the titles (matching the aiven command)
def find_cli_docs():
    list_of_commands = []
    dirname = os.path.dirname(__file__).replace('scripts/aiven','') + "docs/tools/cli"
    print(dirname)
    folder_list = []
    folder_list.append(dirname)
    # Parsing all the folders under /docs/tools/cli
    for folder in folder_list:
        files = os.listdir(folder)
        for fine_name in files:
            # If we find subfolder, we add it to the list of folders
            if os.path.isdir(folder + "/" + fine_name) and fine_name != '/':
                folder_list.append(folder + "/" + fine_name)
            # if it's a file read it, and parse the doctree to extract the titles
            elif fine_name != '/':
                with open(os.path.join("files", folder + "/" + fine_name), 'r') as f:
                    text = f.read()
                    titles = publish_doctree(text).traverse(condition=section_title)
                    for t in titles:
                        list_of_commands.append(t.astext())
    # Remove from the titles the avn prefix to match it with the functions
    list_of_commands = list(map(lambda x: x.replace('avn ', ''), list_of_commands))
    
    return sorted(list_of_commands)

# This function parses the CLI and returns all the functions
def find_cli_func():
    # retrieves the list of functions from cli.AivenCLI and replaces the __ with @ 
    l = list(map(lambda x: x.replace('__', '@'), dir(cli.AivenCLI)))
    # replaces the single _ with - (since in cli a double _ would be a space, while a single _ would be translated to -)
    l = list(map(lambda x: x.replace('_', '-'), l))
    # replaces the @ with a space (since in cli a double _ would be a space, while a single _ would be translated to -)
    l = list(map(lambda x: x.replace('@', ' '), l))
    # removes from the list anything starting with - or space (not visible commands)
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
