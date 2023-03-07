**1.Download and install the environment:**

-   Clone project:
    -   **_git clone https://github.com/PhuNguyen1601/fastapi-mysql.git_** \*
    -   **_cd fastapi-mysql_**
-   Create env: **python -m venv envname**
-   Active env: **envname\Scripts\activate**
-   Install package: **python -r requirements.txt**
-   Start Project: **uvicorn main:app --reload**

**2.Project are divided into folder:**

-   Folder models: Create table database
-   Folder schemas: Create schemas for model
-   Folder routes: Project paths
-   File config/db.py: Connect to Mysql
