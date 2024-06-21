
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_NORMATIVE_DOCS_KINDS (
                    _id bigint, _name string
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_NORMATIVE_DOCS_KINDS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
