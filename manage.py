#!/usr/bin/env python
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
