from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import chat


app = Flask(__name__)
cors = CORS(app,resources={r"/chatbot/": {"origins": "http://localhost:8000",
"methods":["POST",],
"allow-headers":["Content-Type","Authorization"]
}})
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'



@app.route('/chatbot/', methods=["POST",])
def chatbotResponse():
    
    if request.method == 'POST':
        print(request.content_type)
        if request.content_type =="application/json":
            the_question = request.get_json()['question']
            the_response = chat.chatbot_response(the_question)
            return jsonify({"response":the_response})
    return "{}"
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=False)