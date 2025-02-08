import joblib
from gensim.models import Word2Vec
import numpy as np
from preprocessing import preprocess_text  # Ensure preprocess_text is imported

# Loading models (Word2Vec, SVM model, and MLP model)
def load_models():
    word2vec_model = Word2Vec.load('word2vec_model.model') 
    svm_model = joblib.load('SVM_model.pkl')  # SVM model
    mlp_model = joblib.load('MLP_model.pkl')  # MLP model
    return word2vec_model, svm_model, mlp_model


def classify_reviews(reviews, word2vec_model, selected_model):
    predictions = []
    
    for review in reviews:
        preprocessed_review = preprocess_text(review['Review Text'])  

        # Converting words to vectors using Word2Vec
        words = preprocessed_review.split()
        vectors = np.array([word2vec_model.wv[word] for word in words if word in word2vec_model.wv])
        
        if vectors.size > 0:
            # Average word vectors
            text_vector = np.mean(vectors, axis=0).reshape(1, -1)
            
            try:
                rating = float(review['Rating'])
            except ValueError:
                rating = 3.0  # Default rating

            review_length = len(words)
            
            rating_vector = np.array([[rating]])  
            length_vector = np.array([[review_length]]) 
            
            # Combining all features 
            combined_features = np.hstack([rating_vector, length_vector, text_vector])  

            # Predicting using the selected model (SVM or MLP)
            prediction = selected_model.predict(combined_features)
            predictions.append(prediction[0])
        else:
            predictions.append(0)  # Default prediction when no valid vectors

    return predictions


if __name__ == "__main__":
    word2vec_model, svm_model, mlp_model = load_models()
