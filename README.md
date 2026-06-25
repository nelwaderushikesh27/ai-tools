# 🛠️ AI Tools Collection

A curated collection of AI/ML utility tools and scripts.

## 📦 Tools Included

| Tool | Description | Tech |
|------|-------------|------|
| 🔤 **text-summarizer** | AI text summarization | Transformers |
| 🖼️ **img-enhancer** | Image enhancement & upscaling | OpenCV |
| 🎙️ **speech-to-text** | Speech recognition tool | Whisper |
| 🌍 **translator** | Neural machine translation | MarianMT |
| 📊 **sentiment-analyzer** | Sentiment analysis | Transformers |
| 🧹 **data-cleaner** | ML data preprocessing | Pandas |
| 📈 **model-monitor** | Model performance tracking | MLflow |

## 🚀 Getting Started

```bash
git clone https://github.com/nelwaderushikesh27/ai-tools.git
cd ai-tools

# Install specific tool
pip install -r text-summarizer/requirements.txt

# Run
python text-summarizer/summarize.py --text "Your long text here"
```

## 🔧 Tools Detailed

### 1. Text Summarizer

```python
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(long_text, max_length=130, min_length=30)
print(summary)
```

### 2. Sentiment Analyzer

```bash
python sentiment-analyzer/analyze.py --text "I love this product!"
# Output: {'sentiment': 'POSITIVE', 'confidence': 0.98}
```

### 3. Speech to Text

```bash
python speech-to-text/transcribe.py --audio recording.mp3
# Output: Transcribed text from audio
```

## 📂 Structure

```
ai-tools/
├── text-summarizer/
│   ├── summarize.py
│   ├── requirements.txt
│   └── README.md
├── img-enhancer/
│   ├── enhance.py
│   ├── models/
│   └── README.md
├── speech-to-text/
│   ├── transcribe.py
│   ├── requirements.txt
│   └── README.md
├── translator/
│   ├── translate.py
│   └── README.md
├── sentiment-analyzer/
│   ├── analyze.py
│   └── README.md
├── data-cleaner/
│   ├── clean.py
│   └── README.md
├── model-monitor/
│   ├── monitor.py
│   └── README.md
├── requirements.txt
└── README.md
```

## 📦 Common Dependencies

```txt
transformers>=4.36.0
torch>=2.1.0
opencv-python>=4.8.0
openai-whisper>=20231117
pandas>=2.1.0
numpy>=1.24.0
mlflow>=2.8.0
sentencepiece>=0.1.99
accelerate>=0.25.0
```

## 🤝 Contributing

Add your own AI tools or improve existing ones!

---
*Built with 🤖 for the AI community*
