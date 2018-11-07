import sqlite3

sqlite_file = 'story_points.sqlite'

table_name1 = 'stories'
table_name2 = 'features'


story_points_field = 'points'
story_points_type = 'INTEGER'
story_summary_field = 'summary'
story_summary_type = 'SUMMARY'

feature_summary = 'summary'
feature_summary_type = 'TEXT'
story_id = 'story_id'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


c.execute('CREATE TABLE  IF NOT EXISTS {tn} (story_id INTEGER PRIMARY KEY, {tf} {ft} NOT NULL, {tf2} {ft2} NOT NULL)'.format(tn=table_name1, tf=story_points_field, ft=story_points_type, tf2=story_summary_field, ft2=story_summary_type))

c.execute('CREATE TABLE IF NOT EXISTS {tn} (feature_id INTEGER PRIMARY KEY, {tf} {ft}, {tf2} {ft2},'
          'FOREIGN KEY (story_id) REFERENCES stories(story_id))'
          .format(tn=table_name2, tf=feature_summary, ft=feature_summary_type, tf2=story_id, ft2='INTEGER'))
conn.commit()
conn.close()