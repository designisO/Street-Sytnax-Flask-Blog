from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'The Official Blog of Street Syntax'

@app.route('/blog')
def blog():
    posts = [{'title': 'Street Syntax', 'author': 'Orion'},
             {'title': 'Art of Language', 'author': 'Orion'}]
    return render_template('blog.html', author = "Orion", sunny = False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return "This is blog post number " + blog_id

if __name__ == '__main__':
    app.run()
