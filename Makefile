install-dev:
	pipenv install --dev

lint:
	pipenv run flake8 SafecastPy examples
	pipenv run pylint SafecastPy

format:
	pipenv run black SafecastPy setup.py

release:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel --universal
	pipenv run twine check dist/*
	pipenv run twine upload dist/*
