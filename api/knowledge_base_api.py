import platform
from flask import Flask, request, jsonify
import csv_transformers2  # Import your existing code for CSV and AI/ML model
import question_response_ml
from flask_cors import CORS
import json
#pip install flask-cors

with open('config.json') as f:
    config = json.load(f)

app = Flask(__name__)
if config['development']:
    CORS(app, origins=config['allowed_origins'])  # Enable CORS only in development

@app.route("/check", methods=["GET"])
def check():
   return jsonify("hello")

@app.route("/answer", methods=["POST"])
def answer_question():
  """
  API endpoint to receive user question and return answer.

  Returns:
      JSON: Dictionary containing the answer or error message.
  """
 

  user_question = request.json.get("question")  # Get question from JSON payload

  if not user_question:
    return jsonify({"error": "Missing question in request body"}), 400

  try:
    answer = csv_transformers2.answer_user_question(user_question)
    return jsonify({"answer": answer})
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route("/answer2", methods=["POST"])
def answer_question2():
  """
  API endpoint to receive user question and return answer.

  Returns:
      JSON: Dictionary containing the answer or error message.
  """
 

  user_question = request.json.get("question")  # Get question from JSON payload

  if not user_question:
    return jsonify({"error": "Missing question in request body"}), 400

  try:
    answer = question_response_ml.answer_user_question(user_question)
    return jsonify({"answer": answer})
  except Exception as e:
    print(f"error:"+str(e))
    return jsonify({"error": str(e)}), 500

#if __name__ == "__main__":
 #   app.run(host='0.0.0.0', port=5000, debug=True)

  
if __name__ == "__main__":
     # Check the System Type before to decide to bind
     # If the system is a Linux machine -:) 
     if platform.system() == "Linux":
        app.run(host='0.0.0.0',port=5000, debug=True)
     # If the system is a windows /!\ Change  /!\ the   /!\ Port
     elif platform.system() == "Windows":
        app.run(host='0.0.0.0',port=50000, debug=True)
