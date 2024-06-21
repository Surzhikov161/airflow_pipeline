
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_STEADS (
                    _changeid bigint, _enddate date, _id bigint, _isactive bigint, _isactual bigint, _nextid bigint, _number string, _objectguid string, _objectid bigint, _opertypeid bigint, _previd bigint, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/01/AS_STEADS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_ADDHOUSE_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_ADDHOUSE_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_ADDR_OBJ_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _level bigint, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_ADDR_OBJ_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_APARTMENT_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_APARTMENT_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_HOUSE_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_HOUSE_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_NORMATIVE_DOCS_KINDS (
                    _id bigint, _name string
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_NORMATIVE_DOCS_KINDS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_NORMATIVE_DOCS_TYPES (
                    _enddate date, _id bigint, _name string, _startdate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_NORMATIVE_DOCS_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_OBJECT_LEVELS (
                    _enddate date, _isactive boolean, _level bigint, _name string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_OBJECT_LEVELS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_OPERATION_TYPES (
                    _enddate date, _id bigint, _isactive boolean, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_OPERATION_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_PARAM_TYPES (
                    _code string, _desc string, _enddate date, _id bigint, _isactive boolean, _name string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_PARAM_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                

                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_ROOM_TYPES (
                    _desc string, _enddate date, _id bigint, _isactive boolean, _name string, _shortname string, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/AS_ROOM_TYPES?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
