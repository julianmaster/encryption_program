import importlib
import os
import sys
import tempfile
import zipfile
from io import BytesIO

module_zip = %code%

tmp_dir = tempfile.TemporaryDirectory(delete=False)

with zipfile.ZipFile(BytesIO(module_zip), 'r') as zip_ref:
    zip_ref.extractall(tmp_dir.name)

sys.path.append(tmp_dir.name)

module_name = 'direction'
module_path = os.path.join(tmp_dir.name, "direction.pyc")

spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
