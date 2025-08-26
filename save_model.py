import pandas as pd
from prophet import Prophet
from prophet.serialize import model_to_json
import bentoml

# Train the Model
df = pd.read_csv(
    "https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv"
)
m = Prophet()
m.fit(df)


# Save the Model
with bentoml.models.create(
    name="prophet_model",
) as model_ref:
    with open(f"{model_ref.path}/model.json", "w") as fout:
        fout.write(model_to_json(m))
