import streamlit as st
from keybert_extraction import extract_keywords
from flair_pipeline import create_pipeline
from keyphrase_vectorizer import vectorize_keyphrases
from csv_export import export_to_csv

def main():
    st.title("Keyword Extraction App")
    text = st.text_area("Enter your text here")

    if st.button("Extract Keywords"):
        keywords = extract_keywords(text)
        st.success("Keywords extracted successfully!")
        st.write(keywords)

        pipeline = create_pipeline()
        vectorized_keyphrases = vectorize_keyphrases(keywords, pipeline)
        st.success("Keyphrases vectorized successfully!")
        st.write(vectorized_keyphrases)

        if st.button("Export to CSV"):
            csv_data = export_to_csv(vectorized_keyphrases)
            st.success("Data exported to CSV successfully!")
            st.download_button("Download CSV", data=csv_data, file_name='keywords.csv', mime='text/csv')

if __name__ == "__main__":
    main()