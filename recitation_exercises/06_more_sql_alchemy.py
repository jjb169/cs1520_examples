from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# feature we don't need that is being deprecated upstream by sqlaclchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


'''
This exercise is very similar to last weeks exercise but we will focus 
more on the many to many relationships among different tables (models). 
'''


'''
Consider the following schema:
	Forest(forest_no, forest_name, area)
	State(state_name, area)
	Coverage(entry_no, forest_no, state_name, area)
	Worker(ssn, name, employing_state)

A forest can span more than one state and a worker can work in multiple
forests (notice how both of these define a many to many relationship)
'''


'''
(1) create the tables/models, make sure you set the primary and 
    foreign keys. Look at the '06_db.txt' file to find out
    what the types of each column should be. I only used either
    an integer and a string
'''

#creating the Forest class
class Forest(db.Model):
	#use same attributes as listed above
	forest_no = db.Column(db.Integer, primary_key = True)
	forest_name = db.Column(db.String(80), nullable = False)
	area = db.Column(db.String(80), nullable = False)
	
	#worker col for relationship
	#worker_id = db.column(db.Integer, db.ForeignKey('worker.ssn'), nullable = False)
	
	#init function
	def __init__(self, forest_no, forest_name, area):
		self.forest_no = forest_no
		self.forest_name = forest_name
		self.area = area
		
	#repr function
	def __repr__(self):
		return '<Forest Number {}>'.format(self.forest_no)
		
#create the state class
class State(db.Model):
	#define the attributes listed above as columns
	state_name = db.Column(db.String(80), primary_key = True)
	area = db.Column(db.Integer, nullable = False)

	

	#init function
	def __init__(self, state_name, area):
		self.state_name = state_name
		self.area = area
		
	#repr function
	def __repr__(self):
		return '<State Name {}>'.format(self.state_name)
		
"""follows = db.Table('follows',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('followee_id', db.Integer, db.ForeignKey('user.user_id'))
)	"""
		
#create the coverage class - intermediate relationship table
class Coverage(db.Model):
	#define attributes as columns
	entry_no = db.Column(db.Integer, primary_key = True) 
	forest_no = db.Column(db.Integer, nullable = False)
	state_name = db.Column(db.String(80), nullable = False)
	area = db.Column(db.Integer, nullable = False)
	
	#init function
	def __init__(self, entry_no, forest_no, state_name, area):
		self.entry_no = entry_no
		self.forest_no = forest_no
		self.state_name = state_name
		self.area = area
		
	#repr functin
	def __repr__(self):
		return '<Entry Number {}>'.format(self.entry_no)
		
#create the worker class Worker(ssn, name, employing_state)
class Worker(db.Model):
	#define attributes as columns
	ssn = db.Column(db.String(20), primary_key = True)
	name = db.Column(db.String(20), nullable = False)
	employing_state = db.Column(db.String(30), nullable = False)
	
	#relationship to workers
	#forest = db.relationship('Forest', backref='worker', lazy='dynamic')
	
	#init function
	def __init__(self, ssn, name, employing_state):
		self.ssn = ssn
		self.name = name
		self.employing_state = employing_state
		
	#repr function 
	def __repr__(self):
		return '<Worker SSN {}>'.format(self.ssn)

'''
(2) populate the tables you created above, you can find the data for 
	the tables in the '06_db.txt' file. The delimiter for an entry/record 
	is ',' and for the tables it is an empty line ('\n'). Remeber to 
	drop all any previosuly created tables to avoid any problems
'''


#initialize the database
@app.cli.command('initdb')
def initdb_command():
	"""Reinitializes the database from 05_db.txt"""
	#drop all old tables
	db.drop_all()
	"""Creates the database tables."""
	db.create_all()
	
	#populate the db from the text file
	with open("05_db.txt") as inf:
		#first section is for Forests
		for line in inf:
			#first check if the line is empty '\n'
			if(line == "\n"):
				break
				
			#strip the newline from the current line of data
			line = line.strip()
			#else the line has info that needs added
			info = line.split(",")
			
			
			#create a new forest entry with this info
			db.session.add(Forest(info[0], info[1], info[2]))
				
		#second section is for States
		for line in inf:
			#first check if the line is empty '\n'
			if(line == "\n"):
				break
				
			#else the line has info that needs added
			info = line.split(",")
			
			#create a new forest entry with this info
			db.session.add(State(info[0], info[1]))
		
		
		#third section is for the Coverage
		for line in inf:
			#first check if the line is empty '\n'
			if(line == "\n"):
				break #done reading from file once done here
				
			#else the line has info that needs added
			info = line.split(",")
			
			#create a new forest entry with this info
			db.session.add(Coverage(info[0], info[1], info[2], info[3]))
			
		#fourth section
		for line in inf:
			#first check if the line is empty '\n'
			if(line == "\n"):
				break #done reading from file once done here
				
			#else the line has info that needs added
			info = line.split(",")
			
			#create a new forest entry with this info
			db.session.add(Worker(info[0], info[1], info[2]))
				
	#commit all additions to the db
	db.session.commit()	
	print('Initialized the database.')


'''
(3) As a warmup, find the name(s) of all workers that are employed by the largest state
'''

@app.cli.command('largest_state_workers')
def default():
	print("Workers in the largest state: ")
    largest_state = State.query.filter_by(area=db.session.query(func.max(State.area)).one()[0]).one()
	
    print(result)



'''
(4) Find the names of all workers that work in more than one forest
'''


'''
(5) Find the name(s) of the workers that work in the largest forest
'''


'''
(6) Find the name(s) of the workers that manage the largest area of forests
	Remeber workers can work in multiple forests hence you might need to sum
	the areas of those forests
'''

