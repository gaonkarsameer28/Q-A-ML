import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

#pip install scikit-learn

def load_config():
  """Loads configuration data from config.json."""  
  with open("config.json", "r") as config_file:
    config_data = json.load(config_file)
  return config_data

def answer_user_question(user_question):
    config = load_config()
    csv_file = config["csv_file"]

    # Load data from CSV
    data = pd.read_csv(csv_file)

    # Concatenate question and context into a single column
    data['question_context'] = data['question'] + ' ' + data['context']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(data['question_context'], data['context'], test_size=0.2, random_state=42)

    # Split data into train and test sets
    #X_train, X_test, y_train, y_test = train_test_split(data['question'], data['context'], test_size=0.2, random_state=42)

    # Define pipeline with TF-IDF vectorizer and LinearSVC classifier
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC(dual=False))
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Predict on test data
    predictions = pipeline.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
    predicted_response = pipeline.predict([user_question])
    print("Predicted Response:", predicted_response[0])
    # Check if the predicted response is empty or below a confidence threshold
    confidence_threshold = 0.1  # You can adjust this threshold based on your requirements
    decision_scores = pipeline.decision_function([user_question])[0]
    max_decision_score = max(decision_scores)
    print (confidence_threshold)
    if len(predicted_response) == 0 :#or max_decision_score <= confidence_threshold:
            return("Sorry, I couldn't find an answer to your question.")
    else:
            return(predicted_response[0])

# Example usage
#user_question = input("Enter your question: ")
#answer_user_question(user_question)
#predicted_response = pipeline.predict([user_question])
#print("Predicted Response:", predicted_response[0])
