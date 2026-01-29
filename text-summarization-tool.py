import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")


def summarize_text(text, num_sentences=3):
    text = re.sub(r"\s+", " ", text).strip()
    sentences = sent_tokenize(text)

    if len(sentences) <= num_sentences:
        return text

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))

    word_frequencies = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    selected_sentences = ranked_sentences[:num_sentences]

    # Keep original order
    selected_sentences = sorted(selected_sentences, key=lambda s: sentences.index(s))

    summary = " ".join(selected_sentences)

    # Fix missing spaces after periods
    summary = re.sub(r"\.(?=[A-Za-z])", ". ", summary)

    return summary


if __name__ == "__main__":
    print("📌 TEXT SUMMARIZATION TOOL (NLP Based)\n")
    input_text = input("Enter your text/article:\n\n")

    print("\n🔹 Original Text:\n")
    print(input_text)

    summary_output = summarize_text(input_text, num_sentences=3)

    print("\n✅ Summary:\n")
    print(summary_output)