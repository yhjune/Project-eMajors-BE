# pdf to csv for major simulation
Ewha Womans university major simulation for lower grades

## project tree

```
.
├── README.md
├── __init__.py
├── pyproject.toml
├── pyvenv.cfg
├── requirements.txt
└── src
    ├── __init__.py
    ├── major_csv
    │   ├── __init__.py
    │   ├── csv_func
    │   │   ├── __init__.py
    │   │   └── transform_funcs.py
    │   ├── main.py
    │   ├── plan_func
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   ├── get.cpython-311.pyc
    │   │   │   ├── input.cpython-311.pyc
    │   │   │   ├── instance.cpython-311.pyc
    │   │   │   ├── plan_get.cpython-311.pyc
    │   │   │   ├── plan_input.cpython-311.pyc
    │   │   │   ├── plan_instance.cpython-311.pyc
    │   │   │   ├── plan_print.cpython-311.pyc
    │   │   │   └── print.cpython-311.pyc
    │   │   ├── plan_get.py
    │   │   ├── plan_input.py
    │   │   ├── plan_instance.py
    │   │   └── plan_print.py
    │   ├── preprocessing
    │   │   ├── __init__.py
    │   │   ├── pdf_to_csv.py
    │   │   ├── pdf_to_doc.py
    │   │   └── report_pdf.py
    │   └── shell_func
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-311.pyc
    │       │   └── mongodb_client.cpython-311.pyc
    │       ├── department
    │       └── mongodb_client.py
    └── tests
        ├── __init__.py
        ├── course_introduction_csv.py
        ├── course_introduction_doc.py
        ├── double_major_csv.py
        ├── double_major_doc.py
        ├── files.py
        ├── major_csv.py
        └── major_doc.py
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

## config file for mongoDB

add `.env` file like this:

```
.
├── README.md
├── .env
├── requirements.txt
└── src

```

```
# .env
DB_URI = {"your mongoDB url"}

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


