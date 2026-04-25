import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Data Dashboard", layout="wide")

st.title("📊 Smart Web Data Cleaner Dashboard")

# CSV yükle
@st.cache_data
def load_data():
    return pd.read_csv("books.csv")

df = load_data()

st.subheader("📦 Raw Data")
st.dataframe(df)

# --- METRICS ---
col1, col2, col3 = st.columns(3)

col1.metric("Total Books", len(df))
col2.metric("Average Price", f"£{df['price'].mean():.2f}")
col3.metric("Max Rating", df["rating"].max())

# --- FILTER ---
st.sidebar.header("Filters")

min_price = st.sidebar.slider(
    "Min Price",
    float(df["price"].min()),
    float(df["price"].max()),
    float(df["price"].min())
)

filtered_df = df[df["price"] >= min_price]

st.subheader("📈 Filtered Data")
st.dataframe(filtered_df)

# --- CHARTS ---
st.subheader("📊 Price Distribution")
st.bar_chart(filtered_df["price"])

st.subheader("⭐ Rating Distribution")
st.bar_chart(filtered_df["rating"])

# --- TOP ITEMS ---
st.subheader("🔥 Top 10 Most Expensive Books")
top_expensive = df.sort_values("price", ascending=False).head(10)
st.dataframe(top_expensive)