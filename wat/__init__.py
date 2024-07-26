import sys

from .inspection.inspection import wat

from .version import __version__

sys.modules[__name__] = wat
wat.__version__ = __version__
