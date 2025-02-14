# FAISS and its Indexing Methods
 
FAISS basically operates by converting data into numerical vectors, which are then stored in an index structure
* When a query is provided, FAISS retrieves the most similar vectors based on predefined distance metrics, such as L2 distance (Euclidean distance) or inner product similarity
* The efficiency of FAISS comes from its various indexing methods

---

## Indexing Methods in FAISS

### 1. Flat Index (Exact Search)  
- Method: **IndexFlatL2**  
- About: This index performs a brute-force search across all stored vectors, ensuring an exact nearest neighbor match
- Pros: Provides 100% accuracy as it checks every possible match
- Cons: Computationally expensive and slow, especially for large datasets
- Probable Use Case: small datasets where accuracy is more important than search speed  

### 2. Inverted File Index (IVF)  
- Method: **IndexIVFFlat**  
- About: This approach partitions the dataset into multiple clusters and searches only within the most relevant cluster, significantly reducing the number of comparisons 
- Pros: Faster than the flat index for large datasets 
- Cons: Slightly less accurate since it does not search the entire dataset 
- Probable Use Case: Works well for large datasets where an approximate but fast search is acceptable 

### 3. Hierarchical Navigable Small World (HNSW)  
- Method: **IndexHNSWFlat**  
- About: This index builds a graph structure that allows for fast traversal and retrieval of nearest neighbors 
- Pros: Provides a good balance between speed and accuracy, making it a practical choice for real-time applications 
- Cons: More complex to implement and requires additional memory for graph storage 
- Probable Use Case: Useful when both speed and accuracy are important, such as in real-time search applications 



### Net-net:

| Index | Search Speed | Accuracy | Probable Use Case |  
|---------------|----------------|-------------|----------------|  
| Flat | Slow | 100% Accurate | Small datasets |  
| IVF | Faster | Approximate | Large datasets (100K+ records) |  
| HNSW | Very Fast | High Recall | Real-time search applications |  


###  How it was implemented 
1. Loaded a CSV file containing a five-tuple network flow dataset 
2. Preprocessed the data by normalizing features such as IP addresses and ports 
3. Created multiple FAISS indexes to compare their performance 
4. Inserted the data into the FAISS index and ran similarity searches