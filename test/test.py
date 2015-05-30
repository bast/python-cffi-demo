"""
Unit tests.
"""
import sys
BUILD_DIR = sys.argv[-1]
sys.path.append(BUILD_DIR)

import os
import subprocess
import pytest
from example import ffi, lib


@pytest.fixture(scope='function')
def context(request):
    """
    Add context to test functions.
    """
    ctx = lib.example_new()
    def cleanup():
        """
        Clean up the context.
        """
        lib.example_free(ctx)
    request.addfinalizer(cleanup)
    return ctx


def test_result_string(context):
    """
    Test the result string.
    """
    result = lib.example_get_string(context)
    assert ffi.string(result) == 'raboof!'


def test_add(context):
    """
    Test adding.
    """
    assert lib.example_add(context, 3, 4) == 7


def test_leaks():
    """
    Test memory leaks.
    """
    res = subprocess.Popen(
        [
            'valgrind',
            os.path.join(BUILD_DIR, 'bin', 'unit_tests')
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE).communicate()[1]
    if not 'All heap blocks were freed -- no leaks are possible' in res:
        assert 'definitely lost: 0 bytes in 0 blocks' in res
        assert 'indirectly lost: 0 bytes in 0 blocks' in res
        assert 'possibly lost: 0 bytes in 0 blocks' in res
