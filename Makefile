gen-proto:
	python -m grpc_tools.protoc -I../indexify/protos --python_out=extractor-sdk/indexify_extractor_sdk/ --pyi_out=extractor-sdk/indexify_extractor_sdk/ --grpc_python_out=extractor-sdk/indexify_extractor_sdk/ ../indexify/protos/coordinator_service.proto
