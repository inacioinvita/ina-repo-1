```python
from keyphrase_vectorizer import KeyphraseVectorizer

def vectorize_keyphrases(keyphrases):
    # Initialize the KeyphraseVectorizer
    vectorizer = KeyphraseVectorizer()

    # Fit the vectorizer to the keyphrases
    vectorizer.fit(keyphrases)

    # Transform the keyphrases into vectors
    vectorized_keyphrases = vectorizer.transform(keyphrases)

    return vectorized_keyphrases
```