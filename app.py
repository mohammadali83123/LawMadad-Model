# # Import necessary libraries
# import warnings
# import os
# import nltk

# # Ensure NLTK uses our custom data directory
# nltk.data.path = ['/app/nltk_data'] + nltk.data.path

# # Import other libraries
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from llama_index.core import (
#     VectorStoreIndex,
#     StorageContext,
#     ServiceContext,
#     load_index_from_storage,
#     Document
# )
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.groq import Groq
# import pdfplumber

# # Suppress warnings
# warnings.filterwarnings('ignore')

# # Initialize FastAPI app
# app = FastAPI()

# # Define the request model
# class QueryRequest(BaseModel):
#     query: str

# # Set up the GROQ API key - use environment variable for security
# GROQ_API_KEY = "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"

# # Define the context path for PDF files
# input_files = [
#     "civil.pdf",
#     "constitution.pdf",
#     "criminal.pdf",
#     "family.pdf",
# ]

# # Preprocessing function for PDF text extraction
# def extract_text_from_pdf(file_path):
#     text_data = []
#     try:
#         with pdfplumber.open(file_path) as pdf:
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     text_data.append(text)
#         return "\n".join(text_data)
#     except Exception as e:
#         print(f"Error extracting text from {file_path}: {str(e)}")
#         return ""

# # Function to initialize the index
# def initialize_index():
#     # Check if storage exists
#     persist_dir = "./storage_law_app"
#     if os.path.exists(persist_dir) and os.listdir(persist_dir):
#         print("Loading existing index...")
#         # Initialize embedding model
#         embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         # Initialize LLM
#         llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
#         service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
#         # Reload the index
#         storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
#         return load_index_from_storage(storage_context, service_context=service_context)
#     else:
#         print("Creating new index...")
#         os.makedirs(persist_dir, exist_ok=True)
        
#         # Load and preprocess documents
#         documents = []
#         for file in input_files:
#             if os.path.exists(file):
#                 content = extract_text_from_pdf(file)
#                 if content:
#                     documents.append(Document(text=content))
#             else:
#                 print(f"Warning: File {file} not found")
        
#         if not documents:
#             print("Warning: No documents were loaded")
#             # Create a dummy document if no documents are found
#             documents = [Document(text="This is a placeholder document as no actual documents were found.")]
        
#         # Initialize embedding model
#         embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         # Initialize LLM
#         llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
#         service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
#         # Build and persist vector index
#         vector_index = VectorStoreIndex.from_documents(
#             documents=documents,
#             service_context=service_context,
#             show_progress=True
#         )
#         vector_index.storage_context.persist(persist_dir=persist_dir)
#         return vector_index

# # Define the context for legal queries
# LEGAL_CONTEXT = """
# Context: Provide legal guidance based on the Pakistani legal framework.
# Task: Analyze the query and provide a structured response with headings and bullet points.
# The format should be:
# 1. **Introduction/Overview**: A brief overview of the law or section.
# 2. **Section Description**: Explain what this section does, including its purpose and scope.
# 3. **Legal Provisions**: Highlight the key legal provisions or clauses under the specified section.
# 4. **Punishments**: Explicitly mention the punishments with references if applicable.
# 5. **Related Precedents**: Summarize any relevant legal precedents or landmark cases along with their results.
# 6. **Conclusion/Recommendations**: Conclude with advice or recommendations tailored to the query.
# """

# # Initialize the index at startup
# @app.on_event("startup")
# async def startup_event():
#     global index
#     index = initialize_index()

# # API endpoint for querying the model
# @app.post("/query/")
# async def query_model(request: QueryRequest):
#     try:
#         # Prepare the query engine
#         query_engine = index.as_query_engine()
        
#         # Append context to user query
#         full_query = f"{LEGAL_CONTEXT}\n\nQuery: {request.query}"
        
#         # Query the index
#         response = query_engine.query(full_query)
#         return {"response": response.response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Add a simple root endpoint for API documentation
# @app.get("/")
# async def root():
#     return {
#         "message": "Pakistani Legal Assistant API",
#         "usage": "Send POST requests to /query/ with a JSON body containing the 'query' field"
#     }


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=7860)


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


# import warnings
# import os
# import nltk
# import re

# # Ensure NLTK uses our custom data directory
# nltk.data.path = ['/app/nltk_data'] + nltk.data.path

# # Import other libraries
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from llama_index.core import (
#     VectorStoreIndex,
#     StorageContext,
#     ServiceContext,
#     load_index_from_storage,
#     Document
# )
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.groq import Groq
# import pdfplumber

# # Suppress warnings
# warnings.filterwarnings('ignore')

# # Initialize FastAPI app
# app = FastAPI()

# # Define the request model
# class QueryRequest(BaseModel):
#     query: str

# # Set up the GROQ API key - use environment variable for security
# GROQ_API_KEY = "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"

# # Define the context path for PDF files
# input_files = [
#     "civil.pdf",
#     "constitution.pdf",
#     "criminal.pdf",
#     "family.pdf",
#     "civil_1.pdf",
#     "civil_2.pdf",
#     "property_final.pdf",
#     "criminal_final.pdf",
#     "family_final.pdf"
# ]

# # Preprocessing function for PDF text extraction
# def extract_text_from_pdf(file_path):
#     text_data = []
#     try:
#         with pdfplumber.open(file_path) as pdf:
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     text_data.append(text)
#         return "\n".join(text_data)
#     except Exception as e:
#         print(f"Error extracting text from {file_path}: {str(e)}")
#         return ""

# # Function to initialize the index
# def initialize_index():
#     # Check if storage exists
#     persist_dir = "./storage_law_app"
#     if os.path.exists(persist_dir) and os.listdir(persist_dir):
#         print("Loading existing index...")
#         # Initialize embedding model
#         embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         # Initialize LLM
#         llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
#         service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
#         # Reload the index
#         storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
#         return load_index_from_storage(storage_context, service_context=service_context)
#     else:
#         print("Creating new index...")
#         os.makedirs(persist_dir, exist_ok=True)
        
#         # Load and preprocess documents
#         documents = []
#         for file in input_files:
#             if os.path.exists(file):
#                 content = extract_text_from_pdf(file)
#                 if content:
#                     documents.append(Document(text=content))
#             else:
#                 print(f"Warning: File {file} not found")
        
#         if not documents:
#             print("Warning: No documents were loaded")
#             # Create a dummy document if no documents are found
#             documents = [Document(text="This is a placeholder document as no actual documents were found.")]
        
#         # Initialize embedding model
#         embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         # Initialize LLM
#         llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
#         service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
#         # Build and persist vector index
#         vector_index = VectorStoreIndex.from_documents(
#             documents=documents,
#             service_context=service_context,
#             show_progress=True
#         )
#         vector_index.storage_context.persist(persist_dir=persist_dir)
#         return vector_index

# # Define the context for legal queries
# LEGAL_CONTEXT = """
# Context: Provide legal guidance based on the Pakistani legal framework.
# Task: Analyze the query and provide a structured response with headings and bullet points.
# The format should be:
# 1. **Introduction/Overview**: A brief overview of the law or section.
# 2. **Section Description**: Explain what this section does, including its purpose and scope.
# 3. **Legal Provisions**: Highlight the key legal provisions or clauses under the specified section.
# 4. **Punishments**: Explicitly mention the punishments with references if applicable.
# 5. **Related Precedents**: Summarize any relevant legal precedents or landmark cases along with their results.
# 6. **Conclusion/Recommendations**: Conclude with advice or recommendations tailored to the query.
# """

# # Define general response templates for common non-legal queries
# GENERAL_RESPONSES = {
#     "greeting": "Hello! I'm your Pakistani Legal Assistant. I can help you with questions about Pakistani law, including civil law, criminal law, family law, and constitutional matters. How can I assist you today?",
    
#     "capabilities": "I'm a specialized Pakistani Legal Assistant that can help you with:\n\n"
#                     "- Information about Pakistani civil, criminal, family, and constitutional law\n"
#                     "- Legal provisions and sections with detailed explanations\n"
#                     "- Applicable punishments under various legal provisions\n"
#                     "- Legal precedents and relevant case law\n"
#                     "- Recommendations on legal matters\n\n"
#                     "Just ask me any legal question, and I'll provide a structured response based on Pakistani law.",
    
#     "default": "I'm your Pakistani Legal Assistant. I can help answer questions about Pakistani law. "
#                "For legal queries, I'll provide detailed information with proper structure. "
#                "How can I assist you with your legal questions today?"
# }

# # Function to detect if a query is a legal question or general conversation
# def is_legal_query(query):
#     # Convert to lowercase for easier matching
#     query_lower = query.lower()
    
#     # Define patterns for greetings and capability questions
#     greeting_patterns = [
#         r'\b(hi|hello|hey|greetings|howdy|salam|assalam|namaste)\b',
#         r'\bhow are you\b',
#         r'\bnice to meet you\b'
#     ]
    
#     capability_patterns = [
#         r'\bwhat can you do\b',
#         r'\bwhat are your capabilities\b',
#         r'\bhow can you help\b',
#         r'\bwhat do you know\b',
#         r'\bwhat are you\b',
#         r'\bwho are you\b',
#         r'\bwhat is your purpose\b',
#         r'\bhow do you work\b'
#     ]
    
#     # Check if query matches any greeting patterns
#     for pattern in greeting_patterns:
#         if re.search(pattern, query_lower):
#             return False, "greeting"
    
#     # Check if query matches any capability inquiry patterns
#     for pattern in capability_patterns:
#         if re.search(pattern, query_lower):
#             return False, "capabilities"
    
#     # Legal keywords that suggest a legal query
#     legal_keywords = [
#         'law', 'legal', 'court', 'justice', 'right', 'constitution', 'section', 
#         'crime', 'criminal', 'civil', 'family', 'divorce', 'marriage', 'inheritance',
#         'punishment', 'penalty', 'fine', 'jail', 'prison', 'arrest', 'police',
#         'judge', 'lawyer', 'attorney', 'defendant', 'plaintiff', 'accused',
#         'trial', 'case', 'lawsuit', 'petition', 'appeal', 'witness', 'evidence',
#         'contract', 'property', 'damages', 'compensation', 'regulation', 'statute',
#         'act', 'provision', 'legislation', 'parliament', 'supreme court', 'high court',
#         'district court', 'tribunal', 'code', 'penal', 'procedure'
#     ]
    
#     # Check if the query contains legal keywords
#     for keyword in legal_keywords:
#         if keyword in query_lower:
#             return True, None
    
#     # If the query is longer than 20 characters and not identified as greeting or capabilities,
#     # assume it might be a legal query
#     if len(query) > 20:
#         return True, None
    
#     # Default to general response if we can't clearly identify
#     return False, "default"

# # Initialize the index at startup
# @app.on_event("startup")
# async def startup_event():
#     global index
#     index = initialize_index()

# # API endpoint for querying the model
# @app.post("/query/")
# async def query_model(request: QueryRequest):
#     try:
#         # Determine if the query is legal or general
#         is_legal, response_type = is_legal_query(request.query)
        
#         if not is_legal:
#             # Return predefined general response
#             return {"response": GENERAL_RESPONSES.get(response_type, GENERAL_RESPONSES["default"])}
#         else:
#             # Prepare the query engine for legal questions
#             query_engine = index.as_query_engine()
            
#             # Append context to user query
#             full_query = f"{LEGAL_CONTEXT}\n\nQuery: {request.query}"
            
#             # Query the index
#             response = query_engine.query(full_query)
#             return {"response": response.response}
            
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Add a simple root endpoint for API documentation
# @app.get("/")
# async def root():
#     return {
#         "message": "Pakistani Legal Assistant API",
#         "usage": "Send POST requests to /query/ with a JSON body containing the 'query' field"
#     }


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=7860)


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------


import warnings
import os
import nltk
import re

# Ensure NLTK uses our custom data directory
nltk.data.path = ['/app/nltk_data'] + nltk.data.path

# Import other libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    ServiceContext,
    load_index_from_storage,
    Document
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import pdfplumber

# Suppress warnings
warnings.filterwarnings('ignore')

# Initialize FastAPI app
app = FastAPI()

# Define the request model
class QueryRequest(BaseModel):
    query: str

# Set up the GROQ API key - use environment variable for security
GROQ_API_KEY = "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"

# Define the context path for PDF files
input_files = [
    "civil.pdf",
    "constitution.pdf",
    "criminal.pdf",
    "family.pdf",
    "civil_1.pdf",
    "civil_2.pdf",
    "property_final.pdf",
    "criminal_final.pdf",
    "family_final.pdf",
    "civil_book.pdf",
    "criminal_book.pdf",
    "penal_code_book.pdf",
    "family_law_ordinance_book.pdf",
    "west_family_book.pdf"
]

# Preprocessing function for PDF text extraction
def extract_text_from_pdf(file_path):
    text_data = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_data.append(text)
        return "\n".join(text_data)
    except Exception as e:
        print(f"Error extracting text from {file_path}: {str(e)}")
        return ""

# Function to initialize the index
def initialize_index():
    # Check if storage exists
    persist_dir = "./storage_law_app"
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        print("Loading existing index...")
        # Initialize embedding model
        embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
        # Initialize LLM
        llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
        service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
        # Reload the index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        return load_index_from_storage(storage_context, service_context=service_context)
    else:
        print("Creating new index...")
        os.makedirs(persist_dir, exist_ok=True)
        
        # Load and preprocess documents
        documents = []
        for file in input_files:
            if os.path.exists(file):
                content = extract_text_from_pdf(file)
                if content:
                    documents.append(Document(text=content))
            else:
                print(f"Warning: File {file} not found")
        
        if not documents:
            print("Warning: No documents were loaded")
            # Create a dummy document if no documents are found
            documents = [Document(text="This is a placeholder document as no actual documents were found.")]
        
        # Initialize embedding model
        embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
        # Initialize LLM
        llm = Groq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
        service_context = ServiceContext.from_defaults(embed_model=embed_model, llm=llm)
        
        # Build and persist vector index
        vector_index = VectorStoreIndex.from_documents(
            documents=documents,
            service_context=service_context,
            show_progress=True
        )
        vector_index.storage_context.persist(persist_dir=persist_dir)
        return vector_index

# Define the context for legal queries
LEGAL_CONTEXT = """
Context: Provide legal guidance based on the Pakistani legal framework.
Task: Analyze the query and provide a structured response with headings and bullet points.
The format should be:
1. **Introduction/Overview**: A brief overview of the law or section.
2. **Section Description**: Explain what this section does, including its purpose and scope.
3. **Legal Provisions**: Highlight the key legal provisions or clauses under the specified section.
4. **Punishments**: Explicitly mention the punishments with references if applicable.
5. **Related Precedents**: Summarize any relevant legal precedents or landmark cases along with their results.
6. **Conclusion/Recommendations**: Conclude with advice or recommendations tailored to the query.
"""

# Define general response templates for common non-legal queries
GENERAL_RESPONSES = {
    "greeting": "Hello! I'm your Pakistani Legal Assistant. I can help you with questions about Pakistani law, including civil law, criminal law, family law, and constitutional matters. How can I assist you today?",
    
    "capabilities": "I'm a specialized Pakistani Legal Assistant that can help you with:\n\n"
                    "- Information about Pakistani civil, criminal, family, and constitutional law\n"
                    "- Legal provisions and sections with detailed explanations\n"
                    "- Applicable punishments under various legal provisions\n"
                    "- Legal precedents and relevant case law\n"
                    "- Recommendations on legal matters\n\n"
                    "Just ask me any legal question, and I'll provide a structured response based on Pakistani law.",
    
    "default": "I'm your Pakistani Legal Assistant. I can help answer questions about Pakistani law. "
               "For legal queries, I'll provide detailed information with proper structure. "
               "How can I assist you with your legal questions today?"
}

# Function to detect if a query is a legal question or general conversation
def is_legal_query(query):
    # Convert to lowercase for easier matching
    query_lower = query.lower()
    
    # Define patterns for greetings and capability questions
    greeting_patterns = [
        r'\b(hi|hello|hey|greetings|howdy|salam|assalam|namaste)\b',
        r'\bhow are you\b',
        r'\bnice to meet you\b'
    ]
    
    capability_patterns = [
        r'\bwhat can you do\b',
        r'\bwhat are your capabilities\b',
        r'\bhow can you help\b',
        r'\bwhat do you know\b',
        r'\bwhat are you\b',
        r'\bwho are you\b',
        r'\bwhat is your purpose\b',
        r'\bhow do you work\b'
    ]
    
    # Check if query matches any greeting patterns
    for pattern in greeting_patterns:
        if re.search(pattern, query_lower):
            return False, "greeting"
    
    # Check if query matches any capability inquiry patterns
    for pattern in capability_patterns:
        if re.search(pattern, query_lower):
            return False, "capabilities"
    
    # Legal keywords that suggest a legal query
    legal_keywords = [
        'law', 'legal', 'court', 'justice', 'right', 'constitution', 'section', 
        'crime', 'criminal', 'civil', 'family', 'divorce', 'marriage', 'inheritance',
        'punishment', 'penalty', 'fine', 'jail', 'prison', 'arrest', 'police',
        'judge', 'lawyer', 'attorney', 'defendant', 'plaintiff', 'accused',
        'trial', 'case', 'lawsuit', 'petition', 'appeal', 'witness', 'evidence',
        'contract', 'property', 'damages', 'compensation', 'regulation', 'statute',
        'act', 'provision', 'legislation', 'parliament', 'supreme court', 'high court',
        'district court', 'tribunal', 'code', 'penal', 'procedure'
    ]
    
    # Check if the query contains legal keywords
    for keyword in legal_keywords:
        if keyword in query_lower:
            return True, None
    
    # If the query is longer than 20 characters and not identified as greeting or capabilities,
    # assume it might be a legal query
    if len(query) > 20:
        return True, None
    
    # Default to general response if we can't clearly identify
    return False, "default"

# Initialize the index at startup
@app.on_event("startup")
async def startup_event():
    global index
    index = initialize_index()

# API endpoint for querying the model
@app.post("/query/")
async def query_model(request: QueryRequest):
    try:
        # Determine if the query is legal or general
        is_legal, response_type = is_legal_query(request.query)
        
        if not is_legal:
            # Return predefined general response
            print(f"General query detected: '{request.query}'")
            print(f"Response type: {response_type}")
            return {"response": GENERAL_RESPONSES.get(response_type, GENERAL_RESPONSES["default"])}
        else:
            # Prepare the query engine for legal questions with similarity scores
            query_engine = index.as_query_engine(
                similarity_top_k=5,  # Retrieve top 5 most similar chunks
                response_mode="tree_summarize",
                # Return source nodes to analyze relevance
                include_similarity=True,
            )
            
            # Append context to user query
            full_query = f"{LEGAL_CONTEXT}\n\nQuery: {request.query}"
            
            # Query the index
            response = query_engine.query(full_query)
            
            # Calculate average similarity score from source nodes
            similarity_scores = []
            source_nodes_info = []
            
            if hasattr(response, 'source_nodes') and response.source_nodes:
                print(f"\n--- Diagnostic Information for Query: '{request.query}' ---")
                for i, node in enumerate(response.source_nodes):
                    if hasattr(node, 'score') and node.score is not None:
                        similarity_scores.append(node.score)
                        # Extract first 200 chars of text as preview
                        text_preview = node.node.text[:200] + "..." if len(node.node.text) > 200 else node.node.text
                        source_nodes_info.append({
                            "score": node.score,
                            "text_preview": text_preview
                        })
                        # Print diagnostic info to server logs
                        print(f"Source Node {i+1}: Score={node.score}")
                        print(f"Preview: {text_preview[:100]}...\n")
            
            # Calculate average similarity/confidence
            avg_similarity = sum(similarity_scores) / len(similarity_scores) if similarity_scores else None
            
            # Format the response with confidence information
            response_text = response.response
            
            # Add confidence information at the end of the response
            if avg_similarity is not None:
                confidence_percentage = round(avg_similarity * 100, 2)
                confidence_level = "High" if confidence_percentage > 80 else \
                                  "Medium" if confidence_percentage > 60 else "Low"
                
                # response_footer = f"\n\n---\n**Confidence Level**: {confidence_level} ({confidence_percentage}%)"
                # response_text += response_footer
                
                # Print confidence summary to server logs
                print(f"Confidence Summary: {confidence_level} ({confidence_percentage}%)")
                print("--- End of Diagnostic Information ---\n")
            
            # Return only the response to keep the API clean
            return {"response": response_text}
            
    except Exception as e:
        print(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Add a simple root endpoint for API documentation
@app.get("/")
async def root():
    return {
        "message": "Pakistani Legal Assistant API",
        "usage": "Send POST requests to /query/ with a JSON body containing the 'query' field"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)