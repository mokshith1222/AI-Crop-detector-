import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
SERVER_DIR = os.path.join(ROOT_DIR, "server")

if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)
if SERVER_DIR not in sys.path:
    sys.path.append(SERVER_DIR)

from server import app
