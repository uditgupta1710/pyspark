# pyspark
Pyspark playground

To run **PySpark on Windows**, follow these detailed steps:

---

## ✅ Step-by-Step Guide to Run PySpark on Windows

### 🔧 Prerequisites

Ensure the following are installed:

| Tool         | Version               | Install Link                                                                 |
| ------------ | --------------------- | ---------------------------------------------------------------------------- |
| Python       | 3.8+                  | [python.org](https://www.python.org/downloads/)                              |
| Java (JDK)   | 8 or 11 (recommended) | [oracle.com](https://www.oracle.com/java/technologies/javase-downloads.html) |
| Spark        | 3.x (with Hadoop 3.x) | [spark.apache.org](https://spark.apache.org/downloads.html)                  |
| WinUtils.exe | For Hadoop on Windows | [winutils guide below](#winutils-exe-setup)                                  |

---

## 📥 1. Install Python

Install from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
Make sure to **check "Add Python to PATH"** during installation.

Test:

```bash
python --version
```

---

## ☕ 2. Install Java JDK

Install Java 8 or 11, and set `JAVA_HOME` (as shown in previous answer).
Test:

```bash
java -version
```

---

## ⚡ 3. Download Apache Spark

1. Go to: [https://spark.apache.org/downloads/](https://spark.apache.org/downloads/)
2. Choose:

   * Spark version: 3.x
   * Package type: **Pre-built for Hadoop 3.x**
3. Extract the ZIP to a folder, e.g., `C:\spark`

---

## 🔧 4. WinUtils.exe Setup (for Hadoop)

1. Create folder:

   ```
   C:\hadoop\bin
   ```

2. Download `winutils.exe` from:

   * [https://github.com/steveloughran/winutils](https://github.com/steveloughran/winutils)
     or direct repo mirrors.

3. Place it in `C:\hadoop\bin`.

4. Set environment variable:

   * `HADOOP_HOME = C:\hadoop`

---

## ⚙️ 5. Set Environment Variables

Add these system environment variables:

| Variable      | Value                                 |
| ------------- | ------------------------------------- |
| `JAVA_HOME`   | `C:\Program Files\Java\jdk-<version>` |
| `SPARK_HOME`  | `C:\spark`                            |
| `HADOOP_HOME` | `C:\hadoop`                           |

Update `Path` and add:

```
%JAVA_HOME%\bin
%SPARK_HOME%\bin
%HADOOP_HOME%\bin
```

---

## 📦 6. Install PySpark

Run in CMD or PowerShell:

```bash
pip install pyspark
```

---

## ▶️ 7. Run PySpark

### Option 1: Interactive Shell

```bash
pyspark
```

### Option 2: Python Script

Create `example.py`:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()
df = spark.createDataFrame([(1, 'Alice'), (2, 'Bob')], ['id', 'name'])
df.show()
```

Run:

```bash
python example.py
```

---

## ✅ Verify

You should see Spark logs and output like:

```
+---+-----+
| id| name|
+---+-----+
|  1|Alice|
|  2|  Bob|
+---+-----+
```

---
# PySpark Tutorial for Beginners - Jupyter Notebooks

Welcome to the PySpark Tutorial for Beginners GitHub repository! This repository contains a collection of Jupyter notebooks used in my comprehensive [YouTube video: PySpark tutorial for beginners](https://youtu.be/EB8lfdxpirM). These notebooks provide hands-on examples and code snippets to help you understand and practice PySpark concepts covered in the tutorial video.

If you find this tutorial helpful, consider sharing this video with your friends and colleagues to help them unlock the power of PySpark and unlock the following bonus videos.

🎁 Bonus Videos:
- Hit **50,000 views** to unlock a video about building an **end-to-end machine-learning pipeline with PySpark**. 
- Hit **100,000 views** to unlock another video video about **end-to-end spark streaming**.

Do you like this tutorial? Why not check out my other video of [Airflow Tutorial for Beginners](https://youtu.be/K9AnJ9_ZAXE), which has more than **350k views 👀** and around **7k likes 👍**.

Don't forget to subscribe to my [YouTube channel](https://www.youtube.com/c/coder2j) and [my blog](https://coder2j.com/) for more exciting tutorials like this. And connect me on [X/Twitter](https://twitter.com/coder2j) and [Linkedin](https://www.linkedin.com/in/coder2j/), I post content there regularly too. Thank you for your support! ❤️


## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Notebook Descriptions](#notebook-descriptions)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In our [PySpark tutorial video](https://youtu.be/EB8lfdxpirM), we covered various topics, including Spark installation, SparkContext, SparkSession, RDD transformations and actions, Spark DataFrames, Spark SQL, and more. These Jupyter notebooks are designed to complement the video content, allowing you to follow along, experiment, and practice your PySpark skills.

## Getting Started

To get started with the Jupyter notebooks, follow these steps:

1. Clone this GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/coder2j/pyspark-tutorial.git
   ```

2. Ensure you have Python and Jupyter Notebook installed on your machine.

3. Follow the YouTube video part 2: Spark Installation to make sure Spark has been installed on your machine.

4. Launch Jupyter Notebook by running:

   ```bash
   jupyter notebook
   ```

5. Open the notebook you want to work on and start experimenting with PySpark.

## Notebook Descriptions

- **Notebook 1 - 01-PySpark-Get-Started**: Instructions and commands for setting the PySpark environment variables to use spark in jupyter notebook.

- **Notebook 2 - 02-Create-SparkContext**: Creating SparkContext objects in different PySpark versions.


- **Notebook 3 - 03-Create-SparkSession.ipynb**: Creating SparkSession objects in PySpark.

- **Notebook 4 - 04-RDD-Operations.ipynb**: Creating RDD and Demonstrating RDD transformations and actions.

- **Notebook 5 - 05-DataFrame-Intro.ipynb**: Introduction to Spark DataFrames and differences compared to RDD.

- **Notebook 6 - 06-DataFrame-from-various-data-source.ipynb**: Creating Spark Dataframe from various data sources.

- **Notebook 7 - 07-DataFrame-Operations.ipynb**: Performing Spark Dataframe operations like filtering, aggregation, etc.

- **Notebook 8 - 08-Spark-SQL.ipynb**: Converting Spark Dataframe to a temporary table or view and performing SQL operations using Spark SQL.

Feel free to explore and run these notebooks at your own pace.

## Prerequisites

To make the most of these notebooks, you should have the following prerequisites:

- Basic knowledge of Python programming.

- Understanding of data processing concepts (though no prior PySpark experience is required).

## Usage

These notebooks are meant for self-learning and practice. Follow along with the [tutorial video](https://youtu.be/EB8lfdxpirM) to gain a deeper understanding of PySpark concepts. Experiment with the code, modify it and try additional exercises to solidify your skills.

## Contributing

If you'd like to contribute to this repository by adding more notebooks, improving documentation, or fixing issues, please feel free to fork the repository, make your changes, and submit a pull request. We welcome contributions from the community!

## License

This project is licensed under the [MIT License](LICENSE.md).
