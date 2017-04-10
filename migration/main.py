import db_migration as dbmigr
import db_migration_utils as utils


with utils.Profiler() as p:
    #source = dbmigr.DbOracle("database.ini", "oracle")
    #twns = source.get_rows_as_tuple("select * from db.town")

    #abonents = source.get_rows_as_tuple("select id, name from db.abonent")
    destination = dbmigr.DbPostgreSQL("database.ini", "postgresql")
    version = destination.get_version_db()
    print(version)
    #destination.insert_rows("insert into abonent(id, name) values(%s, %s)", abonents)