import io
import torch
from PIL import Image
from typing import List
from pdf2image import convert_from_bytes
from transformers import DonutProcessor, VisionEncoderDecoderModel
from indexify_extractor_sdk import Content, Extractor, Feature

class DonutBaseV2(Extractor):
    name = "tensorlake/donutcord"
    description = "An extractor that let's you do Document Parsing."
    system_dependencies = ["poppler-utils", "protobuf-compiler"]
    input_mime_types = ["application/pdf", "image/jpeg", "image/png"]

    def __init__(self):
        super(DonutBaseV2, self).__init__()
        self.processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")
        self.model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-cord-v2")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def _convert_pdf_to_image(self, pdf_data):
        images = convert_from_bytes(pdf_data)
        return images[0].convert("RGB")

    def _convert_image_data_to_image(self, image_data):
        image = Image.open(io.BytesIO(image_data))
        return image.convert("RGB")

    def _process_document(self, image):
        # prepare inputs and generate output
        pixel_values = self.processor(image, return_tensors="pt").pixel_values
        task_prompt = "<s_cord-v2>"
        decoder_input_ids = self.processor.tokenizer(
            task_prompt, add_special_tokens=False, return_tensors="pt"
        ).input_ids

        outputs = self.model.generate(
            pixel_values.to(self.device),
            decoder_input_ids=decoder_input_ids.to(self.device),
            max_length=self.model.decoder.config.max_position_embeddings,
            early_stopping=True,
            pad_token_id=self.processor.tokenizer.pad_token_id,
            eos_token_id=self.processor.tokenizer.eos_token_id,
            use_cache=True,
            num_beams=1,
            bad_words_ids=[[self.processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True,
        )

        # postprocess
        sequence = self.processor.batch_decode(outputs.sequences)[0]
        sequence = sequence.replace(self.processor.tokenizer.eos_token, "").replace(
            self.processor.tokenizer.pad_token, ""
        )
        sequence = sequence.split("<s_cord-v2>", 1)[-1].strip()
        return self.processor.token2json(sequence), image

    def extract(self, content: Content, params = None) -> List[Content]:
        if is_pdf(content.data):
            image = self._convert_pdf_to_image(content.data)
        else:
            image = self._convert_image_data_to_image(content.data)

        data = self._process_document(image)[0]
        return [Content.from_text(str(data), features=[Feature.metadata(value=data, name="invoice_simple_donut")])]
    
    def sample_input(self) -> Content:
        return self.sample_invoice_pdf()

# Function to determine if the content is a PDF
def is_pdf(data):
    return data[:4] == b'%PDF'

# Testing block
if __name__ == "__main__":
    pdf_file_path = "/content/ex_sa_inv.pdf"  # Replace with your PDF file path
    image_file_path = "/content/ex_sa_inv.jpg"  # Replace with your image file path

    extractor = DonutBaseV2()

    with open(pdf_file_path, "rb") as file:
        pdf_data = file.read()
        pdf_content = Content(content_type="application/pdf", data=pdf_data)
        pdf_results = extractor.extract(pdf_content)
        print("PDF Extraction Results:", pdf_results)

    with open(image_file_path, "rb") as file:
        image_data = file.read()
        image_content = Content(content_type="image/jpeg", data=image_data)
        image_results = extractor.extract([image_content])
        print("Image Extraction Results:", image_results)
