from pymongo import MongoClient
from pprint import PrettyPrinter
client=MongoClient()

pp=PrettyPrinter(indent=4)
def __connect__():
	db=client.test
	collection=db.zips
    	return collection


def __connectEmps__():
	db=client.employeesMongo
	collection=db.employees
    	return collection

def query1():
    	zips=__connect__()
	query=zips.aggregate([{"$group" :
                         { "_id" : "$state",
                          "totalPop" : { "$sum" : "$pop" } } },
                       { "$match" : {"totalPop" : { "$gte" : 10*1000*1000 } } }] )
	res='''<table class='table table-bordered table-hover'>
		<tr><th>State</th>
			<th>Population</th></tr>'''
	for i in range(len(query['result'])):
		res+= "<tr><td>"+ str(query['result'][i]['_id']) + "</td><td> "+str(query['result'][i]['totalPop'])+"</td></tr>"
    	return res

def query2():
	zips=__connect__()
	query=zips.aggregate([{ "$group" : {"_id" : { "state" : "$state", "city" : "$city" }, 
				"pop" : { "$sum" : "$pop" } } },
   				{"$group" : { "_id" : "$_id.state", "avgCityPop" : { "$avg" : "$pop" } } }
				])

	res='''<table class='table table-bordered table-hover'>
		<tr><th>State</th>
			<th>Average City Population</th></tr>'''

	for i in range(len(query['result'])):
		res+= "<tr><td>"+ str(query['result'][i]['_id']) + "</td><td> "+str(query['result'][i]['avgCityPop'])+"</td></tr>"
	return res

def query3():
	zips=__connect__()
	query=zips.aggregate([{ "$group":
                         { "_id": { "state": "$state", "city": "$city" },
                           "pop": { "$sum": "$pop" } } },
                       { "$sort": { "pop": 1 } },
                       { "$group":
                         { "_id" : "$_id.state",
                           "biggestCity":  { "$last": "$_id.city" },
                           "biggestPop":   { "$last": "$pop" },
                           "smallestCity": { "$first": "$_id.city" },
                           "smallestPop":  { "$first": "$pop" } } },
                       { "$project":
                         { "_id": 0,
                           "state": "$_id",
                           "biggestCity":  { "name": "$biggestCity",  "pop": "$biggestPop" },
                           "smallestCity": { "name": "$smallestCity", "pop": "$smallestPop" } } }])


	res='''<table class='table table-bordered table-hover'>
		<tr><th>State</th>
			<th>Biggest City</th>
			<th>Population </th>
			<th>Smallest City</th>
			<th>Population</th>'''

	for i in range(len(query['result'])):
		res+= '''<tr><td>'''+ str(query['result'][i]['state']) + '''</td>
			<td>'''+str(query['result'][i]['biggestCity']['name'])+'''</td>
			<td>'''+str(query['result'][i]['biggestCity']['pop'])+  '''</td>
			<td>'''+str(query['result'][i]['smallestCity']['name'])+ '''</td>
			<td>'''+str(query['result'][i]['smallestCity']['pop'])+ '''</td></tr>'''
	return res

def query4():
	zips=__connect__()
 	stuff=[]
	res='''<table class='table table-bordered table-hover'>
		<tr><th>State</th>
			<th>City</th></tr>'''
	for item in zips.find({"city":"SPRINGFIELD"},{"state":"1","city":"1"}):
		res+="<tr><td>"+item['state']+"</td><td>"+item['city']+"</td></tr>"
	return res


def empsQuery1():
	zips=__connectEmps__()
 	stuff=[]
	res='''<table class='table table-bordered table-hover'>
		<tr><th>Name</th>
			<th>Salary</th>
			<th>Department</th></tr>'''
	for item in zips.find({},{"id":"0","name":"1","salary":"1","department":"1"}).sort([("salary",-1)]).limit(20):
		res+="<tr><td>"+item['name']+"</td><td>"+item['salary']+"</td><td>"+item['department']+"</td></tr>"
	return res


def empsQuery2():
	zips=__connectEmps__()
 	stuff=[]
	res='''<table class='table table-bordered table-hover'>
		<tr><th>Name</th>
			<th>Salary</th>
			<th>Title</th></tr>'''
	for item in zips.find({"title":"Software Engineer"},{"id":"0","name":"1","salary":"1","title":"1"}).sort([("salary",-1)]).limit(10):
		res+="<tr><td>"+item['name']+"</td><td>"+item['salary']+"</td><td>"+item['title']+"</td></tr>"
	return res


def empsQuery3():
	zips=__connectEmps__()
 	stuff=[]
	res='''<table class='table table-bordered table-hover'>
		<tr><th>Name</th>
			<th>Year of Birth</th></tr>'''
	for item in zips.find({},{"id":"0","name":"1","yearBorn":"1"}).sort([("yearBorn",1)]).limit(10):
		res+="<tr><td>"+item['name']+"</td><td>"+item['yearBorn']+"</td></tr>"
	return res

def empsQuery4():
	zips=__connectEmps__()
 	stuff=[]
	res='''<table class='table table-bordered table-hover'>
		<tr><th>Name</th>
			<th>Title</th>
			<th>Salary</th></tr>'''
	for item in zips.find({"title":"Software Manager"},{"id":"0","name":"1","title":"1","salary":"1"}).sort([("salary",-1)]).limit(10):
		res+="<tr><td>"+item['name']+"</td><td>"+item['title']+"</td><td>"+item['salary']+"</td></tr>"
	return res

if __name__=="__main__":
	print(empsQuery1())    
