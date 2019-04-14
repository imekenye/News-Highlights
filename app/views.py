from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    news_sources = get_sources('mysources')
    news_category = get_sources('category')
    

    title = 'Home - Welcome to Your #1 News Source'
    return render_template('index.html', title = title, sources = news_sources, category = news_category )

@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)    
