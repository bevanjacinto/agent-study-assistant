from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

docs = [
    "Recursion is a technique where a function calls itself to solve smaller instances of a problem.",
    
    "A recursive function must have a base case to stop the recursion and prevent infinite loops.",
    
    "Example of recursion in Python: factorial calculation where n! = n * (n-1)!",
    
    "Recursion can be less efficient due to repeated calls but can be optimized using memoization."
]

embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)