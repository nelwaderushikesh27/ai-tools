"""
Text summarizer using Hugging Face Transformers.
"""

from transformers import pipeline
import argparse


def summarize(text, max_length=130, min_length=30, model="facebook/bart-large-cnn"):
    """Summarize text using a pre-trained model."""
    summarizer = pipeline("summarization", model=model)
    
    # Handle long texts by chunking
    max_chunk = 1024
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])
    
    return ' '.join(summaries)


def main():
    parser = argparse.ArgumentParser(description="AI Text Summarizer")
    parser.add_argument('--text', type=str, help='Text to summarize')
    parser.add_argument('--file', type=str, help='File containing text')
    parser.add_argument('--max-length', type=int, default=130)
    parser.add_argument('--min-length', type=int, default=30)
    
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Provide --text or --file")
        return
    
    summary = summarize(text, args.max_length, args.min_length)
    print(f"\n📝 Summary:\n{summary}")


if __name__ == "__main__":
    main()
