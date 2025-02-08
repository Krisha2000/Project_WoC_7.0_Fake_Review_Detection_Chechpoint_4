import streamlit as st
from scraper import scrape_reviews
from model import load_models, classify_reviews
from preprocessing import preprocess_text
import pandas as pd
import plotly.graph_objects as go

# Loading models
word2vec_model, mlp_model, svm_model = load_models()

# Streamlit UI
st.title("🛒 Product Review Fake or Real Classifier")

# Optional file uploader to load models (if you want users to upload their own models)
# svm_model = st.file_uploader("Upload SVM Model", type=["pkl"])
# word2vec_model = st.file_uploader("Upload Word2Vec Model", type=["model"])

# Dropdown menu to select model
model_choice = st.selectbox(
    "Select a Model for Prediction",
    ["MLP (Multi-layer Perceptron)", "SVM (Support Vector Machine)"]
)

# Getting user input for product link
url = st.text_input("Enter Product URL to Scrape Reviews")

if url:
    st.write("🔍 Scraping reviews from the URL...")

    reviews = scrape_reviews(url)

    if not reviews.empty:
        st.success(f"✅ Scraped {len(reviews)} reviews successfully!")

        try:
            if "Review Text" in reviews.columns and "Rating" in reviews.columns:
               
                preprocessed_reviews = []
                for i, review in enumerate(reviews["Review Text"]):
                    review_text = preprocess_text(review)
                    rating = reviews.iloc[i]["Rating"]
                    preprocessed_reviews.append({"Review Text": review_text, "Rating": rating})

                # Getting predictions based on selected model
                model_dict = {
                    "MLP (Multi-layer Perceptron)": mlp_model,
                    "SVM (Support Vector Machine)": svm_model
                }

                selected_model = model_dict[model_choice]
                predictions = classify_reviews(preprocessed_reviews, word2vec_model, selected_model)


                
                df = pd.DataFrame({
                    "Review": reviews["Review Text"],
                    "Rating": reviews["Rating"],
                    "Prediction": predictions
                })
                
                if selected_model == mlp_model:
                    df["Prediction"] = df["Prediction"].map({0: "Fake", 1: "Real"})
                else:
                    df["Prediction"] = df["Prediction"].map({1: "Fake", 0: "Real"})

                st.write(df)

                # Plotting Pie Chart for Selected Model
                review_counts = df["Prediction"].value_counts()

                fig = go.Figure(data=[go.Pie(
                    labels=review_counts.index,
                    values=review_counts,
                    hoverinfo="label+percent",
                    textinfo="percent+label",
                    textfont_size=15,
                    marker=dict(
                        colors=["#FF4C4C", "#4CAF50"],  
                        line=dict(color="black", width=2)
                    )
                )])

                fig.update_layout(
                    title=f"📝 Fake vs Real Reviews ({model_choice})",
                    plot_bgcolor="rgba(0,0,0,0)",  
                    paper_bgcolor="rgba(0,0,0,0)",  
                    font=dict(family="Arial, sans-serif", size=14, color="white")
                )

                st.plotly_chart(fig)

            else:
                st.warning("⚠ Invalid reviews data format.")
        except Exception as e:
            st.error(f"⚠ Error in processing reviews: {e}")

    else:
        st.warning("⚠ No reviews found. Please check the URL and try again.")
