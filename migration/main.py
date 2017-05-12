import db_migration as dbmigr
import db_migration_utils as utils


with utils.Profiler() as p:
    migration = dbmigr.DbMigration2("database.ini")
    #migration.export_abonents()
    #migration.fill_abn_column("select abonent_id, sum(t.debit) val from db.tdr t where t.report_date_id = 5 group by t.abonent_id", "deb_cr_yr_may", "storage.abn_debit_storage")
    migration.main()