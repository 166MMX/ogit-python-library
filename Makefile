pipenv:
    python3 -m venv venv
    ./venv/bin/pip install --upgrade pip setuptools
    ./venv/bin/pip install pipenv

requirements-dev: pipenv
    ./venv/bin/pipenv install --dev

generate: requirements-dev


build: generate
    $(./venv/bin/pipenv --py) -m pep517.build .

publish: build
    ./venv/bin/pipenv run twine upload --repository testpypi dist/*

clean
    rm -r venv dist build src/*.egg-info
