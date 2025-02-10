# 🛒Fake Review Detection Website

## Objective

This project aims to build an interactive website that allows users to input a product URL, scrape reviews, and classify them as "Real" or "Fake" using trained machine learning models. The classification results are displayed in a user-friendly interface, helping users assess the authenticity of product reviews. 

## Demo

Here is a demo of the Fake Review Detection app:

https://github.com/user-attachments/assets/db852426-531c-4144-885e-2498e87dd40e


## Features

- **Product Review Scraping**: Extracts reviews from the given product URL.
- **English Reviews Filtering**: The system processes only **English-language** reviews, as the trained models are optimized for English text.
- **Review Preprocessing**: Handles emojis and corrects spelling to improve text quality before applying **Word2Vec**.
- **Machine Learning-Based Classification**: Uses trained **SVM** and **MLP** models to classify reviews.
- **Model Selection**: Users can select between SVM and MLP models for predictions.
- **Overall Review Distribution**: Displays a **pie chart** showing the percentage of real vs. fake reviews.
- **User-Friendly Interface**: Implemented using **Streamlit** for easy interaction.

  
- **Project Folder Structure:**
  - `Project_WoC_7.0_Fake_Review_Detection_Chechpoint_4`
    - `app.py` - Streamlit interface for the user to input product URL and view results.
    - `scraping.py` - Scrapes reviews (ratings and text) from product URLs on e-commerce platforms (e.g., Amazon).
    - `preprocessing.py` - Processes and prepares review data for prediction.
    - `model.py` - load all pre-trained models like word2vec, SVM and , MLP.
    - `SVM_model.pkl` - Trained SVM model for fake review detection.
    - `MLP_model.pkl` - Trained MLP model for fake review detection.
    - `word2_vec_model.model` - Trained Word2Vec model
    - `README.md` - Project documentation.


## Technology Stack

- **Frontend & Backend**: Streamlit
- **Machine Learning Models**: Support Vector Machine (SVM) and Multi-Layer Perceptron (MLP)
- **Web Scraping**: BeautifulSoup
- **Libraries Used**:
  - numpy
  - pandas
  - scikit-learn
  - streamlit
  - BeautifulSoup4
  - requests
  - langdetect ( to detect English language)
  - emoji (to convert Emoji to text)
  - plotly (for pie chart visualization)

## How It Works

1. **User Input**:  
   The user provides a product URL.

2. **Scraping Reviews**:  
   The system extracts reviews (text & rating) from the given URL.  
   It filters only English-language reviews.
   
4. **Processinng Reviews**:  
   The system preprocesses the reviews, a step completed in Checkpoint 1. Additionally, I have implemented 
   emoji handling and spelling correction to enhance the quality of the text before converting it into word 
   vectors using Word2Vec. This ensures that the model receives clean and meaningful input for better 
   classification.
   
6. **Model Selection**:  
   Users can choose between SVM and MLP models for classification.

7. **Review Classification**:  
   The selected model predicts whether each review is "Real" or "Fake."

8. **Results Display**:  
   - Shows classified reviews along with their labels.
   - Displays a pie chart indicating the percentage of real vs. fake reviews.

## Installation & Setup

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Project_WoC_7.0_Fake_Review_Detection_Checkpoint_4.git
   cd Project_WoC_7.0_Fake_Review_Detection_Checkpoint_4/checkpoint_4
2. **Install Dependencies**
  Install all the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
3. **Run the Streamlit App**
   Launch the Streamlit app:
   ```bash
   streamlit run app.py
