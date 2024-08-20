# Indexify Extractors

## Overview

Extractors are modules that give Indexify data processing capabilities such as metadata or embedding extraction from document, videos and audio. This repository hosts a collection of extractors for Indexify.

For the main Indexify project, visit: [Indexify Main Repository](https://github.com/diptanu/indexify).

## Available Extractors
We have built some extractors based on demand from our users. You can write a new or a custom extractor for your use-case too, instructions for writing new extractors are below.

* [Embedding Extractors](https://github.com/tensorlakeai/indexify-extractors/tree/main/embedding)
* [Video Extractors](https://github.com/tensorlakeai/indexify-extractors/tree/main/video)
* [Invoice Extractors](https://github.com/tensorlakeai/indexify-extractors/tree/main/invoices)
* [Audio Extractors](https://github.com/tensorlakeai/indexify-extractors/tree/main/whisper-asr)
* [PDF Extractors](https://github.com/tensorlakeai/indexify-extractors/tree/main/pdf)

## Usage
#### Install
```bash
pip install indexify-extractor-sdk
```

#### List Available extractors
```bash
indexify-extractor list
```

#### Download an Extractor
Find the name of the extractor you want.
```bash
indexify-extractor download tensorlake/minilm-l6
```

#### Load and Run in Notebook or Python Applications
```python
from indexify_extractor_sdk import load_extractor, Content
extractor, config_cls = load_extractor("indexify_extractors.minilm-l6.minilm_l6:MiniLML6Extractor")
content = Content.from_text("hello world")
out = extractor.extract(content)
```

Extractors can be parameterized when they are called. The input parameters are Pydantic Models. Inspect the config class programatically or in the docs of the corresponding extractor -
```python
ex, config = load_extractor("indexify_extractors.chunking.chunk_extractor:ChunkExtractor")
config.schema()
#{'properties': {'overlap': {'default': 0, 'title': 'Overlap', 'type': 'integer'}, 'chunk_size': {'default': 100, 'title': 'Chunk Size', 'type': 'integer'}, 'text_splitter': {'default': 'recursive', 'enum': ['char', 'recursive', 'markdown', 'html'], 'title': 'Text Splitter', 'type': 'string'}, 'headers_to_split_on': {'default': [], 'items': {'type': 'string'}, 'title': 'Headers To Split On', 'type': 'array'}}, 'title': 'ChunkExtractionInputParams', 'type': 'object'}
```

#### Extract Locally on shell -
```bash
indexify-extractor run-local indexify_extractors.minilm-l6.minilm_l6:MiniLML6Extractor --text "hello world" // or --file
```

#### Run Extractors as a Service for Continous Extraction and Indexing with Indexify Server
To run the extractor with Indexify's control plane such that it can continuously extract from content -
```bash
indexify-extractor join-server --coordinator-addr localhost:8950 --ingestion-addr localhost:8900
```
The `coordinator-addr` and `ingestion-addr` above are the default addresses exposed by the Indexify server to get extraction instructions and to upload extracted data, they can be configured in the server configuration.

## Build a new Extractor
If want to build a new extractor to give Indexify new data processing capabilities you can write a new extractor by cloning this repository - https://github.com/tensorlakeai/indexify-extractor-template

#### Clone the template
```shell
curl https://codeload.github.com/tensorlakeai/indexify-extractor-template/tar.gz/main | tar -xz  indexify-extractor-template-main
```

#### Implement the extractor interface
```python
class InputParams(BaseModel):
    a: int = 0
    b: str = ""


class MyExtractor(Extractor):
    name = "yourorgname/myextractor"
    description = "Description of the extractor goes here."
    system_dependencies = []
    input_mime_types = ["text/plain"]

    def __init__(self):
        super().__init__()

    def extract(self, content: Content, params: InputParams) -> List[Union[Feature, Content]]:
        return [
            Content.from_text(
                text="Hello World", features=[Feature.embedding(values=[1, 2, 3])]
            ),
            Content.from_text(
                text="Pipe Baz", features=[Feature.embedding(values=[1, 2, 3])]
            ),
            Content.from_text(
                text="Hello World",
                features=[Feature.metadata({"key": "value"})],
            ),
        ]

    def sample_input(self) -> Tuple[Content, Type[BaseModel]]:
        Content.from_text(text="Hello World")
```

All the Python dependencies of the extractor goes into `requirements.txt` file adjacent to the extractor file.

Once you have developed the extractor you can test the extractor locally by running the `indexify-extractor run-local` command as described above.

#### Test and Deploy the extractor
You can test your extractor without running the Indexify server!
```python
ex, config = load_extractor("custom_extractor:MyExtractor")
config.schema()
ex.extract(Content(...), config(...))# or ignore config if you don't have config
```
Run the extractor on shell
```bash
indexify-extractor run-local custom_extractor:MyExtractor --text "hello world" // or --file /path to file
```

#### Install your Extractor
You can install your extractor locally
```bash
indexify-extractor install-local custom_extractor:MyExtractor
```

When you are ready to deploy the extractor in production, package the extractor and deploy as many instances you want on your cluster for parallelism, and point it to the indexify server.
```
indexify-extractor join-server --coordinator-addr localhost:8950 --ingestion-addr localhost:8900
```

#### Package the Extractor
Once you build a new extractor, and have tested it and it's time to deploy this in production, you can build a container with the extractor -
```bash
indexify-extractor package indexify_extractors.<folder_name>.custom_extractor:MyExtractor
```

If you want to package an extractor in a container that support Nvidia CUDA GPU, you can pass the `--gpu` flag to the package command.

#### Running Your packaged extractor
To run your packaged extractor image you can run the following command
```bash
docker run ExtractorImageName indexify-extractor join-server --coordinator-addr=host.docker.internal:8950 --ingestion-addr=host.docker.internal:8900
```

If you have a GPU enabled extractor, you might need to set up your machine to support running the container with the GPU. This might involve installing the Nvidia Container Toolkit and setting up the Nvidia runtime for Docker. You can find more information on how to do this in the [Nvidia Container Toolkit Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html).

Finally, to run your GPU enabled extractor, you can add the `--gpus all` flag to the `docker run` command.
