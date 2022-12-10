"""
This script checks if a renamed file is added for proper redirection on redirects_ file.
"""
import os, sys, argparse
import coloredlogs, logging
from typing import Dict, List

p = os.path.abspath(os.path.join(__file__, "../../.."))
os.chdir(p)

REDIRECTED_FILE = "_redirects"

logger = logging.getLogger("check_renamed_files")
logging.basicConfig(format="%(asctime)s - [%(levelname)s] - %(message)s")


FIELD_STYLES = dict(asctime=dict(color="yellow"), levelname=dict(color="magenta"))
LEVEL_STYLES = dict(
    debug=dict(color="green"),
    info=dict(color="cyan"),
    verbose=dict(color="blue"),
    warning=dict(color="yellow"),
    error=dict(color="red"),
    critical=dict(color="red"),
)

coloredlogs.install(
    level="DEBUG",
    logger=logger,
    isatty=True,
    level_styles=LEVEL_STYLES,
    field_styles=FIELD_STYLES,
)


def find_redirected() -> Dict:
    """Creates a dict with the redirected files
    on the _redirects file.

    { previous : redirected}

    :returns: set with redirected files
    :rtype: set
    """
    all_redirected_links = {}
    with open(REDIRECTED_FILE) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith("/docs/") and not line.startswith("/docs/:"):
            previous, redirected = [x.lstrip("/") for x in line.split()]
            # avoid repetitions of `html`
            if not previous.endswith(".html"):
                all_redirected_links[previous] = redirected

    return all_redirected_links


def check_missing_redirects(renamed_files: List[str]):
    """
    Creates a dict with all missing redirects.

    { previous_link: current_link }

    :returns: missing redirects
    :rtype: dict
    """

    INPUT = os.environ["ALL_OLD_AND_NEW_RENAMED_FILES"]
    all_new_and_renamed_files = dict([x.split(",")[::-1] for x in INPUT.split(" ")])

    missing_redirects = {}
    all_redirected_links = find_redirected()
    for renamed in renamed_files:
        try:
            previous_link = all_new_and_renamed_files[renamed].rstrip(".rst")
            logger.debug(previous_link)
        except KeyError:
            logger.error("Missing renamed files on all new and renamed files.")
            exit(0)
        current_link = renamed.rstrip(".rst")
        if all_redirected_links.get(previous_link) != current_link:
            missing_redirects[previous_link] = current_link
    return missing_redirects


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to find missing redirects.")
    parser.add_argument(
        "--renamed_files",
        help="delimited list input",
        type=str,
        nargs="*",
        default=" ",
    )
    parser.add_argument(
        "--path_file", help="path to a file", type=str, default=os.getenv("GITHUB_ENV")
    )

    renamed_files = parser.parse_args().renamed_files
    env_file = parser.parse_args().path_file

    if not renamed_files:
        logger.info("No files are renamed.")
        sys.exit()

    missing_redirects = check_missing_redirects(renamed_files)
    if not missing_redirects:
        logger.info("Files renamed and redirects are added to _redirects.")
        sys.exit()

    res = ""
    h = ["Previous Name", "Current Name"]
    logger.error("{:<40s} {:<40s}".format(*h))
    for k, v in missing_redirects.items():
        logger.error("/{:<40s} /{:<40s}".format(k, v))

    logger.info("🚨 Seems like you forgot to add redirects for the renamed files. 🚨")
    logger.info(
        "ℹ️ More info: https://docs.aiven.io/docs/community/documentation/tips-tricks/renaming-files.html"
    )

    with open(env_file, "a") as myfile:
        myfile.write(f"MISSING_REDIRECTION={missing_redirects}")
