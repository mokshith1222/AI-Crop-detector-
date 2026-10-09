import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_DIR = os.path.join(CURRENT_DIR, "server")
if SERVER_DIR not in sys.path:
    sys.path.append(SERVER_DIR)

from server import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)
