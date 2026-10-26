
# Hugging Face Sentiment Analysis

## Description
This project takes a sentence as input and predicts whether
the sentiment is positive or negative using a pretrained
Hugging Face Transformer model.

## Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- NLP (Natural Language Processing)

## Model Used
distilbert/distilbert-base-uncased-finetuned-sst-2-english

## How to Run

1. Clone this repository.
2. Install the required dependencies:

   pip install -r requirements.txt

3. Run the application:

   python app.py

4. Enter a sentence when prompted.

## Example Output

Input:
I am an Engineer

Output:
Label: POSITIVE
Score: 0.9878

Note: The score above is an example. Actual scores depend
on the input and model output.

## Author
Akshata Gurnale
