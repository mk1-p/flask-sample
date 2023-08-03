from app.app_blueprint import page_app, render_template

@page_app.route('/')
def home():
    return render_template('welcome.html')

@page_app.app_errorhandler(404)
def page_not_found(e):
    print("에러 통과")
    return render_template('pages/404.html'), 404