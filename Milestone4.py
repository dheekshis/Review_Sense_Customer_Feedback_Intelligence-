# ============================
# ReviewSense – Milestone 4
# Interactive Customer Feedback Dashboard
# ============================

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from wordcloud import WordCloud
import numpy as np

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="ReviewSense Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.metric-card {
    background-color: #f0f2f6;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Milestone2_Sentiment_Results_new.csv")
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

@st.cache_data
def load_keywords():
    try:
        return pd.read_csv("Milestone3_Keyword_Insights.csv")
    except:
        return pd.DataFrame()

df = load_data()
keywords_df = load_keywords()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🔍 Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["sentiment"].unique(),
    default=df["sentiment"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    options=df["product"].unique(),
    default=df["product"].unique()
)

# Date Filter Safe
if "date" in df.columns and df["date"].notna().any():

    st.sidebar.subheader("📅 Date Range")

    min_date = df["date"].min()
    max_date = df["date"].max()

    start_date = st.sidebar.date_input("Start Date", min_date)
    end_date = st.sidebar.date_input("End Date", max_date)

    filtered_df = df[
        (df["sentiment"].isin(sentiment_filter)) &
        (df["product"].isin(product_filter)) &
        (df["date"].notna()) &
        (df["date"] >= pd.to_datetime(start_date)) &
        (df["date"] <= pd.to_datetime(end_date))
    ].copy()

else:
    filtered_df = df[
        (df["sentiment"].isin(sentiment_filter)) &
        (df["product"].isin(product_filter))
    ].copy()

# ---------------------------
# Dashboard Title
# ---------------------------
st.markdown(
    '<h1 class="main-header">📊 ReviewSense – Customer Feedback Dashboard</h1>',
    unsafe_allow_html=True
)

# ---------------------------
# KPI Metrics
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

total_reviews = len(filtered_df)
pos_count = len(filtered_df[filtered_df["sentiment"] == "Positive"])
neg_count = len(filtered_df[filtered_df["sentiment"] == "Negative"])
neu_count = len(filtered_df[filtered_df["sentiment"] == "Neutral"])

pos_pct = (pos_count / total_reviews * 100) if total_reviews > 0 else 0
neg_pct = (neg_count / total_reviews * 100) if total_reviews > 0 else 0
neu_pct = (neu_count / total_reviews * 100) if total_reviews > 0 else 0

col1.metric("Total Reviews", total_reviews)
col2.metric("Positive", f"{pos_pct:.1f}%")
col3.metric("Negative", f"{neg_pct:.1f}%")
col4.metric("Neutral", f"{neu_pct:.1f}%")

# ---------------------------
# Sentiment Distribution
# ---------------------------
st.subheader("😊 Sentiment Distribution")

if not filtered_df.empty:
    fig1, ax1 = plt.subplots(figsize=(8,5))
    filtered_df["sentiment"].value_counts().plot(kind="bar", ax=ax1)
    st.pyplot(fig1)
else:
    st.info("No data matches selected filters.")

# ---------------------------
# Product-wise Sentiment
# ---------------------------
st.subheader("📱 Product-wise Sentiment")

if not filtered_df.empty:
    product_sent = (
        filtered_df.groupby("product")["sentiment"]
        .value_counts()
        .unstack(fill_value=0)
    )

    st.dataframe(product_sent)

    fig_hm, ax_hm = plt.subplots(figsize=(8,5))
    sns.heatmap(product_sent, annot=True, fmt="d", cmap="RdYlGn", ax=ax_hm)
    st.pyplot(fig_hm)

# ---------------------------
# Trend Over Time
# ---------------------------
if "date" in filtered_df.columns and not filtered_df.empty:

    st.subheader("📈 Sentiment Trends Over Time")

    filtered_df["month"] = filtered_df["date"].dt.to_period("M")
    trend = filtered_df.groupby(["month", "sentiment"]).size().unstack(fill_value=0)

    fig_trend, ax_trend = plt.subplots(figsize=(10,5))
    trend.plot(ax=ax_trend)
    st.pyplot(fig_trend)

# ---------------------------
# Keywords
# ---------------------------
st.subheader("🔑 Top Keywords & Word Cloud")

if not keywords_df.empty:

    top10 = keywords_df.head(10)

    fig_bar, ax_bar = plt.subplots(figsize=(8,5))
    ax_bar.barh(top10["keyword"], top10["frequency"])
    ax_bar.invert_yaxis()
    st.pyplot(fig_bar)

    word_freq = dict(zip(keywords_df["keyword"], keywords_df["frequency"]))
    wc = WordCloud(width=400, height=400, background_color="white").generate_from_frequencies(word_freq)

    fig_wc, ax_wc = plt.subplots(figsize=(5,5))
    ax_wc.imshow(wc, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)

# ---------------------------
# Confidence Score
# ---------------------------
st.subheader("📊 Confidence Score Distribution")

if not filtered_df.empty:
    fig_hist, ax_hist = plt.subplots(figsize=(8,4))
    ax_hist.hist(filtered_df["confidence_score"], bins=20)
    st.pyplot(fig_hist)

# ---------------------------
# Data Preview & Download
# ---------------------------
with st.expander("📋 Preview Filtered Data"):
    st.dataframe(filtered_df.head(15))

st.download_button(
    "⬇️ Download Filtered Reviews",
    filtered_df.to_csv(index=False).encode("utf-8"),
    "ReviewSense_Filtered_Reviews.csv"
)

if not keywords_df.empty:
    st.download_button(
        "⬇️ Download Keyword List",
        keywords_df.to_csv(index=False).encode("utf-8"),
        "ReviewSense_Keywords.csv"
    )

st.success("✅ Dashboard ready! Use sidebar filters to explore.")