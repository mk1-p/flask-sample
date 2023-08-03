from app import create_app
# from flask import Flask

if __name__ == '__main__':
    print("Run Back Application!!")
    application = create_app()
    application.run(host='0.0.0.0', port=9000, debug=True)

