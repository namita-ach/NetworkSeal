import faiss
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_csv(file_path): # make it a function cuz life is easier that way
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df): #Convert IPs into numeric format and normalize numerical values.
    df["src_ip"] = df["src_ip"].apply(lambda x: hash(x) % (10**8))
    df["dst_ip"] = df["dst_ip"].apply(lambda x: hash(x) % (10**8))

    # use standard scaler to normalize- you don't want one random vector in one random direction with a higher magnitude
    scaler = StandardScaler()
    numerical_cols = ["src_ip", "dst_ip", "src_port", "dst_port", "protocol"]
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df[numerical_cols].to_numpy(), scaler

'''EXPLORING DIFFERENT INDEXING METHODS NOW'''

def create_flat_index(dim): #FAISS IndexFlatL2 index for exact nearest neighbor search
    index = faiss.IndexFlatL2(dim)
    return index

def create_ivf_index(data, num_clusters=100): #Creates an IVFFlat index for faster approximate nearest neighbor search
    dim = data.shape[1]
    quantizer = faiss.IndexFlatL2(dim)
    index = faiss.IndexIVFFlat(quantizer, dim, num_clusters, faiss.METRIC_L2)
    index.train(data.astype(np.float32))
    return index

def create_hnsw_index(dim, M=32): #Creates an HNSW index for approximate nearest neighbor search.
    index = faiss.IndexHNSWFlat(dim, M)
    return index

def add_to_index(index, data): #Adds vectorized data to the FAISS index.
    index.add(data.astype(np.float32))

def search_index(index, query_vector, k=5): #looks in FAISS index for five nearest enighbors
    distances, indices = index.search(query_vector.astype(np.float32), k)
    return distances, indices

if __name__ == "__main__":
    file_path = "flows.csv"

    df = load_csv(file_path)
    data, scaler = preprocess_data(df)

    method = "IVF"  # then you can just change to "Flat", "IVF", or "HNSW"

    if method == "Flat":
        index = create_flat_index(data.shape[1])
    elif method == "IVF":
        index = create_ivf_index(data)
    elif method == "HNSW":
        index = create_hnsw_index(data.shape[1])
    else:
        raise ValueError("Invalid indexing method selected!")

    add_to_index(index, data)

    query_vector = np.expand_dims(data[0], axis=0)
    distances, indices = search_index(index, query_vector, k=5)

    print("Nearest Neighbors:", indices)
    print("Distances:", distances)

