
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_NORMATIVE_DOCS_TYPES (
                    _enddate date, _id bigint, _name string, _startdate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_NORMATIVE_DOCS_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
