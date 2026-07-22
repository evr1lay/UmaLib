# UmaLib   
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138.1-009688)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-active-success)


Simple horse management API built with FastAPI + SQLAlchemy.

## Quick Start

```bash
# Clone
git clone https://github.com/yourusername/umalib.git
cd umalib

# Setup
python -m venv venv
source venv/scripts/activate
pip install -r requirements.txt

# Run
uvicorn main:app --reload