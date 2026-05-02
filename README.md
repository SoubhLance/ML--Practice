# 🤖 ML--Practice

<div align="center">

![Python](https://img.shields.io/badge/Python-80.1%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-12.2%25-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Practice%20Repo-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Included-8E24AA?style=for-the-badge&logo=openai&logoColor=white)

**A comprehensive, end-to-end Machine Learning & Data Science practice repository**
**from Python basics all the way to model deployment with Docker & MLFlow.**

*by [SoubhLance (Soubhik Sadhu)](https://github.com/SoubhLance)*

</div>

---

## 📦 What's Included

- ✅ Complete Python Bootcamp — 16 modules
- ✅ Complete Data Science + ML + NLP — 27 modules
- ✅ Python scripts and experiments
- ✅ Jupyter Notebooks throughout
- ✅ End-to-end project with deployment
- ✅ MLFlow, DagsHub, BentoML experiment tracking
- ✅ Docker containerisation
- ✅ NLP and Deep Learning bonus
---

## 🧩 Concept Mindmap

```mermaid
mindmap
  root((ML Practice))
    Python Foundations
      Basics and Syntax
      OOP and Classes
      Advanced Concepts
      File and DB Handling
      Logging and Exceptions
    Web and Deployment
      Flask
      Streamlit
      Docker
      Git and GitHub
      MLFlow and DagsHub
      BentoML
    Supervised Learning
      Linear Regression
      Ridge Lasso ElasticNet
      Logistic Regression
      SVM
      Naive Bayes
      KNN
      Decision Trees
      Random Forest
      AdaBoost
      Gradient Boosting
      XGBoost
    Unsupervised Learning
      K-Means Clustering
      Hierarchical Clustering
      DBSCAN
      Silhouette Clustering
      Anomaly Detection
      PCA
    NLP and Deep Learning
      Complete NLP Pipeline
      Text Preprocessing
      Deep Learning Bonus
    Projects
      Step-by-Step ML Lifecycle
      End-to-End Deployment
      AdaBoost Projects
      Gradient Boosting Projects
```

---

## 🔄 ML Pipeline

```mermaid
flowchart LR
    A[Raw Data] --> B[EDA and Analysis]
    B --> C[Feature Engineering]
    C --> D{Model Type?}

    D -->|Supervised| E[Train and Test Split]
    D -->|Unsupervised| F[Clustering or PCA]

    E --> G[Model Training]
    G --> H[Hyperparameter Tuning]
    H --> I[Evaluation Metrics]
    F --> I

    I --> J{Good Enough?}
    J -->|No| C
    J -->|Yes| K[Serialize Model]

    K --> L{Deploy How?}
    L --> M[Flask API]
    L --> N[Streamlit App]
    L --> O[Docker Container]

    M --> P[Production]
    N --> P
    O --> P
    P --> Q[MLFlow Tracking]
    Q --> R[DagsHub and BentoML]
```

---

## ⚙️ Tech Stack

```mermaid
flowchart LR
    subgraph Core [Core]
        Python
        Jupyter
    end

    subgraph DS [Data Science]
        NumPy
        Pandas
        Matplotlib
        Seaborn
    end

    subgraph MLLib [ML Libraries]
        ScikitLearn[Scikit-learn]
        XGBoost
        SciPy
    end

    subgraph NLPDL [NLP and DL]
        NLTK
        spaCy
        Keras
    end

    subgraph Deploy [Deployment]
        Flask
        Streamlit
        Docker
        MLFlow
        BentoML
        DagsHub
    end

    Core --> DS
    Core --> MLLib
    Core --> NLPDL
    MLLib --> Deploy
    NLPDL --> Deploy
```

---

## 📚 Module Breakdown

### 🐍 Complete Python Bootcamp

| # | Module | Key Topics |
|---|--------|------------|
| 1 | Python Basics | Variables, data types, I/O |
| 2 | Control Flow | if/else, loops, comprehensions |
| 3 | Data Structures | Lists, dicts, tuples, sets |
| 4 | Functions | Args, kwargs, lambdas, closures |
| 5 | Modules | Imports, packages, pip |
| 6 | File Handling | Read/write, CSV, JSON |
| 7 | Exception Handling | try/except, custom exceptions |
| 8 | Classes & Objects | OOP, inheritance, dunder methods |
| 9 | Advanced Python | Decorators, generators, iterators |
| 10 | Data Analysis | NumPy, Pandas, Matplotlib |
| 11 | Databases | SQLite, SQLAlchemy |
| 12 | Logging | Python logging module |
| 13 | Flask | REST APIs, routing, templates |
| 14 | Streamlit | ML web app UIs |
| 15 | Memory Management | gc, memory profiling |
| 16 | Multithreading | threading, multiprocessing, GIL |

---

### 🤖 Complete Data Science + ML + NLP

| # | Module | Algorithms / Tools |
|---|--------|--------------------|
| 2 | Introduction | ML overview, EDA, feature engineering |
| 3 | Linear Regression | OLS, gradient descent |
| 4 | Ridge / Lasso / ElasticNet | Regularization techniques |
| 5 | ML Project Lifecycle | Data pipeline, cross-validation |
| 6 | Logistic Regression | Binary & multiclass classification |
| 7 | SVM | Kernel tricks, hyperplane |
| 8 | Naive Bayes | Gaussian, Multinomial + handwritten notes |
| 9 | K-Nearest Neighbor | Distance metrics, k-tuning |
| 10 | Decision Tree | CART, entropy, Gini |
| 11 | Random Forest | Bagging, feature importance |
| 12 | AdaBoost | Boosting, weak learners |
| 13 | Gradient Boosting | GBM, learning rate |
| 14 | XGBoost | Extreme gradient boosting |
| 15 | Unsupervised ML | Clustering overview |
| 16 | PCA | Dimensionality reduction |
| 17 | K-Means Clustering | Elbow method, centroids |
| 18 | Hierarchical Clustering | Dendrograms, linkage |
| 19 | DBSCAN | Density-based clustering |
| 20 | Silhouette Clustering | Cluster quality scoring |
| 21 | Anomaly Detection | Isolation Forest, LOF |
| 22 | Docker | Containerisation for ML |
| 23 | Git & GitHub | Version control for ML projects |
| 24 | End-to-End Deployment | Full ML app deployment |
| 25 | MLFlow + DagsHub + BentoML | Experiment tracking, model registry |
| 26 | Complete NLP | Tokenisation, TF-IDF, embeddings |
| 27 | Deep Learning Bonus | Neural networks intro |

---

## 📊 Language Distribution

```mermaid
pie title Language Breakdown
    "Python" : 80.1
    "Jupyter Notebook" : 12.2
    "C" : 3.4
    "Cython" : 2.2
    "Tcl" : 1.2
    "C++" : 0.7
    "Other" : 0.2
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/SoubhLance/ML--Practice.git
cd ML--Practice
```

```bash
# Python Bootcamp
cd Complete-Python-Bootcamp-main
pip install -r requirements.txt

# Data Science + ML
cd Complete-Data-Science-With-Machine-Learning-And-NLP-2024-main
pip install -r requirements.txt
```

```bash
jupyter notebook
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.

---

<div align="center">

**Made with ❤️ by [Soubhik Sadhu](https://github.com/SoubhLance)**

*If this helped you, drop a ⭐ on the repo!*

</div>
