SHELL := /bin/bash


.PHOHY: req
req:
	poetry install --no-root

.PHOHY: start_api
start_api: req
	poetry run uvicorn src.main:app --reload

.PHOHY: alembic_gen
alembic_gen:
	poetry run alembic revision --autogenerate -m ""
	poetry run alembic upgrade head

.PHOHY: alembic_upgrade
alembic_upgrade:
	poetry run alembic upgrade head

.PHOHY: start_db
start_db:
	./start_db.sh
	sleep 1
	poetry run alembic upgrade head

.PHOHY: start_db_no_upgrade
start_db_no_upgrade:
	./start_db.sh

.PHOHY:flake8
flake8:
	poetry run flake8
