import json
from typing import List, Optional, Union

import cv2
import numpy as np
from indexify_extractor_sdk import Content, Extractor, Feature
from pydantic import BaseModel, Field
from ultralytics import YOLO


class YoloExtractorConfig(BaseModel):
    model_name: str = Field(default="yolov8n.pt")
    conf: float = Field(default=0.25)
    iou: float = Field(default=0.7)


class YoloExtractor(Extractor):
    name = "tensorlake/yolo-extractor"
    description = "An extractor that uses YOLO for object detection in images."
    system_dependencies = ["libsm6", "libglib2.0-0", "libxext6", "libgl1-mesa-glx"]
    input_mime_types = ["image/jpeg", "image/png"]

    def __init__(self):
        super(YoloExtractor, self).__init__()
        self._models = {}

    def extract(
        self, content: Content, params: YoloExtractorConfig
    ) -> List[Union[Feature, Content]]:
        contents = []

        # Load the YOLO model
        if params.model_name not in self._models:
            self._models[params.model_name] = YOLO(params.model_name)

        # Decode the image data
        nparr = np.frombuffer(content.data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Run inference
        results = self._models[params.model_name](img, conf=params.conf, iou=params.iou)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                class_id = int(box.cls)
                class_name = result.names[class_id]
                confidence = float(box.conf)

                detection = {
                    "bbox": [x1, y1, x2, y2],
                    "class": class_name,
                    "score": confidence,
                }

                contents.append(
                    Content(content_type="application/json", data=json.dumps(detection))
                )

        return contents

    def sample_input(self) -> Content:
        return self.sample_jpg()


if __name__ == "__main__":
    with open("test_image.jpg", "rb") as f:
        image_data = f.read()
    input_content = Content(content_type="image/jpeg", data=image_data)
    input_params = YoloExtractorConfig()
    extractor = YoloExtractor()
    results = extractor.extract(input_content, params=input_params)
