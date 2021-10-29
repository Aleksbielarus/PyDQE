table_queries = \
    [
        '''SELECT 
                             note_name
                           , note_text
                           , note_city
                           , note_source
                           , count(*)
                         FROM notes.news_notes
                         GROUP BY 
                             note_name
                           , note_text
                           , note_city
                           , note_source
                         HAVING count(*) > 1
                     ''',
 '''SELECT 
                          note_name
                        , note_text
                        , note_date
                        , note_source
                        , count(*)
                      FROM notes.private_ad_notes
                      GROUP BY 
                          note_name
                        , note_text
                        , note_date
                        , note_source
                      HAVING count(*) > 1
                    ''',
        '''SELECT 
                      note_name
                    , note_text
                    , note_city
                    , note_degrees
                    , note_date
                    , note_source
                    , count(*)
                  FROM notes.weather_notes
                  GROUP BY 
                      note_name
                    , note_text
                    , note_city
                    , note_degrees
                    , note_date
                    , note_source
                  HAVING count(*) > 1
                  '''
        ]