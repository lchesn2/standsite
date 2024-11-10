from flask import Flask, render_template,url_for
app=Flask(__name__)




@app.route('/')
def hellow_world():
    return render_template('index.html')
    
# @app.route('/')
# def hellow_world():
#     return render_template('index.html')  


# @app.route('/about_me')
# def about_me():
#     return render_template('about_me.html')


# @app.route('/blog')
# def blog():
#     return render_template('blog.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	#return render_template(f"{page_name}.html")
    return render_template(page_name)