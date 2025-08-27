# BentoProphet

A time series forecasting project demonstrating how to build inference APIs using Facebook's Prophet model with BentoML. This project provides two different approaches to serving Prophet models for time series forecasting.

## 📋 Overview

BentoProphet showcases two different patterns for serving time series forecasting models:

- **`fit_predict/`**: Train-and-predict service that trains a new Prophet model on each request
- **`predict/`**: Pre-trained model service that loads a saved model and makes predictions

Both services provide APIs for:
- Generating forecasts with confidence intervals
- Creating forecast visualization plots
- Analyzing forecast components (trend, seasonality, etc.)

## 🔧 Getting Started

### Option 1: Fit-and-Predict Service
Navigate to the `fit_predict/` directory for a service that trains models dynamically on each request.

### Option 2: Pre-trained Model Service  
Navigate to the `predict/` directory for a service that uses pre-trained models for faster inference.

## 🌐 Deployment

Both services can be deployed locally using `bentoml serve` or to BentoCloud for production use.

## 📖 Documentation

For detailed usage instructions and examples, see the README files in each service directory:

- [Fit-Predict Service Documentation](./fit_predict/README.md)
- [Pre-trained Model Service Documentation](./predict/README.md)

## 🤝 Contributing

This project is part of the BentoML examples collection. For contributions and issues, please refer to the [BentoML documentation](https://docs.bentoml.com/en/latest/examples/overview.html).

## 📄 License

This project is licensed under the MIT License.
