import streamlit as st
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
from io import BytesIO
from docx import Document
import PyPDF2
st.set_option('deprecation.showPyplotGlobaUse',False)
# Streamlit app title
st.title("Sherazi di Word Cloud")

# Function to generate word cloud
def generate_word_cloud(text, stopwords):
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(text)
    return wordcloud

# Upload files
st.sidebar.header("Upload Files")
uploaded_files = st.sidebar.file_uploader("Upload one or more documents (docx, pdf, txt)", type=["docx", "pdf", "txt"], accept_multiple_files=True)

# Checkbox for stop words
use_stopwords = st.sidebar.checkbox("Use Stopwords")

# Display uploaded files
if uploaded_files:
    for file in uploaded_files:
        with st.expander(f"Uploaded File: {file.name}"):
            file_content = file.read()

            # Extract text from different file types
            if file.name.endswith(".pdf"):
                pdf_reader = PyPDF2.PdfReader(BytesIO(file_content))
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            elif file.name.endswith(".docx"):
                doc = Document(BytesIO(file_content))
                text = " ".join([para.text for para in doc.paragraphs])
            else:  # Assume it's a text file
                text = file_content.decode('utf-8', errors='ignore')

            st.write("Text from the uploaded document:")
            st.write(text)

            if use_stopwords:
                stopwords = set(STOPWORDS)
            else:
                stopwords = set()

            # Generate Word Cloud
            wordcloud = generate_word_cloud(text, stopwords)
            st.image(wordcloud.to_array(), use_container_width=True, caption="Word Cloud")

            # Calculate word frequency
            words = text.split()
            word_freq = Counter(words)

            # Display the top 50 words
            st.subheader("Top 50 Words")
            for word, freq in word_freq.most_common(50):
                st.write(f"{word}: {freq}")

            # Option to add custom stopwords
            custom_stopwords = st.text_input("Enter additional stopwords (comma-separated):")
            custom_stopwords = set(custom_stopwords.split(','))

            # Remove custom stopwords from word cloud
            filtered_wordcloud = generate_word_cloud(text, stopwords.union(custom_stopwords))
            st.image(filtered_wordcloud.to_array(), use_container_width=True, caption="Filtered Word Cloud")

            # Display word frequency table
            st.subheader("Word Frequency Table")
            sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            st.table(sorted_word_freq)

# Share on social media
if st.button("Share on Social Media"):
    st.write("Share this awesome word cloud with your friends!")

# Footer
st.sidebar.markdown("---")
st.sidebar.text("By Sherazi")
