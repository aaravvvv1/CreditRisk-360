# CreditRisk 360: End-to-End Default Prediction Pipeline

## 📌 Project Overview
CreditRisk 360 is a full-stack data intelligence solution designed to predict loan defaults and visualize financial risk.
By integrating **SQL** for data extraction, **Python (Scikit-Learn)** for predictive modeling, and **Power BI** for interactive reporting, this project identifies high-risk borrowers that traditional banking grades often miss.

**Key Achievement:** identified **$67M** in toxic loan exposure hidden within "Grade A" & "Grade B" portfolios.

## 🛠️ Tech Stack
* **Database:** PostgreSQL (Data Ingestion & Storage)
* **Python:** Pandas (ETL), Scikit-Learn (Random Forest Classifier), SQLAlchemy
* **Visualization:** Power BI (DAX Measures, Star Schema, Bookmarks)

## 📊 Workflow
1.  **Ingestion:** Automated extraction of 28,000+ credit records from PostgreSQL.
2.  **Processing:** Cleaned data, handled outliers, and performed One-Hot Encoding for categorical features.
3.  **Modeling:** Trained a Random Forest model achieving **93% Accuracy** in predicting default probability.
4.  **Deployment:** Exported risk scores (`Low`, `Medium`, `High`) back to a CSV for BI consumption.
5.  **Reporting:** Built an executive dashboard to filter risk by Loan Grade, Income, and Ownership status.

## 📈 Key Insights
* **The "Silent Killer":** A significant cluster of borrowers with high credit grades (A/B) were flagged as **High Risk** due to dangerous Debt-to-Income ratios (>40%).
* **Income vs. Risk:** Default probability does not strictly correlate with low income; leverage (Loan Amount / Income) is the stronger predictor.

## 🚀 How to Run
1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/yourusername/CreditRisk-360.git](https://github.com/yourusername/CreditRisk-360.git)
    ```
2.  **Install Dependencies**
    ```bash
    pip install pandas sqlalchemy psycopg2-binary scikit-learn
    ```
    ![Dashboard Preview](Dasboard_view.png)
3.  **Run the Pipeline**
    ```bash
    python train_model.py
    ```

