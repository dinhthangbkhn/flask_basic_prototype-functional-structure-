from application import app

@app.route('/')
def index():
    return 'Hello world, My name is Thang'

