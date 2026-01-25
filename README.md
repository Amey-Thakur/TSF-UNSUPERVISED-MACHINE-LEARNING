<div align="center">

  <a name="readme-top"></a>
  # Unsupervised Machine Learning
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Technology](https://img.shields.io/badge/Technology-Python%20%7C%20Scikit--Learn-blueviolet)](https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING)
  [![Developed by Amey Thakur and Mega Satish](https://img.shields.io/badge/Developed%20by-Amey%20Thakur%20%26%20Mega%20Satish-blue.svg)](https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING)

  A clustering analysis demonstrating the application of **K-Means Algorithm** to identify optimum clusters in the Iris dataset and visualize the underlying patterns.
  
  **[Google Colab](https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING/blob/main/Source%20Code/TSF_INTERNSHIP_TASK_2_UNSUPERVISED_LEARNING.ipynb)** &nbsp;·&nbsp; **[Kaggle Notebook](https://www.kaggle.com/ameythakur20/tsf-internship-task-2-unsupervised-learning)**

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Methodology](#methodology) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#results) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  <a name="authors"></a>
  ## Authors

  | <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) | <a href="https://github.com/msatmod"><img src="Mega/Mega.png" width="150" height="150" alt="Mega Satish"></a><br>[**Mega Satish**](https://github.com/msatmod)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--1844--9557-green.svg)](https://orcid.org/0000-0002-1844-9557) |
  | :---: | :---: |

</div>

> [!IMPORTANT]
> ### 🤝🏻 Special Acknowledgement
> *Special thanks to **[Mega Satish](https://github.com/msatmod)** for her meaningful contributions, guidance, and support that helped shape this work.*

---

<!-- OVERVIEW -->
<a name="overview"></a>
## Overview

**Unsupervised Machine Learning - Task 2** is a core Data Science exploration conducted under the **Graduate Rotational Internship Program (GRIP)** at **The Sparks Foundation**. The project focuses on the **Iris Dataset** to predict the optimum number of clusters and represent them visually.

By leveraging the **K-Means Clustering** algorithm, the system iteratively partitions data points into $K$ distinct non-overlapping subgroups (clusters) where each data point belongs to the cluster with the nearest mean.

### Computational Objectives
The analysis is governed by strict **exploratory principles** ensuring cluster validity:
*   **Elbow Method**: Determining the optimal value of $K$ by plotting the Within-Cluster Sum of Squares (WCSS).
*   **Cluster Centroids**: Computing the central vector for each species group.
*   **Dimensionality Visualization**: Plotting the classified clusters in a 2D feature space.

---

<!-- FEATURES -->
<a name="methodology"></a>
## Methodology & Features

| Component | Technical Description |
|-----------|-----------------------|
| **Ingestion Pipeline** | Automated data retrieval and parsing using **Pandas** for the Iris dataset. |
| **Optimal K Selection** | Implementation of the **Elbow Method** to minimize WCSS/Inertia. |
| **Model Architecture** | application of `KMeans` from **Scikit-Learn** for centroid initialization and fitting. |
| **Visualization** | Scatter plotting of clusters and centroids using **Matplotlib**. |
| **Cluster Prediction** | Assigning new sample points to the nearest established cluster. |

### Tech Stack
- **Runtime**: Python 3.x
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Machine Learning**: Scikit-Learn (sklearn)
- **Environment**: Jupyter Notebook / Google Colab

---

<!-- STRUCTURE -->
<a name="project-structure"></a>
## Project Structure

```python
TSF-UNSUPERVISED-MACHINE-LEARNING/
│
├── docs/                                            # Technical Documentation
│   └── SPECIFICATION.md                             # Architecture & Design Specification
│
├── Mega/                                            # Archival Attribution Assets
│   ├── Filly.jpg                                    # Companion (Filly)
│   ├── Mega.png                                     # Author Profile Image (Mega Satish)
│   └── ...                                          # Additional Attribution Files
│
├── Source Code/                                     # Core Implementation
│   └── TSF_INTERNSHIP_TASK_2_UNSUPERVISED_LEARNING.ipynb  # Jupyter Notebook (Analysis Kernel)
│   └── Iris.csv                                     # Empirical Data Source
│
├── screenshots/                                     # Result Visualization (Empty for setup)
│
├── .gitattributes                                   # Git configuration
├── .gitignore                                       # Repository Filters
├── CITATION.cff                                     # Scholarly Citation Metadata
├── codemeta.json                                    # Machine-Readable Project Metadata
├── LICENSE                                          # MIT License Terms
├── README.md                                        # Project Documentation
└── SECURITY.md                                      # Security Policy
```

---

<!-- RESULTS -->
<a name="results"></a>
## Results

<div align="center">
  <i>Detailed visualization results to be added.</i>
  <br>
  <!-- Placeholders for screenshots -->
</div>

---

<!-- QUICK START -->
<a name="quick-start"></a>
## Quick Start

### 1. Prerequisites
- **Python 3.7+**: Required for runtime execution. [Download Python](https://www.python.org/downloads/)
- **Jupyter Environment**: For interactive code execution (JupyterLab or Notebook).

> [!WARNING]
> **Data Path Integrity**
>
> The analysis kernel relies on relative file paths. Ensure `Iris.csv` remains accessible to the notebook. Modifying the directory structure without updating the ingestion logic will result in `FileNotFoundError` during runtime.

### 2. Installation
Establish the local environment by cloning the repository and installing the computational stack:

```bash
# Clone the repository
git clone https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING.git
cd TSF-UNSUPERVISED-MACHINE-LEARNING

# Install clustering dependencies
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Execution
Launch the analysis kernel to reproduce the findings:
```bash
jupyter notebook "Source Code/TSF_INTERNSHIP_TASK_2_UNSUPERVISED_LEARNING.ipynb"
```

---

<!-- LICENSE -->
<a name="license"></a>
## License

This academic submission, developed for the **Graduate Rotational Internship Program (GRIP)** at **The Sparks Foundation**, is made available under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original authors.

Copyright © 2021 Amey Thakur & Mega Satish

---

<!-- ABOUT -->
<a name="about-this-repository"></a>
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur) & [Mega Satish](https://github.com/msatmod)  
**Role**: Data Science & Business Analytics Interns  
**Program**: Graduate Rotational Internship Program (GRIP)  
**Organization**: [The Sparks Foundation](https://www.thesparksfoundationsingapore.org/)

This project features **Unsupervised Machine Learning - Task 2**, a clustering analytics study conducted as part of the **GRIP Internship**. It explores the application of K-Means to solve grouping problems.

**Connect:** [GitHub](https://github.com/Amey-Thakur) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/amey-thakur) &nbsp;·&nbsp; [ORCID](https://orcid.org/0000-0001-5644-1575)

### Acknowledgments

Grateful acknowledgment to [**Mega Satish**](https://github.com/msatmod) for her exceptional collaboration and scholarly partnership during the execution of this data science internship task. Her analytical precision, deep understanding of clustering algorithms, and constant support were instrumental in refining the models used in this study. Working alongside her was a transformative experience; her thoughtful approach to problem-solving and steady encouragement turned complex analytical challenges into meaningful learning moments. This work reflects the growth and insights gained from our side-by-side academic journey. Thank you, Mega, for everything you shared and taught along the way.

Special thanks to the **mentors at The Sparks Foundation** for providing this platform for rapid skill development and industrial exposure.

---

<div align="center">

  [↑ Back to Top](#readme-top)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Methodology](#methodology) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#results) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  📈 **[TSF-UNSUPERVISED-MACHINE-LEARNING](https://github.com/Amey-Thakur/TSF-UNSUPERVISED-MACHINE-LEARNING)**

  ---

  ### Presented as part of the Internship @ The Sparks Foundation

  ---

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
