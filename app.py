from flask import Flask, request, jsonify
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    input_text = data['text']

    # Cleaning
    cleaned_text = re.sub(r'[^\w\s]', '', input_text)

    # Tokenization
    nltk.download('punkt')
    tokens = nltk.word_tokenize(cleaned_text)

    # Removing stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]

    # Lemmatization
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    lemma = [lemmatizer.lemmatize(w, 'v') for w in filtered_sentence]

    return jsonify({'processed_text': lemma})

if __name__ == '__main__':
    app.run()
