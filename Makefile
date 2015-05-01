.PHONY:test
test: clean
	nosetests -sv
	# coverage run --source=encryptit setup.py test
	./script/check-pep8.sh utcdatetime/
	./script/check-todo.sh utcdatetime/

.PHONY: clean
clean:
	find . -iname '*.pyc' -delete
	find . -name __pycache__ -type d -delete
	rm -rf utcdatettime.egg-info
	rm -rf dist/ MANIFEST
	rm -f .coverage

