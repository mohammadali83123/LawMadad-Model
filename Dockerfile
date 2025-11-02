FROM python:3.9-slim

WORKDIR /app

# Install essential build tools
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create app directories with proper permissions
RUN mkdir -p /app/nltk_data /app/storage_law_app
RUN chmod -R 777 /app/nltk_data /app/storage_law_app

# Set environment variable for NLTK data path 
ENV NLTK_DATA=/app/nltk_data

# Pre-download all necessary NLTK data packages
RUN python -m nltk.downloader -d /app/nltk_data punkt
RUN python -m nltk.downloader -d /app/nltk_data stopwords
RUN python -m nltk.downloader -d /app/nltk_data averaged_perceptron_tagger
RUN python -m nltk.downloader -d /app/nltk_data wordnet
RUN python -m nltk.downloader -d /app/nltk_data omw-1.4

# Download the embedding model in advance
RUN python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='sentence-transformers/all-MiniLM-L6-v2')"

# Copy all application files
COPY . .

# Expose the port
EXPOSE 7860

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]