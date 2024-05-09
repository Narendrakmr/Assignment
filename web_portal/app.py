from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# Error handling example
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Example route with error handling
@app.route('/route')
@cross_origin()
def index():
    try:
        # Your route logic here
        return render_template('index.html')
    except Exception as e:
        # Log the error
        app.logger.error(f"An error occurred: {str(e)}")
        # Return an error response
        return "An error occurred", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=443)

