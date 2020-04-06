from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home/<string:name>')

def hello_world(name):
    return 'Hello, ' + name
#variables from urls - for dynamic urls - things have ids that keep changing
#can have multiple variables in url,
#make sure to pass to the routing method
@app.route('/onlyget', methods=['GET'])
#by setting up a method = only read the data but can't post
#POST
def only_get():
    return 'You can only get'

if __name__ == "__main__":
    app.run(debug=True)

#the domain would be here inside the route parenthisis
#@ - decorator - used for urls
#route is followed by the function that will run
#getting url parameters to the code - using variables in urls
#<data_type:variable_name>
#templates - organise html, css to avoid clutter - where html code is - place all of it into a template file