# Brazilian E-Commerce Data Analysis using Python

## 1. Project Overview

This project focuses on exploring and analyzing the Brazilian E-Commerce Public Dataset by Olist using Python and Jupyter Notebook.

The dataset contains approximately 100,000 orders from an e-commerce platform in Brazil. It includes information about customers, orders, products, sellers, payments, reviews, and deliveries.

The main objective is to understand e-commerce business performance through data analysis and visualization.

## 2. Tools and Technologies

- **Python** – Programming and data analysis
- **Jupyter Notebook** – Interactive coding and analysis
- **Git** – Version control
- **GitHub** – Project hosting and collaboration
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization

## 3. Dataset

**Dataset Name:** Brazilian E-Commerce Public Dataset by Olist

**Source:** [Download from Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

The dataset contains the following CSV files:

| CSV File | Description |
|---|---|
| customers.csv | Customer details |
| orders.csv | Order information |
| order_items.csv | Products purchased in each order |
| order_payments.csv | Payment details |
| order_reviews.csv | Customer reviews |
| products.csv | Product information |
| sellers.csv | Seller information |
| geolocation.csv | Geographical information |
| product_category_name_translation.csv | Product category translations |

**Note:** The dataset is not included in this repository. Users must download it separately from Kaggle.

## 4. Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### Step 2: Install Jupyter Notebook

Open Command Prompt or Terminal and execute:

```bash
pip install notebook
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 4: Install Git

Download Git from the official website:

https://git-scm.com/install/

Verify the installation:

```bash
git --version
```

### Step 5: Download the Dataset

1. Visit the Olist dataset link on Kaggle.
2. Log in to your Kaggle account.
3. Download the dataset ZIP file.
4. Extract the ZIP file.
5. Place all CSV files inside the project's `olist_dataset/` folder.

## 5. Project Folder Structure

The project is organized into separate folders for datasets, logs, output files, configuration files, Jupyter notebooks, and Python processing modules.

```text
Tap - Python/
│
├── .vscode/
│
├── logs/
│
├── olist_dataset/
│   ├── customers.csv
│   ├── geolocation.csv
│   ├── order_items.csv
│   ├── order_payments.csv
│   ├── order_reviews.csv
│   ├── orders_semicolon.csv
│   ├── orders.csv
│   ├── product_category_name_translation.csv
│   ├── products.csv
│   ├── schema.sql
│   └── sellers.csv
│
├── output/
│   ├── bad_records.csv
│   └── run_summary.json
│
├── .gitignore
│
├── bad_records.csv
├── clean_orders.csv
├── clean_orders.json
├── column_mapping.json
├── config.yaml
│
├── Day 12.ipynb
├── Day 13.ipynb
├── Day 14.ipynb
├── olist_analysis.ipynb
│
├── manifest.json
├── pytest.py
├── reader.py
├── requirements.txt
├── run_summary.json
├── test_functions.py
├── transformer.py
└── validator.py
```

## 6. Running the Project

### Step 1: Clone the Repository

Open Command Prompt or Terminal:

```bash
git clone https://github.com/your-username/your-repository.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Brazilian-Ecommerce-Analysis
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

### Step 5: Open and Run the Notebook

1. Open the project folder.
2. Select the required notebook, such as `olist_analysis.ipynb`.
3. Execute the notebook cells in sequence using **Shift + Enter**.
4. View the outputs, analysis, and visualizations.

## 7. Example Dataset Loading

Use the following Python code to load the dataset:

```python
import pandas as pd

customers = pd.read_csv(
    '../data/raw/olist_customers_dataset.csv'
)

orders = pd.read_csv(
    '../data/raw/olist_orders_dataset.csv'
)

print(customers.head())
print(orders.head())
```

Make sure the file paths match the project folder structure.

## 8. Updating the Project Using Git

To upload changes to GitHub:

```bash
git add .
git commit -m "Update data analysis"
git push origin main
```

## 9. Expected Outcomes

- Understand customer purchasing behavior.
- Analyze sales and revenue trends.
- Identify popular product categories.
- Evaluate payment methods.
- Analyze delivery performance.
- Understand customer satisfaction through reviews.
- Create meaningful data visualizations.

## 10. References

- [Python Official Website](https://www.python.org/)
- [Jupyter Notebook Documentation](https://jupyter.org/)
- [Git Official Website](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Olist Brazilian E-Commerce Dataset – Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

