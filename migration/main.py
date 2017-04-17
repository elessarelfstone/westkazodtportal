import db_migration as dbmigr
import db_migration_utils as utils


with utils.Profiler() as p:
    migration = dbmigr.DbMigration2("database.ini")
    migration.export_abonents()
