# "Database code" for the DB Forum.

import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("SELECT content, time FROM posts ORDER BY time DESC")
  posts = c.fetchall()
  db.close()
  return posts
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("INSERT into posts VALUES (%s)", (content,))
  db.commit()
  db.close()