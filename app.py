from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home/<string:name>')

def hello_world(name):
    return 'Hello, ' + name
#variables from urls - for dynamic urls - things have ids that keep changing
#can have multiple variables in url,
#make sure to pass to the routing method
if __name__ == "__main__":
    app.run(debug=True)

#the domain would be here inside the route parenthisis
#@ - decorator - used for urls
#route is followed by the function that will run
#getting url parameters to the code - using variables in urls
#<data_type:variable_name>