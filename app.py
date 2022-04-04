"""
main module of the server file
"""
from config import Config
from app import app, db
from waitress import serve


@app.before_first_request
def create_tables():
    print("Creating database tables...")
    db.create_all()
    print("Done!")

if __name__ == '__main__':
    app.secret_key=Config.SECRET_KEY
    
    # if Config.APP_ENV == "production":
    serve(app, host="0.0.0.0", port='5000')
    # else:
    # app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)

