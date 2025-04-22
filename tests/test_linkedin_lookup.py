import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.linkedin_data_processing.agents.linkedin_lookup_agent import lookup

if __name__ == "__main__":
    try:
        linkedin_url = lookup("Gabriel Caldas")
        print(f"LinkedIn URL: {linkedin_url}")
    except Exception as e:
        print(f"Error: {e}")