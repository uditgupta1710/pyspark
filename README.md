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

## Need GUI?

Install **Jupyter**:

```bash
pip install notebook
```

Then run:

```bash
jupyter notebook
```

And use PySpark inside a notebook.

---

Let me know if you want a **Conda-based setup**, or to run PySpark on **Windows Subsystem for Linux (WSL)** instead.
