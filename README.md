# Research Concierge

**Research Concierge** is an AI-powered research assistant that can fetch papers from APIs (CrossRef, arXiv), parse PDFs, extract metadata, summarize content, and maintain persistent session memory. The system is modular with agents for coordination, retrieval, extraction, and summarization.


## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [License](#license)


## Features

- Fetch papers and metadata from CrossRef and arXiv APIs
- Parse PDFs and extract full text
- Summarize PDFs and extract keywords
- Persistent session memory using `MemoryBank` (pause/resume sessions)
- Modular agent-based architecture
- Easy to extend with additional agents or APIs

## Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/hari12314/research-concierge.git
cd research-concierge
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage
- Test Memory Extraction
```bash
python -m scripts.test_memory_extraction
```

- Test Coordinator Agent
```bash
python -m scripts.test_coordinator
```

## Testing
All agents and modules have corresponding test scripts in the scripts/ folder:
- test_week2.py → Coordinator & Retriever
- test_week3.py → PDF Parser & Extractor
- test_week4.py → Memory Bank (persistent session memory)

## Future Enhancements
- Implement pause/resume for sessions
- Integrate full CrossRef API for metadata
- Add automated evaluation using gold datasets
- Support multiple file formats (PDF, DOCX)



