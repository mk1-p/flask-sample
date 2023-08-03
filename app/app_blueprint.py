from flask import Blueprint, render_template, jsonify


#: blueprint 관련 세팅
#: web page 라우트 용
page_app = Blueprint('page_app', __name__,
                     template_folder='../templates', static_folder='../static') #: 템플릿 및 스태틱 파일 경로를 미리 지정
#: api 라우트 용
api_app = Blueprint('api_app', __name__, url_prefix='/api') #: prefix로 /api 를 붙이도록 한다.

