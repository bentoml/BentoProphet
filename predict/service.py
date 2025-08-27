import bentoml
import io
import pandas as pd
from prophet.serialize import model_from_json
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
    model_ref = bentoml.models.BentoModel("prophet_model:latest")

    def __init__(self) -> None:
        with open(f"{self.model_ref.path}/model.json") as fin:
            self.model = model_from_json(fin.read())

    @bentoml.api()
    def predict(self, period: int = 365) -> pd.DataFrame:
        future = self.model.make_future_dataframe(periods=period)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(period)

    @bentoml.api()
    def plot(self, period: int = 365) -> Image:
        future = self.model.make_future_dataframe(periods=period)
        forecast = self.model.predict(future)
        fig = self.model.plot(forecast)

        return fig_to_pil(fig)

    @bentoml.api()
    def plot_components(self, period: int = 365) -> Image:
        future = self.model.make_future_dataframe(periods=period)
        forecast = self.model.predict(future)
        fig = self.model.plot_components(forecast)

        return fig_to_pil(fig)
