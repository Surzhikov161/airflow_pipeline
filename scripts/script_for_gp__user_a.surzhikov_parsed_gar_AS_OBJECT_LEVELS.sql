
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_OBJECT_LEVELS (
                    _enddate date, _isactive boolean, _level bigint, _name string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_OBJECT_LEVELS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
