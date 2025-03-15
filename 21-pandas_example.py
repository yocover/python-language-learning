# 使用python 中的第三方库 pandas
# pandas 是一个数据分析库
# 它提供了大量的数据结构和数据分析方法
import pandas as pd
from sqlalchemy import create_engine

# 连接数据库
# 使用 PostgreSQL 数据库连接
engine = create_engine("postgresql://user:password@localhost:5432/python_learning_db")

# 测试数据库是否连接成功
try:
    with engine.connect() as connection:
        print("数据库连接成功")
except Exception as e:
    print(f"数据库连接失败: {e}")

# # 读取数据库中的数据
df = pd.read_sql_table("destination_table", con=engine)

df.to_json("destination_table.json")
print(df)

quit()

# 写入数据库
# df.to_sql("users", con=engine, if_exists="replace")


data = {
    "Name": ["Sally", "Mary", "John"],
    "Age": [50, 40, 30],
    "City": ["New York", "Paris", "Tokyo"],
}

df = pd.DataFrame(data)
print(df)

# 读取csv 文件

df_from_csv = pd.read_csv("source.csv")
print(df_from_csv)

# 写入csv 文件
df.to_csv("destination.csv", index=False)

# 写入excel
df_from_csv.to_excel("destination.xlsx", sheet_name="Source Data")

# 写入markdown
df_from_csv.to_markdown("destination.md")

df_from_csv.to_sql("destination_table", con=engine, if_exists="replace")
