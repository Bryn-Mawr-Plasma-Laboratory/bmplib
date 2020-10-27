# This file is part of the bmplib package, a Python toolkit for the
# Bryn Mawr Plasma Laboratory at Bryn Mawr College.
#

__all__ = ["spectral"]

import pkg_resources

from bapsflib import (spectral)

# --- Define version -----------------------------------------------------------
try:
    # this places a runtime dependency on setuptools
    #
    # note: if there's any distribution metadata in your source files, then this
    #       will find a version based on those files.  Keep distribution metadata
    #       out of your repository unless you've intentionally installed the package
    #       as editable (e.g. `pip install -e {bmplib_directory_root}`),
    #       but then __version__ will not be updated with each commit, it is
    #       frozen to the version at time of install.
    #
    #: `bmplib` version string
    __version__ = pkg_resources.get_distribution("bmplib").version
except pkg_resources.DistributionNotFound:
    # package is not installed
    fallback_version = "unknown"
    try:
        # code most likely being used from source
        # if setuptools_scm is installed then generate a version
        from setuptools_scm import get_version

        __version__ = get_version(
            root="..", relative_to=__file__, fallback_version=fallback_version
        )
        del get_version
        warn_add = "setuptools_scm failed to detect the version"
    except ModuleNotFoundError:
        # setuptools_scm is not installed
        __version__ = fallback_version
        warn_add = "setuptools_scm is not installed"

    if __version__ == fallback_version:
        from warnings import warn

        warn(
            f"bmplib.__version__ not generated (set to 'unknown'), bmplib is "
            f"not an installed package and {warn_add}.",
            RuntimeWarning,
        )

        del warn
    del fallback_version, warn_add


del pkg_resources