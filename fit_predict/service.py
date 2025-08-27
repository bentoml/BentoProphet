import bentoml
import io
import pandas as pd
from prophet import Prophet
from PIL import Image as PILImage
from PIL.Image import Image

import matplotlib as plt

plt.use("Agg")  # Use a non-interactive backend


# Convert to PIL Image
def fig_to_pil(fig):
    """Convert matplotlib figure to PIL Image"""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, bbox_inches="tight")
    buf.seek(0)
    pil_img = PILImage.open(buf)
    return pil_img

image = bentoml.images.Image(python_version="3.11").requirements_file("requirements.txt")

@bentoml.service(image=image)
class ProphetService:

    @bentoml.api()
    def train_and_predict(self, data: pd.DataFrame, period: int = 365) -> pd.DataFrame:
        """
        Train a Prophet model on the provided data and make predictions
        
        Args:
            data: DataFrame with 'ds' (date) and 'y' (target) columns
            period: Number of days to predict into the future
        """
        # Initialize and train the model
        model = Prophet()
        model.fit(data)
        
        # Make predictions
        future = model.make_future_dataframe(periods=period)
        forecast = model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(period)

    @bentoml.api()
    def plot(self, data: pd.DataFrame, period: int = 365) -> Image:
        """
        Train a Prophet model and generate a plot of the forecast
        
        Args:
            data: DataFrame with 'ds' (date) and 'y' (target) columns
            period: Number of days to predict into the future
        """
        # Initialize and train the model
        model = Prophet()
        model.fit(data)
        
        # Make predictions and plot
        future = model.make_future_dataframe(periods=period)
        forecast = model.predict(future)
        fig = model.plot(forecast)

        return fig_to_pil(fig)

    @bentoml.api()
    def plot_components(self, data: pd.DataFrame, period: int = 365) -> Image:
        """
        Train a Prophet model and generate component plots of the forecast
        
        Args:
            data: DataFrame with 'ds' (date) and 'y' (target) columns
            days: Number of days to predict into the future
        """
        # Initialize and train the model
        model = Prophet()
        model.fit(data)
        
        # Make predictions and plot components
        future = model.make_future_dataframe(periods=period)
        forecast = model.predict(future)
        fig = model.plot_components(forecast)

        return fig_to_pil(fig)
