from flask import Flask, render_template, request, url_for
# from app import routes
from app.routes import *


# 환경 변수 세팅

# 크롤러 드라이버 초기화

# 스케줄러 초기화

# Flask App 실행

def print_settings(config):
    print('========================================================')
    print('SETTINGS for APPLICATION')
    print('========================================================')
    for key, value in config:
        print ('%s=%s' % (key, value))
    print('========================================================')


def create_app():
    app = Flask(__name__)

    #: Config 설정
    from app.app_config import AppConfig
    app.config.from_object(AppConfig)
    # print_settings(app.config.items())

    #: BluePrint 세팅
    from app.app_blueprint import page_app, api_app
    app.register_blueprint(api_app)
    app.register_blueprint(page_app)

    print(app.url_map)

    return app
