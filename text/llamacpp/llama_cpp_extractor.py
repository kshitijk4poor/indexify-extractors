from typing import List, Tuple
from indexify_extractor_sdk.base_extractor import Feature
from pydantic import BaseModel, Field
from llama_cpp import Llama
from indexify_extractor_sdk import Extractor, Content

class ModelConfig(BaseModel):
    model: str = Field(default='microsoft/Phi-3-mini-4k-instruct-gguf')
    filename: str = Field(default='*q4.gguf')
    system_prompt: str = Field(default='You are a helpful assistant.')
    max_tokens: int = Field(default=4000)
    n_ctx: int = Field(default=2048)

class LlamaCppExtractor(Extractor):
    name = "tensorlake/llama_cpp"
    description = "An extractor that let's you use LLMs from Llama CPP."
    input_mime_types = ["text/plain", "application/json"]

    def __init__(self):
        super(LlamaCppExtractor, self).__init__()
        self._models = {}

    def extract(self, content: Content, params: ModelConfig) -> List[Content]:
        model = params.model
        filename = params.filename
        system_prompt = params.system_prompt
        user_input = content.data.decode("utf-8")

        if model not in self._models:
            self._models[model] = Llama.from_pretrained(repo_id=model, filename=filename, verbose=False, n_ctx=params.n_ctx)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
        try:
            response = self._models[model].create_chat_completion(messages, max_tokens=params.max_tokens)
        except Exception as e:
            print(f"exception calling llama.cpp {e}")
        result = response["choices"][0]["message"]["content"]
        return [Content.from_text(result)]
    
    def sample_input(self) -> Content:
        return Content.from_text("How to create a chatbot in Python?")
    

if __name__ == "__main__":
    extractor = LlamaCppExtractor()
    content = extractor.sample_input()
    params = ModelConfig(max_tokens=256)
    print(extractor.extract(content, params))
