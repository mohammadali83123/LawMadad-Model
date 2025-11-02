import os
import sys
import nltk

def check_environment():
    print("=== Environment Check ===")
    
    # Check Python version
    print(f"Python version: {sys.version}")
    
    # Check current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if directories exist
    nltk_data_dir = '/app/nltk_data'
    storage_dir = './storage_law_app'
    
    print(f"NLTK data directory exists: {os.path.exists(nltk_data_dir)}")
    print(f"Storage directory exists: {os.path.exists(storage_dir)}")
    
    # Check permissions
    if os.path.exists(nltk_data_dir):
        print(f"NLTK data directory permissions: {oct(os.stat(nltk_data_dir).st_mode)[-3:]}")
    
    if os.path.exists(storage_dir):
        print(f"Storage directory permissions: {oct(os.stat(storage_dir).st_mode)[-3:]}")
    
    # Check NLTK data path
    print(f"NLTK data path: {nltk.data.path}")
    
    # Check environment variables
    print("\nEnvironment Variables:")
    for key, value in os.environ.items():
        if key in ('NLTK_DATA', 'GROQ_API_KEY', 'PORT', 'HOST'):
            if key == 'GROQ_API_KEY' and value:
                print(f"{key}: [REDACTED]")
            else:
                print(f"{key}: {value}")
    
    # Check if PDF files exist
    print("\nPDF Files:")
    pdf_files = ["civil.pdf", "constitution.pdf", "criminal.pdf", "family.pdf"]
    for file in pdf_files:
        print(f"{file} exists: {os.path.exists(file)}")

if __name__ == "__main__":
    check_environment()