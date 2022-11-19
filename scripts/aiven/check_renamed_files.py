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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to find missing redirects.")
    parser.add_argument(
        "--renamed_files", help="delimited list input", type=str, nargs="*", default=" "
    )

    renamed_files = parser.parse_args().renamed_files
    print(renamed_files)
    if not renamed_files:
        print("No renamed files found.")
        sys.exit()

    res = checks_renamed_files(set(renamed_files))
    print(" ".join(res))

    # print("Missing redirects")
    # print(missing_redirects)
    # if missing_redirects:
    #    raise MissingRedirection(
    #        "Missing redirections for following files: "
    #        + str(missing_redirects)
    #        + "\n"
    #        + "Add redirects at _redirects file."
    #    )
#        if [ -z "$redirects_missing" ]
#        then
#              echo "Redirects added correct."
#        else
#              echo "::error::Redirectis Missing _redirects for the files "$redirects_missing" "
#        fi
