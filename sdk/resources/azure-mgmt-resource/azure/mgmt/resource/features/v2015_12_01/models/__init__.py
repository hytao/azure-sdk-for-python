# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import FeatureProperties
    from ._models_py3 import FeatureResult
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
except (SyntaxError, ImportError):
    from ._models import FeatureProperties
    from ._models import FeatureResult
    from ._models import Operation
    from ._models import OperationDisplay
from ._paged_models import FeatureResultPaged
from ._paged_models import OperationPaged

__all__ = [
    'FeatureProperties',
    'FeatureResult',
    'Operation',
    'OperationDisplay',
    'OperationPaged',
    'FeatureResultPaged',
]