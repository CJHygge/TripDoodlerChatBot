import tkinter as tk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

def summarize_paragraph(paragraph):
    # Tokenize the paragraph into sentences
    sentences = sent_tokenize(paragraph)

    # Tokenize the sentences into words
    words = word_tokenize(paragraph)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.casefold() not in stop_words]

    # Stemming the words
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]

    # Calculate word frequencies
    fdist = FreqDist(stemmed_words)

    # Calculate the weight of each sentence based on word frequencies
    sentence_weights = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence)
        sentence_stemmed_words = [stemmer.stem(word) for word in sentence_words]
        weight = sum([fdist[word] for word in sentence_stemmed_words])
        sentence_weights[sentence] = weight

    # Sort the sentences based on their weights
    sorted_sentences = sorted(sentence_weights, key=sentence_weights.get, reverse=True)

    # Choose the top 3 sentences as the summary
    summary = " ".join(sorted_sentences[:3])

    return summary

def run_summarizer():
    paragraph = input_box.get("1.0", tk.END)
    summary = summarize_paragraph(paragraph)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary)

# Create the main window
window = tk.Tk()
window.title("TripDoodler GPT Summarizer and Filter BOT")
window.configure(bg='#ADD8E6')  # Set the background color to blue

# Create the input box
input_label = tk.Label(window, text="Input Paragraph:")
input_label.pack()
input_box = tk.Text(window, height=10, width=50)
input_box.pack(fill=tk.BOTH, expand=True) # Allow the input box to expand

# Create the output box
output_label = tk.Label(window, text="Summary:")
output_label.pack()
output_box = tk.Text(window, height=5, width=50)
output_box.pack(fill=tk.BOTH, expand=True) #Allow the output box to expand

# Create the "Run" button
run_button = tk.Button(window, text="Run", command=run_summarizer, bg='#90EE90')
run_button.pack()

# Start the GUI event loop
window.mainloop()