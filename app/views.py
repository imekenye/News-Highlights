from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to Your #1 News Source'
    return render_template('index.html', title = title)

@app.route('/article/<int:article_id>')
def movie(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)    
