import logging
import multiprocessing
import os
import sys
from enum import Enum
from typing import Optional

import typer
from typing_extensions import Annotated

from . import indexify_extractor, version
from .agent import DEFAULT_BATCH_SIZE
from .base_extractor import EXTRACTORS_PATH
from .list_extractors import list_extractors
from .packager import ExtractorPackager

cpu_count = multiprocessing.cpu_count()

typer_app = typer.Typer(
    help="indexify-extractor - CLI for running and packaging indexify extractors",
    pretty_exceptions_enable=False,
)

default_extractor_path = os.getenv("EXTRACTOR_PATH", None)


# Hack to get around buffered output when not run using interactive terminal in docker
# and to ensure that print statements are flushed immediately
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)


class DownloadMethod(str, Enum):
    direct = "direct"
    server_proxy = "server-proxy"


def print_version():
    print(f"indexify-extractor-sdk version {version.__version__}")


@typer_app.command(help="Describe the extractor")
def describe(extractor: str):
    try:
        indexify_extractor.describe_sync(extractor)
    except Exception as e:
        print(f"{e}")


@typer_app.command(help="Run the extractor locally on the given text or file")
def run_local(
    extractor: str = typer.Argument(
        default_extractor_path,
        help="The extractor name in the format 'module_name:class_name'. For example, 'mock_extractor:MockExtractor'.",
    ),
    text: Optional[str] = typer.Option(None, help="Text to extract from"),
    file: Optional[str] = typer.Option(None, help="File to extract from"),
):
    indexify_extractor.local(extractor, text, file)


@typer_app.command(help="Joins the extractors to the coordinator server")
def join_server(
    coordinator_addr: str = "localhost:8950",
    ingestion_addr: str = "localhost:8900",
    listen_port: int = typer.Option(
        0,
        help="The port to listen on for extractor API extract functions.",
    ),
    download_method: DownloadMethod = typer.Option(
        DownloadMethod.server_proxy,
        help="Method to download the content. Can be 'direct' to access storage url directly "
        "or 'server-proxy' to use ingestion server as proxy.",
    ),
    advertise_addr: str = typer.Option(
        None,
        help="Override advertise address.",
    ),
    workers: Annotated[
        int, typer.Option(help="number of worker processes for extraction")
    ] = 1,
    batch_size: Annotated[
        int, typer.Option(help="number of items to process in a batch")
    ] = DEFAULT_BATCH_SIZE,
    config_path: Optional[str] = typer.Option(
        None, help="Path to the TLS configuration file"
    ),
):
    print_version()

    # Check if any extractors are downloaded.
    if not os.path.isdir(EXTRACTORS_PATH):
        raise Exception(
            "No extractors found. Download extractors using the downloader."
        )

    print("workers ", workers)
    print("config path provided ", config_path)

    indexify_extractor.join(
        workers=workers,
        coordinator_addr=coordinator_addr,
        download_method=download_method,
        ingestion_addr=ingestion_addr,
        listen_port=listen_port,
        advertise_addr=advertise_addr,
        config_path=config_path,
        batch_size=batch_size,
    )


@typer_app.command(help="Package the extractor into a Docker image.")
def package(
    extractor: str = typer.Argument(
        ...,
        help="The extractor name in the format 'module_name:class_name'. For example, 'mock_extractor:MockExtractor'.",
    ),
    verbose: bool = typer.Option(False, "--verbose", help="Run in verbose mode."),
    dev: bool = typer.Option(False, "--dev", help="Run in development mode."),
    gpu: bool = typer.Option(False, "--gpu", help="Use GPU acceleration."),
    tofile: str = typer.Option(
        None, "--to-file", help="Write Dockerfile to a specific file"
    ),
):
    """
    Packages an extractor into a Docker image, including Dockerfile generation and tarball creation.
    """
    print_version()
    module_name, class_name = indexify_extractor.split_validate_extractor(extractor)
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)
    packager = ExtractorPackager(
        module_name=module_name,
        class_name=class_name,
        verbose=verbose,
        dev=dev,
        gpu=gpu,
        tofile=tofile,
    )
    packager.package()


@typer_app.command(help="Download an extractor with the given url")
def download(extractor_path: str = typer.Argument(..., help="Extractor Name")):
    from .downloader import download_extractor

    download_extractor(extractor_path)


@typer_app.command(name="version", help="Print the version of the SDK and the CLI")
def _version():
    print_version()


@typer_app.command(help="List all the available extractors")
def list(
    extractor_type: Optional[str] = typer.Option(
        None,
        "--type",
        help="Type of extractor(embedding, text, image, pdf, audio, video)",
    )
):
    list_extractors(extractor_type)


@typer_app.command(help="Check and prepare extractor in development for local testing")
def install_local(
    extractor: str = typer.Argument(
        default_extractor_path,
        help="The extractor name in the format module_name:class_name",
    ),
    install_system_dependencies: bool = typer.Option(
        False, help="Install system dependencies"
    ),
):
    indexify_extractor.install_local(
        extractor, install_system_dependencies=install_system_dependencies
    )
