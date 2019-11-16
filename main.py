# Author: Benjamin Noriega
# CSC 346 Cloud Computing - Russell Lewis
# Lab 7 - Google App Engine
# File : main.py
# Date: November 15th, 2019

import cgi, json, MySQLdb, passwords, random, webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        conn = MySQLdb.connect(
			unix_socket = passwords.SQL_HOST,
			user = passwords.SQL_USER,
			passwd = passwords.SQL_PASSWD,
			db = users)

		curs_1 = conn.cursor()
        
		curs_1.execute('SELECT * FROM people')
		response = curs_1.fetchall()

		res_json = json.dumps([{'id': p[0], 'name': p[1]} for p in response], indent = 2)

		curs_1.close()

		cookie = self.request.cookies.get('cookie1')

		if cookie is None:
			id = '%032x' % random.getrandbits(128)
			self.response.set_cookie('cookie1', id, maxage = 1800)
			self.response.write(cookie)

			curs_2 = conn.cursor()
            curs_2.execute(f"INSERT INTO sess_table (id, user) VALUES({id}, '');")

			self.response.write("""
			<html>
			<head>
			<title>Form</title>
			</head>
            <body>              
                <form action="https://nordi1.appspot.com/" method="get">
	                <input type="text" name=user value=""><br>
                    <input type=submit><br/>
                </form>
       		</body>
            </html>
            """)
			
			curs_3 = conn.cursor()
			name = self.request.get('user')
			cursor3.execute(f"UPDATE sess_table SET user = {name} WHERE id = {id};")

			self.response.write(name)
			curs_3.close()
			conn.commit()
			conn.close()
		else:
			self.response.write(cookie)

		self.response.write("""
		<html>
		<head>
		<title>Increment Link Page</title>
		</head>
		<body>
			<a href='https://nordi1.appspot.com'>Increment Page</a>
		</body>
		</html>
		""")
# stopped instance
app = webapp2.WSGIApplication([("/", MainPage),], debug=True)