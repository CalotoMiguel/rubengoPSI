export PGDATABASE := psi
export PGUSER := alumnodb
export PGPASSWORD := alumnodb
export PGHOST := localhost

clear_db:
	dropdb --if-exists $(PGDATABASE)
	createdb



connect_db:
	psql