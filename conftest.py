"""Файл конфигурации для pytest, чтобы он видел папку src."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
