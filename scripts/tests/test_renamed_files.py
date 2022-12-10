import sys, os
import mock, pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../../")
from scripts.check_renamed_files import check_missing_redirects


@mock.patch.dict(
    os.environ,
    {
        "ALL_OLD_AND_NEW_RENAMED_FILES": "docs/tools.rst,docs/renamed_tools_file.rst docs/community.rst,docs/renamed_community_file.rst docs/integrations.rst,docs/renamed_integration_file.rst docs/platform.rst,docs/platform2.rst docs/products/opensearch/howto/connect-with-python.rst,docs/products/opensearch/howto/renamed_opensearch_file.rst"
    },
)
def test_check_missing_redirects_with_missing_links():
    renamed_files = [
        "docs/renamed_community_file.rst",
        "docs/renamed_integration_file.rst",
        "docs/renamed_tools_file.rst",
        "docs/products/opensearch/howto/renamed_opensearch_file.rst",
    ]
    missing_redirects = check_missing_redirects(renamed_files)
    assert missing_redirects == {
        "docs/community": "docs/renamed_community_file",
        "docs/integration": "docs/renamed_integration_file",
        "docs/tool": "docs/renamed_tools_file",
        "docs/products/opensearch/howto/connect-with-python": "docs/products/opensearch/howto/renamed_opensearch_file",
    }


@mock.patch.dict(
    os.environ,
    {
        "ALL_OLD_AND_NEW_RENAMED_FILES": "docs/tools.rst,docs/renamed_tools_file.rst docs/community.rst,docs/renamed_community_file.rst docs/integrations.rst,docs/renamed_integration_file.rst docs/platform.rst,docs/platform2.rst docs/products/opensearch/howto/connect-with-python.rst,docs/products/opensearch/howto/renamed_opensearch_file.rst"
    },
)
def test_check_missing_redirects_with_no_renamed_files():
    """
    Test when there were previous changes in all old and new renamed file,
    without renamed files in current commit. No missind redirects should be
    reported
    """
    renamed_files = []
    missing_redirects = check_missing_redirects(renamed_files)
    assert missing_redirects == {}


@mock.patch.dict(
    os.environ,
    {"ALL_OLD_AND_NEW_RENAMED_FILES": ""},
)
def test_check_missing_redirects_no_files_changed_and_no_renamed_files():
    """
    Function should raise an error if no files changed and this function is called
    """
    with pytest.raises(ValueError):
        renamed_files = []
        check_missing_redirects(renamed_files)
