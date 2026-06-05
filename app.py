import streamlit as st
import pandas as pd
import plotly.express as px

from twitter_stream import get_tweets
from sentiment_analyzer import get_sentiment

# Page Configuration
st.set_page_config(
    page_title="Real-Time Sentiment Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Real-Time Sentiment Analysis Dashboard")

# Refresh Button
if st.button("🔄 Refresh Data"):
    st.rerun()

# Search Box
keyword = st.text_input(
    "🔍 Search Tweets",
    ""
)

# Load Tweets
df = get_tweets()

# Filter Tweets
if keyword:
    df = df[
        df["tweet"].str.contains(
            keyword,
            case=False
        )
    ]

# Sentiment Analysis
df[["Sentiment", "Score"]] = df["tweet"].apply(
    lambda x: pd.Series(get_sentiment(x))
)

# KPI Metrics
positive = len(df[df["Sentiment"] == "Positive"])
negative = len(df[df["Sentiment"] == "Negative"])
neutral = len(df[df["Sentiment"] == "Neutral"])

avg_score = round(df["Score"].mean(), 2)

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("😊 Positive", positive)
c2.metric("😐 Neutral", neutral)
c3.metric("😡 Negative", negative)
c4.metric("📈 Avg Score", avg_score)

# Data Table
st.subheader("📋 Tweet Data")

st.dataframe(
    df,
    use_container_width=True
)

# Download CSV
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Results",
    data=csv,
    file_name="sentiment_results.csv",
    mime="text/csv"
)

# Sentiment Counts
sentiment_counts = df["Sentiment"].value_counts()

# Charts Section
col1, col2 = st.columns(2)

# Bar Chart
with col1:
    st.subheader("📊 Sentiment Distribution")

    st.bar_chart(sentiment_counts)

# Pie Chart
with col2:
    st.subheader("🥧 Sentiment Breakdown")

    pie_df = sentiment_counts.reset_index()
    pie_df.columns = ["Sentiment", "Count"]

    fig = px.pie(
        pie_df,
        values="Count",
        names="Sentiment",
        title="Sentiment Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )