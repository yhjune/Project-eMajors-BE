# 이화여자대학교 2023학년도 학사학위 청구논문
- 자기설계전공 트랙 : 디지털인문학
- [상세 위키](https://github.com/yhjune/major_csv/wiki)
- 2023-2 학사학위 청구논문을 위키 형식에 맞추어 재편집했습니다. 출처없는 무단 복제 및 사용을 금합니다.

> 본교에서는 2017년 입학생부터 정시 입학생을 계열별 모집으로 선발하고 있다. 이들은 1년간의 전공탐색 이후 본 전공을 결정하게 된다. 기존에 운영 중인 수강 과목 관련 시스템으로는 각각 4학기 이상 이수자와 7학기 이상 이수자를 대상으로 하는 수강 시뮬레이션 시스템과 졸업 시뮬레이션 시스템이 있다. 그러나 이는 최대 4학기 이내에서 전공결정과 복수전공 결정이 이루어지는 학생들이 대상이 아니므로 도움을 받기 어렵다. 따라서 본 연구에서는 년도별교과목기술부(2023학년도)에 기반, 4학기 미만 이수자들을 대상으로 하는 전공과목 로드맵 시스템을 설계하는 것을 목적으로 한다. 해당 시스템의 데이터와 주요 알고리즘을 오픈소스로 공개하고, 이를 통해 복수전공 결정 등을 위한 기초 교과목을 선수강하기 위한 계획 수립에 도움을 주는 시스템을 발전시킬 것을 기대한다.

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


