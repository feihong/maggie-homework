install:
	pip install -r requirements.txt

lab:
	jupyter-lab

build:
	python build.py

serve:
	cd _build && python -m http.server

publish: build
	ghp-import --no-jekyll --push --no-history _build
	echo "Deployed to https://feihong.github.io/maggie-homework/"
