import pandas as pd

# Путь к локальному raw файлу
RAW_FILE = "data/raw/default_of_credit_card_clients.xls"

# Загружаем полный датасет
df = pd.read_excel(RAW_FILE)

# Берём случайные 500 строк для sample (не трогаем исходный файл)
sample_df = df.sample(500, random_state=42)

# Сохраняем sample в папку data/samples
sample_df.to_csv("data/samples/default_sample.csv", index=False)

print("Sample created: data/samples/default_sample.csv")