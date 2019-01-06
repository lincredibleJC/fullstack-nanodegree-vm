# "Database code" for the DB Forum.

import psycopg2

import bleach

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("UPDATE posts SET content= 'cheese' WHERE content LIKE '%spam%'")
  c.execute("SELECT content, time FROM posts ORDER BY time DESC")
  posts = ([str(bleach.clean(row[0])), row[1]] for row in c.fetchall()) # c.fetchall() returns a table [[content, time],...]
  db.close()
  return posts
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  content = bleach.clean(content)
  c.execute("INSERT into posts VALUES (%s)", (content,))
  db.commit()
  db.close()
  
