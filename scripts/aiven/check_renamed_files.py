"""
This script checks if renamed files were not added in the _redirects file.

PS. Fix the input
"""
import argparse
import os
import sys
import re

from typing import Set


p = os.path.abspath(os.path.join(__file__, "../../.."))
os.chdir(p)

REDIRECTED_FILE = "_redirects"


class MissingRedirection(Exception):
    pass


def checks_renamed_files(renamed: Set[str]) -> bool:
    def find_redirected() -> Set:
        """Creates a set with the redirected files

        :returns: set with redirected files
        :rtype: set
        """
        redirected = set()
        with open(REDIRECTED_FILE) as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("/docs/") and not line.startswith("/docs/:"):
                res = line.split(" ")[0]
                if not res.endswith(".html"):
                    redirected.add(
                        res,
                    )
        return redirected

    redirected = find_redirected()
    return renamed.difference(redirected)


def main():
    parser = argparse.ArgumentParser(description="Script to find missing redirects.")
    parser.add_argument(
        "--renamed_files", help="delimited list input", type=str, nargs="*", default=" "
    )
    args = parser.parse_args()
    renamed = set(
        [re.sub("\.rst$", "", item) for item in args.renamed_files.split(" ")],
    )
    print("RENAMED FILES")
    print(renamed)

    if not renamed:
        sys.exit()

    missing_redirects = checks_renamed_files(renamed)
    return missing_redirects


if __name__ == "__main__":
    main()

    # print("Missing redirects")
    # print(missing_redirects)
    # if missing_redirects:
    #    raise MissingRedirection(
    #        "Missing redirections for following files: "
    #        + str(missing_redirects)
    #        + "\n"
    #        + "Add redirects at _redirects file."
    #    )
