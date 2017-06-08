select ms.column_name,
       dt.table_name,
       ms.is_active,
       srt.arch_exist ,
       storage.get_script(sqt.template, ms.year_ago , ms.report_period) script
from storage.map_storage ms,
     storage.data_type dt,
     storage.source_table srt,
     storage.sql_template sqt
     where ms.data_type_id = dt.id and
	   ms.sql_template_id = sqt.id and
	   ms.source_table_id = srt.id and
     ms.is_active is TRUE
order by ms.id