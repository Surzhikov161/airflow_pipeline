
                CREATE EXTERNAL TABLE public.surzhikov_pxf_AS_STEADS (
                    _changeid bigint, _enddate date, _id bigint, _isactive bigint, _isactual bigint, _nextid bigint, _number string, _objectguid string, _objectid bigint, _opertypeid bigint, _previd bigint, _startdate date, _updatedate date
                    )
                LOCATION ('pxf://user/a.surzhikov/parsed_gar/01/AS_STEADS?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                
