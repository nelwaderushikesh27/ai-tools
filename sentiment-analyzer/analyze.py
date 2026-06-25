"""
Sentiment analyzer using Hugging Face Transformers.
"""

from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    
    def analyze(self, text):
        result = self.analyzer(text)[0]
        return {
            'text': text,
            'sentiment': result['label'],
            'confidence': round(result['score'], 4)
        }
    
    def analyze_batch(self, texts):
        results = self.analyzer(texts)
        return [
            {
                'text': text,
                'sentiment': r['label'],
                'confidence': round(r['score'], 4)
            }
            for text, r in zip(texts, results)
        ]


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Sentiment Analyzer")
    parser.add_argument('--text', type=str, help='Text to analyze')
    parser.add_argument('--file', type=str, help='File with texts')
    
    args = parser.parse_args()
    analyzer = SentimentAnalyzer()
    
    if args.file:
        with open(args.file, 'r') as f:
            texts = [line.strip() for line in f if line.strip()]
        results = analyzer.analyze_batch(texts)
        for r in results:
            print(f"{r['sentiment']:>8} ({r['confidence']:.2f}): {r['text']}")
    elif args.text:
        result = analyzer.analyze(args.text)
        print(f"Text: {result['text']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Confidence: {result['confidence']}")
    else:
        print("Provide --text or --file")
