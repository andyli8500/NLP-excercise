# NLP-excercise
Some excercises might be helpful


# Sentiment Analysis

- Tool: 
    1. Amazon Comprehend (https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api.html)
        - there are some examples on how to use it in python SDK in this notebook I made: [comprehend test using Python SDK](comprehend-test.ipynb)
        
    2. Twitter API (https://pypi.python.org/pypi/twitter) 
        - I have made a sample code in: [twitter test with Python API](twitter-random.py) 
        - Note that, this is a complete, but simple, version of data work flow: Grab data from twitter -> strip information -> push to a Stream for buffering -> then use Data Analytic Tool, E.g. Elasticsearch, for visualization on the results