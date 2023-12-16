install:
	pip install -r requirements.txt

lab:
	jupyter-lab

build:
	python build.py

serve: build
	cd content && python -m http.server

publish: build
	ghp-import --no-jekyll --push --no-history content
	echo "Deployed to https://feihong.github.io/maggie-homework/"
