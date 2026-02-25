from pydantic import BaseModel
from typing import List, Union


class PredictionInput(BaseModel):
    input: List[List[Union[str, float, int]]]


class PredictionOutput(BaseModel):
    prediction: List[float]