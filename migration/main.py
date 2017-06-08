import db_migration as db_migr
import db_migration_utils as utils


with utils.Profiler() as p:
    migration = db_migr.DbMigration("database.ini", ["oracle", "postgres"])
    migration.main()