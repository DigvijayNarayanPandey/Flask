from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
 return 'Hello World'
#if _name_ =="_main_":
 #   app.run(debug=True)
# @app.route('/about me')
# def about():
#     return "Hello my name is Narayan"
# @app.route('/contact')
# def cont():
#     return "I can be contacted"
if __name__=="__main__":
    app.run(debug=True)