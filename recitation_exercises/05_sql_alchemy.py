from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# feature we don't need that is being deprecated upstream by sqlaclchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



'''
Consider the following schema:
	Forest(forest_no, forest_name, area)
	State(state_name, area)
	Coverage(entry_no, forest_no, state_name, area)

Notice how a forest can span two states
'''


'''
(1) create the tables/models, make sure you set the primary and 
    foreign keys. Look at the '05_db.txt' file to find out
    what the types of each column should be. I only used either
    an integer and a string
'''

#creating the Forest class
class Forest(db.Model):
	#use same attributes as listed above
	forest_no = db.Column(db.Integer, primary_key = True)
	forest_name = db.Column(db.String(80), nullable = False)
	area = db.Column(db.String(80), nullable = False)
	
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
		
#create the coverage class
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


'''
(2) populate the tables you created above, you can find the data for 
	the tables in the '05_db.txt' file. The delimiter for an entry/record 
	is ',' and for the tables it is an empty line ('\n'). Remeber to 
	drop all any previosuly created tables to avoid nay problems
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
				
	#commit all additions to the db
	db.session.commit()	
	print('Initialized the database.')


'''
(3) find and print the forest name(s) with the largest area (hint: use the func.max)
'''
@app.cli.command('area')
def largest_area():
	"""Finds and prints the forest(s) with largest area"""
	
	#use func.max to return the entry with max area
	#largest = db.session.query(func.max(Forest.area))#.filter_by(forest_name="Allegheny National Forest")
	#largest = Forest.query#.get(1)
	
	print()
	

'''
(4) find and print names of all forests that are located in PA (hint: might have to join 2 tables)
'''


'''
(5) find and print the number of forests for each state in descending order (hint: use func.count)
'''


'''
(6) find and print the percentage of area covered by forests in all states (hint: use func.sum)
'''

""" THIS IS THE SOLUTION """

# Run all queries
@app.cli.command('check')
def default():
    print('\n--- Q1 ---')
    result = Forest.query.filter_by(area=db.session.query(func.max(Forest.area)).one()[0]).one()
    print(result)
​
    print('\n--- Q2 ---')
    results = db.session.query(Coverage, Forest).filter(Forest.forest_no==Coverage.forest_no, Coverage.state_name=="PA")
    for row in results:
        print(row[1])
​
    print('\n--- Q3 ---')
    results = db.session.query(Coverage.state_name, func.count(Coverage.forest_no).label('forests_count')).group_by(Coverage.state_name).order_by(desc('forests_count'))
    for row in results:
        print(row)
​
    print('\n--- Q4 ---')
    results = db.session.query(Coverage.state_name, func.sum(cast(Coverage.area, db.Float)) * 100.0 / State.area).filter(State.state_name==Coverage.state_name).group_by(Coverage.state_name)
    for row in results:
        print(row)




