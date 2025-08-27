<div align="center">
    <h1 align="center">Time Series Forecasting with BentoML</h1>
</div>

This is a BentoML example project, demonstrating how to build a time series forecasting inference API that takes in time series data, trains a forecasting model, and makes predictions. The project uses Facebook's Prophet model for time series forecasting.

See [here](https://docs.bentoml.com/en/latest/examples/overview.html) for a full list of BentoML example projects.

## Install dependencies

```bash
git clone https://github.com/bentoml/BentoProphet.git
cd BentoProphet

# Recommend Python 3.11
pip install -r requirements.txt
```

## Run the BentoML Service

We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Service.

```bash
$ bentoml serve .

2024-01-08T09:07:28+0000 [INFO] [cli] Prometheus metrics for HTTP BentoServer from "service:ProphetService" can be accessed at http://localhost:3000/metrics.
2024-01-08T09:07:28+0000 [INFO] [cli] Starting production HTTP BentoServer from "service:ProphetService" listening on http://localhost:3000 (Press CTRL+C to quit)
```

The Service is accessible at [http://localhost:3000](http://localhost:3000/). You can interact with it using the Swagger UI or in other different ways:

**CURL - Train Model and Get Predictions**
To get the full dataframe for realistic prediction, you can download the csv from the official example given at https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv.

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"data": [{"ds": "2023-01-01", "y": 100}, {"ds": "2023-01-02", "y": 110}], "period": 30}' \
     http://localhost:3000/predict
```

**CURL - Get Forecast Plot**

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"data": [{"ds": "2023-01-01", "y": 100}, {"ds": "2023-01-02", "y": 110}], "period": 90}' \
     http://localhost:3000/plot \
     --output forecast_plot.png
```

**CURL - Get Components Plot**

```bash
curl -s \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"data": [{"ds": "2023-01-01", "y": 100}, {"ds": "2023-01-02", "y": 110}], "period": 365}' \
     http://localhost:3000/plot_components \
     --output components_plot.png
```

**Python client**

```python
import bentoml

with bentoml.SyncHTTPClient("http://localhost:3000") as client:
    # Sample time series data
    time_series_data = [
        {"ds": "2023-01-01", "y": 100},
        {"ds": "2023-01-02", "y": 110},
        {"ds": "2023-01-03", "y": 105},
        # ... more data points
    ]
    
    # Train model and get predictions for next 30 days
    forecast = client.predict(data=time_series_data, period=30)
    
    # Get forecast plot
    plot_image = client.plot(data=time_series_data, period=90)
    
    # Get components analysis
    components_plot = client.plot_components(data=time_series_data, period=365)
```

## Input Data Format

The service expects time series data in the following format:
- `data`: List of dictionaries containing time series data
  - `ds`: Date string in YYYY-MM-DD format
  - `y`: Numeric value for that date
- `period`: Number of days to forecast into the future

## Deploy to BentoCloud

After the Service is ready, you can deploy the application to BentoCloud for better management and scalability. [Sign up](https://www.bentoml.com/) if you haven't got a BentoCloud account.

Make sure you have [logged in to BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html), then run the following command to deploy it.

```bash
bentoml deploy .
```

Once the application is up and running on BentoCloud, you can access it via the exposed URL.
