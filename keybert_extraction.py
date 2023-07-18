```python
from keybert import KeyBERT
from transformers import pipeline

def extract_keywords(text, num_keywords=10):
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', 
                                      use_maxsum=True, nr_candidates=20, top_n=num_keywords)
    return keywords
```