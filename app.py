from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default="Anonza")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)




all_posts = [
    {
        'title': 'Post 1',
        'content': '1. I love my friends'
    },

     {
        'title': 'Post 2',
        'content': '2. I love my VU friends'
    }
]

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

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()

        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)

#the domain would be here inside the route parenthisis
#@ - decorator - used for urls
#route is followed by the function that will run
#getting url parameters to the code - using variables in urls
#<data_type:variable_name>
#templates - organise html, css to avoid clutter - where html code is - place all of it into a template file