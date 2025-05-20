import sys
import os

# fmt: off
# Add the src directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from app import main
# fmt: on

if __name__ == "__main__":
    main()
