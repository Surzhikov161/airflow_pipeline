
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_ADDR_OBJ_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _level bigint, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_ADDR_OBJ_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
