from dotenv import load_dotenv
load_dotenv()

import pandas as pd
df = pd.read_csv("dataset.csv")

examples = [{"inputs": {"question": row["user_input"]},
             "outputs": {"answer": row["reference"]}} for _, row in df.iterrows()]

from langsmith import Client
client = Client()

dataset = client.create_dataset(
    dataset_name="AGENT_DATASET", description="dataset for AI trends"
)

client.create_examples(dataset_id=dataset.id, examples=examples)
