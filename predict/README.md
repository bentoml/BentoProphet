<div align="center">
    <h1 align="center">Serving Prophet with BentoML</h1>
</div>

[Prophet](https://facebook.github.io/prophet/) is a forecasting procedure implemented in R and Python. It is fast and provides completely automated forecasts that can be tuned by hand by data scientists and analysts. This is a BentoML example project, demonstrating how to build a time series forecasting inference API using Facebook's Prophet model.

See [here](https://docs.bentoml.com/en/latest/examples/overview.html) for a full list of BentoML example projects.

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoProphet.git
cd BentoProphet

# Recommend Python 3.11
pip install -r requirements.txt
```

## Train and Save the Model

Before running the service, you need to train and save the Prophet model:

```bash
python save_model.py
```

This script will:
- Download sample data (Peyton Manning Wikipedia page views)
- Train a Prophet model on the time series data
- Save the model using BentoML's model store

## Run the BentoML Service

We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Service.

```bash
$ bentoml serve .

2024-01-08T09:07:28+0000 [INFO] [cli] Prometheus metrics for HTTP BentoServer from "service:ProphetService" can be accessed at http://localhost:3000/metrics.
2024-01-08T09:07:28+0000 [INFO] [cli] Starting production HTTP BentoServer from "service:ProphetService" listening on http://localhost:3000 (Press CTRL+C to quit)
Prophet model loaded successfully
```

The Service is accessible at [http://localhost:3000](http://localhost:3000/). You can interact with it using the Swagger UI or in other different ways:

**CURL - Get Predictions**

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"period": 30}' \
     http://localhost:3000/predict
```

**CURL - Get Forecast Plot**

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"period": 90}' \
     http://localhost:3000/plot \
     --output forecast_plot.png
```

**CURL - Get Components Plot**

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"period": 365}' \
     http://localhost:3000/plot_components \
     --output components_plot.png
```

**Python client**

```python
import bentoml

with bentoml.SyncHTTPClient("http://localhost:3000") as client:
    # Get predictions for next 30 days
    forecast = client.predict(period=30)
    
    # Get forecast plot
    plot_image = client.plot(period=90)
    
    # Get components analysis
    components_plot = client.plot_components(period=365)
```

## Deploy to BentoCloud

After the Service is ready, you can deploy the application to BentoCloud for better management and scalability. [Sign up](https://www.bentoml.com/) if you haven't got a BentoCloud account.

Make sure you have [logged in to BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html), then run the following command to deploy it.

```bash
bentoml deploy .
```

Once the application is up and running on BentoCloud, you can access it via the exposed URL.
