$ErrorActionPreference = "Stop"
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest --maxfail=1 --disable-warnings -q
