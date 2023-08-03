# -*- coding: utf-8 -*-

class AppConfig(object):
    #: 임시 저장소 위치
    TMP_FOLDER = 'resource/tmp/'
    #: 세션 타임아웃은 초(second) 단위(60분)
    PERMANENT_SESSION_LIFETIME = 60 * 60
    #: 쿠기에 저장되는 세션 쿠키
    SESSION_COOKIE_NAME = 'app_session'
    #: 로그 레벨 설정
    LOG_LEVEL = 'debug'
    


