.PHONY:test
test: clean
	coverage run --source=utcdatetime setup.py test
	./script/check-pep8.sh .
	./script/check-todo.sh utcdatetime/

.PHONY: clean
clean:
	find . -iname '*.pyc' -delete
	find . -name __pycache__ -type d -delete
	rm -rf utcdatettime.egg-info
	rm -rf dist/ MANIFEST
	rm -f .coverage

