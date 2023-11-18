# pdf to csv for major simulation
Ewha Womans university major simulation for lower grades

## project tree

```
.
├── README.md
├── pyproject.toml
├── requirements.txt
└── src
    ├── major_csv
    │   ├── __init__.py
    │   ├── course_introduction_csv.py
    │   ├── double_major_csv.py
    │   └── major_csv.py
    └── tests
        └── __init__.py
```

## requirements.txt
```
distlib==0.3.7
distro==1.8.0
filelock==3.12.4
JPype1==1.4.1
numpy==1.26.0
packaging==23.2
pandas==2.1.1
platformdirs==3.11.0
python-dateutil==2.8.2
pytz==2023.3.post1
six==1.16.0
tabula-py==2.8.2
tzdata==2023.3
virtualenv==20.24.5
```

## How to run

```python
python -m venv {/path/to/new/virtual/environment}
```
venv must be located in the same level with `src` folder:
```
.
├── README.md
├── pyproject.toml
├── requirements.txt
├── {your venv folder name}
└── src
```

and then activate the venv with `source {your venv foler name}/bin/activate`

lastly, install all the requiremnts with :

~~~
pip install -r requirements.txt
~~~


