TESTS=tests
SETTINGS=tests.settings
COVERAGE_COMMAND=


test:
	cd tests && DJANGO_SETTINGS_MODULE=$(SETTINGS) $(COVERAGE_COMMAND) ./manage.py test --traceback $(TESTS) --verbosity=2

coverage:
	+make test COVERAGE_COMMAND='coverage run --source=i18ntools --branch'
	cd tests && coverage html

docs:
	cd docs && $(MAKE) html

clean:
	rm -r tests/.coverage tests/htmlcov docs/_build

.PHONY: test coverage docs
