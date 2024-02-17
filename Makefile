autogenerate:
	alembic revision --autogenerate -m "make migrations"

migrate:
	alembic upgrade head

load_fake_data:
	python3 sql_gun/add_data_into_db.py