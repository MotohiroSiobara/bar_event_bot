import sqlalchemy as sa

url = 'sqlite:///bar_event.db'
ENGINE = sa.create_engine(url, echo=True)

# ENGINE.execute('DROP TABLE user')
# ENGINE.execute('CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), user_id  VARCHAR(20), screen_name VARCHAR(20), follow_count INT, follower_count INT, profile_image_url VARCHAR(20), follow_flg BIT, follower_flg BIT, url VARCHAR(255), college VARCHAR(255), description VARCHAR(255))')

# ENGINE.execute('ALTER TABLE user ADD college  VARCHAR(255)')
# SQL文に「?」が使用できないので、代わりに「%s」を使用
# ins = "INSERT INTO zoo (critter, count, damages) VALUES (%s, %s, %s)"
# engine.execute(ins, "あひる", 10, 0.0)
# engine.execute(ins, "くま", 2, 1000.0)
# engine.execute(ins, "いたち", 1, 2000.0)



# for row in rows:
#     print(row)
