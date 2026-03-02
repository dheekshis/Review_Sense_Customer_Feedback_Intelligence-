📊 ReviewSense – Turning Customer Feedback into Actionable Insights

✨ Project Overview

ReviewSense is a comprehensive customer feedback analytics system that converts raw textual reviews into structured, data-driven insights.

It processes unstructured customer opinions and transforms them into measurable business intelligence using Natural Language Processing (NLP) and interactive dashboards.

The workflow is organized into four major stages:

① Data Cleaning & Preparation
② Sentiment Analysis
③ Keyword Extraction
④ Interactive Dashboard Visualization

The final deliverable is an interactive BI dashboard built with Streamlit.


🏗 System Architecture


Unstructured Reviews
        ↓
Text Cleaning & Formatting
        ↓
Sentiment Detection
        ↓
Keyword Mining
        ↓
Interactive Dashboard
        ↓
Business Intelligence

🔹 Milestone 1 – Data Cleaning & Preprocessing

🎯 Goal

Prepare and standardize raw feedback data for accurate NLP processing.

⚙️ Activities Performed

✓ Eliminated special characters & punctuation
✓ Converted all text to lowercase
✓ Removed redundant spaces
✓ Standardized formatting
✓ Created a new column → clean_feedback

📥 Input

Raw review dataset (CSV format)

📤 Output

Milestone1_cleaned_feedback.csv

🛠 Tools & Libraries

• Python
• pandas
• Regular Expressions (re)


🔹 Milestone 2 – Sentiment Analysis

🎯 Goal

Categorize customer reviews into:

➤ Positive
➤ Negative
➤ Neutral

⚙️ Activities Performed

✓ Applied TextBlob polarity scoring
✓ Assigned sentiment labels
✓ Calculated confidence scores
✓ Generated sentiment distribution chart
✓ Created bar graph visualization

📥 Input

Milestone1_cleaned_feedback.csv

📤 Output

• Milestone2_Sentiment_Results_new.csv
• sentiment_bar_chart.png

📊 Output Fields

• clean_feedback
• sentiment
• confidence_score

🛠 Tools & Libraries

• Python
• pandas
• TextBlob
• matplotlib


🔹 Milestone 3 – Keyword Extraction

🎯 Goal

Extract high-frequency keywords from customer reviews.

⚙️ Activities Performed

✓ Lowercased text
✓ Removed non-alphabetic characters
✓ Tokenized text into words
✓ Calculated word frequency using Counter
✓ Ranked keywords by frequency

📥 Input

Milestone2_Sentiment_Results_new.csv

📤 Output

Milestone3_Keyword_Insights.csv

📊 Output Fields

• keyword
• frequency

🛠 Tools & Libraries

• Python
• pandas
• collections.Counter
• Regular Expressions (re)


🔹 Milestone 4 – Interactive Dashboard

🎯 Goal

Convert analytical outputs into a dynamic business intelligence dashboard.

🎛 Sidebar Filters

✓ Sentiment selector (Positive / Negative / Neutral)
✓ Product filter
✓ Date range selector

📌 KPI Indicators

• Total Reviews
• % Positive
• % Negative
• % Neutral

📊 Visual Components

▸ Sentiment distribution bar graph
▸ Product-wise sentiment summary table
▸ Sentiment heatmap (Product vs Sentiment)
▸ Monthly sentiment trend chart
▸ Top keyword frequency chart
▸ Word cloud visualization
▸ Confidence score histogram

📤 Export Options

⬇ Download filtered dataset (CSV)
⬇ Download keyword insights (CSV)

📥 Inputs

• Milestone2_Sentiment_Results_new.csv
• Milestone3_Keyword_Insights.csv

📤 Outputs

Interactive Streamlit Application

Exportable files:

• ReviewSense_Filtered_Reviews.csv
• ReviewSense_Keywords.csv

🛠 Technology Stack

• Python
• pandas
• TextBlob
• matplotlib
• seaborn
• WordCloud
• Streamlit

▶️ Setup & Execution Guide

Step ① – Install Required Packages

bash
pip install pandas textblob matplotlib seaborn wordcloud streamlit

Step ② – Execute Sentiment Module
bash
python milestone2.py


Step ③ – Execute Keyword Module

bash
python milestone3.py

Step ④ – Launch Dashboard

bash
python -m streamlit run milestone4.py

📊 Business Impact

ReviewSense empowers organizations to:

✓ Track customer satisfaction levels
✓ Evaluate product performance
✓ Detect recurring issues
✓ Monitor sentiment trends over time
✓ Support data-driven decision-making
✓ Export insights for reporting

🎓 Key Learning Highlights

• Text preprocessing fundamentals
• NLP-based sentiment classification
• Keyword frequency analysis
• Data visualization techniques
• Dashboard creation using Streamlit
• Designing an end-to-end analytics pipeline

🏁 Final Summary

ReviewSense effectively converts raw textual feedback into structured and meaningful business insights through:

✔ Sentiment Classification
✔ Keyword Analytics
✔ Interactive Visualization

This project showcases a complete real-world analytics pipeline suitable for business intelligence and decision-support applications.

📜 License

This project is licensed under the MIT License.

Developed as part of my Artificial Intelligence Internship – 2026.
