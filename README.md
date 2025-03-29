# Building GenAI Powered Apps

This repository contains projects and resources for building applications powered by Generative AI. It is part of the IBM Generative AI Engineer specialization on Coursera.

GitHub Repo - https://github.com/CodeHalwell/ibm-build-genai-apps

## Contents

- **Projects**: A folder for each of the projects in the Building Generative AI-Powered Applications with Python module
- **Code Examples**: Demonstrations of Generative AI techniques.
- **Documentation**: Guides and references for using Generative AI tools.

## Requirements

- Python 3.12 or higher
- **Dependencies**: All required libraries are listed in `pyproject.toml`.

## Setup

1. Clone the repository:
    - Run: git clone https://github.com/CodeHalwell/ibm-build-genai-apps.git

2. Change directory to the repository folder:
    - Run: cd Building_GenAI_Powered_Apps

3. (Optional) Create and activate a virtual environment:
    - On Windows:
      - python -m venv venv
      - venv\Scripts\activate
    - On macOS/Linux:
      - python3 -m venv venv
      - source venv/bin/activate

4. Install the required dependencies (using pyproject.toml):
    - If using Poetry:
      - Run: poetry install
    - Otherwise, if your project is configured for pip installation:
      - Run: pip install .

5. (Optional) Install uv support:
    - If using Poetry:
      - Run: poetry add uvicorn
    - Otherwise:
      - Run: pip install uvicorn

## Usage

Run the provided scripts or notebooks to explore Generative AI applications. Detailed instructions are provided in each folder.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.