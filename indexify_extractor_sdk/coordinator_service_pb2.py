# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coordinator_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19\x63oordinator_service.proto\x12\x14indexify_coordinator"1\n\x19GetContentMetadataRequest\x12\x14\n\x0c\x63ontent_list\x18\x01 \x03(\t"Y\n\x1aGetContentMetadataResponse\x12;\n\x0c\x63ontent_list\x18\x01 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"\xaa\x01\n\x11UpdateTaskRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x32\n\x07outcome\x18\x03 \x01(\x0e\x32!.indexify_coordinator.TaskOutcome\x12;\n\x0c\x63ontent_list\x18\x04 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"\x19\n\x17ListStateChangesRequest"k\n\x0bStateChange\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x13\n\x0b\x63hange_type\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\x04\x12\x14\n\x0cprocessed_at\x18\x05 \x01(\x04"N\n\x18ListStateChangesResponse\x12\x32\n\x07\x63hanges\x18\x01 \x03(\x0b\x32!.indexify_coordinator.StateChange"@\n\x10ListTasksRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x19\n\x11\x65xtractor_binding\x18\x02 \x01(\t">\n\x11ListTasksResponse\x12)\n\x05tasks\x18\x01 \x03(\x0b\x32\x1a.indexify_coordinator.Task"\x14\n\x12UpdateTaskResponse"3\n\x1eGetExtractorCoordinatesRequest\x12\x11\n\textractor\x18\x02 \x01(\t"0\n\x1fGetExtractorCoordinatesResponse\x12\r\n\x05\x61\x64\x64rs\x18\x01 \x03(\t"\'\n\x12ListIndexesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"C\n\x13ListIndexesResponse\x12,\n\x07indexes\x18\x01 \x03(\x0b\x32\x1b.indexify_coordinator.Index"2\n\x0fGetIndexRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t">\n\x10GetIndexResponse\x12*\n\x05index\x18\x01 \x01(\x0b\x32\x1b.indexify_coordinator.Index"@\n\x12\x43reateIndexRequest\x12*\n\x05index\x18\x02 \x01(\x0b\x32\x1b.indexify_coordinator.Index"\x15\n\x13\x43reateIndexResponse"z\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x19\n\x11\x65xtractor_binding\x18\x05 \x01(\t\x12\x11\n\textractor\x18\x06 \x01(\t"\x1e\n\tEmbedding\x12\x11\n\tembedding\x18\x01 \x03(\x02" \n\nAttributes\x12\x12\n\nattributes\x18\x02 \x01(\t"\x81\x01\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\tembedding\x18\x02 \x01(\x0b\x32\x1f.indexify_coordinator.Embedding\x12\x34\n\nattributes\x18\x03 \x01(\x0b\x32 .indexify_coordinator.Attributes"V\n\x07\x43ontent\x12\x0c\n\x04mime\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12/\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32\x1d.indexify_coordinator.Feature"p\n\x17RegisterExecutorRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x32\n\textractor\x18\x03 \x01(\x0b\x32\x1f.indexify_coordinator.Extractor"/\n\x18RegisterExecutorResponse\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t"\'\n\x10HeartbeatRequest\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t"S\n\x11HeartbeatResponse\x12\x13\n\x0b\x65xecutor_id\x18\x01 \x01(\t\x12)\n\x05tasks\x18\x02 \x03(\x0b\x32\x1a.indexify_coordinator.Task"\xeb\x02\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\textractor\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12?\n\x10\x63ontent_metadata\x18\x04 \x01(\x0b\x32%.indexify_coordinator.ContentMetadata\x12\x14\n\x0cinput_params\x18\x05 \x01(\t\x12\x19\n\x11\x65xtractor_binding\x18\x06 \x01(\t\x12P\n\x14output_index_mapping\x18\x07 \x03(\x0b\x32\x32.indexify_coordinator.Task.OutputIndexMappingEntry\x12\x32\n\x07outcome\x18\x08 \x01(\x0e\x32!.indexify_coordinator.TaskOutcome\x1a\x39\n\x17OutputIndexMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x17\n\x15ListExtractorsRequest"M\n\x16ListExtractorsResponse\x12\x33\n\nextractors\x18\x01 \x03(\x0b\x32\x1f.indexify_coordinator.Extractor"\xcd\x01\n\tExtractor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0cinput_params\x18\x03 \x01(\t\x12=\n\x07outputs\x18\x04 \x03(\x0b\x32,.indexify_coordinator.Extractor.OutputsEntry\x12\x18\n\x10input_mime_types\x18\x05 \x03(\t\x1a.\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"#\n\x13GetNamespaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"J\n\x14GetNamespaceResponse\x12\x32\n\tnamespace\x18\x01 \x01(\x0b\x32\x1f.indexify_coordinator.Namespace"\xc6\x01\n\x12ListContentRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12I\n\tlabels_eq\x18\x04 \x03(\x0b\x32\x36.indexify_coordinator.ListContentRequest.LabelsEqEntry\x1a/\n\rLabelsEqEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"R\n\x13ListContentResponse\x12;\n\x0c\x63ontent_list\x18\x01 \x03(\x0b\x32%.indexify_coordinator.ContentMetadata"(\n\x13ListBindingsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t"P\n\x14ListBindingsResponse\x12\x38\n\x08\x62indings\x18\x01 \x03(\x0b\x32&.indexify_coordinator.ExtractorBinding"`\n\x16\x43reateNamespaceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x08\x62indings\x18\x02 \x03(\x0b\x32&.indexify_coordinator.ExtractorBinding";\n\x17\x43reateNamespaceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03"\x16\n\x14ListNamespaceRequest"L\n\x15ListNamespaceResponse\x12\x33\n\nnamespaces\x18\x01 \x03(\x0b\x32\x1f.indexify_coordinator.Namespace"\xd7\x01\n\x10\x45xtractorBinding\x12\x11\n\textractor\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cinput_params\x18\x04 \x01(\t\x12\x44\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x33.indexify_coordinator.ExtractorBinding.FiltersEntry\x12\x16\n\x0e\x63ontent_source\x18\x06 \x01(\t\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"v\n\x14\x45xtractorBindRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x37\n\x07\x62inding\x18\x03 \x01(\x0b\x32&.indexify_coordinator.ExtractorBinding\x12\x12\n\ncreated_at\x18\x02 \x01(\x03"\xb2\x03\n\x15\x45xtractorBindResponse\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x32\n\textractor\x18\x02 \x01(\x0b\x32\x1f.indexify_coordinator.Extractor\x12h\n\x18index_name_table_mapping\x18\x04 \x03(\x0b\x32\x46.indexify_coordinator.ExtractorBindResponse.IndexNameTableMappingEntry\x12j\n\x19output_index_name_mapping\x18\x05 \x03(\x0b\x32G.indexify_coordinator.ExtractorBindResponse.OutputIndexNameMappingEntry\x1a<\n\x1aIndexNameTableMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a=\n\x1bOutputIndexNameMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8f\x02\n\x0f\x43ontentMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12\x0c\n\x04mime\x18\x04 \x01(\t\x12\x41\n\x06labels\x18\x05 \x03(\x0b\x32\x31.indexify_coordinator.ContentMetadata.LabelsEntry\x12\x13\n\x0bstorage_url\x18\x06 \x01(\t\x12\x12\n\ncreated_at\x18\x07 \x01(\x03\x12\x11\n\tnamespace\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"N\n\x14\x43reateContentRequest\x12\x36\n\x07\x63ontent\x18\x02 \x01(\x0b\x32%.indexify_coordinator.ContentMetadata"#\n\x15\x43reateContentResponse\x12\n\n\x02id\x18\x01 \x01(\t"S\n\tNamespace\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x08\x62indings\x18\x02 \x03(\x0b\x32&.indexify_coordinator.ExtractorBinding*3\n\x0bTaskOutcome\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x32\x9c\x0f\n\x12\x43oordinatorService\x12j\n\rCreateContent\x12*.indexify_coordinator.CreateContentRequest\x1a+.indexify_coordinator.CreateContentResponse"\x00\x12y\n\x12GetContentMetadata\x12/.indexify_coordinator.GetContentMetadataRequest\x1a\x30.indexify_coordinator.GetContentMetadataResponse"\x00\x12\x64\n\x0bListContent\x12(.indexify_coordinator.ListContentRequest\x1a).indexify_coordinator.ListContentResponse"\x00\x12j\n\rCreateBinding\x12*.indexify_coordinator.ExtractorBindRequest\x1a+.indexify_coordinator.ExtractorBindResponse"\x00\x12g\n\x0cListBindings\x12).indexify_coordinator.ListBindingsRequest\x1a*.indexify_coordinator.ListBindingsResponse"\x00\x12i\n\x08\x43reateNS\x12,.indexify_coordinator.CreateNamespaceRequest\x1a-.indexify_coordinator.CreateNamespaceResponse"\x00\x12\x63\n\x06ListNS\x12*.indexify_coordinator.ListNamespaceRequest\x1a+.indexify_coordinator.ListNamespaceResponse"\x00\x12`\n\x05GetNS\x12).indexify_coordinator.GetNamespaceRequest\x1a*.indexify_coordinator.GetNamespaceResponse"\x00\x12m\n\x0eListExtractors\x12+.indexify_coordinator.ListExtractorsRequest\x1a,.indexify_coordinator.ListExtractorsResponse"\x00\x12s\n\x10RegisterExecutor\x12-.indexify_coordinator.RegisterExecutorRequest\x1a..indexify_coordinator.RegisterExecutorResponse"\x00\x12\x62\n\tHeartbeat\x12&.indexify_coordinator.HeartbeatRequest\x1a\'.indexify_coordinator.HeartbeatResponse"\x00(\x01\x30\x01\x12\x64\n\x0bListIndexes\x12(.indexify_coordinator.ListIndexesRequest\x1a).indexify_coordinator.ListIndexesResponse"\x00\x12[\n\x08GetIndex\x12%.indexify_coordinator.GetIndexRequest\x1a&.indexify_coordinator.GetIndexResponse"\x00\x12\x64\n\x0b\x43reateIndex\x12(.indexify_coordinator.CreateIndexRequest\x1a).indexify_coordinator.CreateIndexResponse"\x00\x12\x88\x01\n\x17GetExtractorCoordinates\x12\x34.indexify_coordinator.GetExtractorCoordinatesRequest\x1a\x35.indexify_coordinator.GetExtractorCoordinatesResponse"\x00\x12\x61\n\nUpdateTask\x12\'.indexify_coordinator.UpdateTaskRequest\x1a(.indexify_coordinator.UpdateTaskResponse"\x00\x12s\n\x10ListStateChanges\x12-.indexify_coordinator.ListStateChangesRequest\x1a..indexify_coordinator.ListStateChangesResponse"\x00\x12^\n\tListTasks\x12&.indexify_coordinator.ListTasksRequest\x1a\'.indexify_coordinator.ListTasksResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "coordinator_service_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._options = None
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTOR_OUTPUTSENTRY"]._options = None
    _globals["_EXTRACTOR_OUTPUTSENTRY"]._serialized_options = b"8\001"
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._options = None
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTORBINDING_FILTERSENTRY"]._options = None
    _globals["_EXTRACTORBINDING_FILTERSENTRY"]._serialized_options = b"8\001"
    _globals["_EXTRACTORBINDRESPONSE_INDEXNAMETABLEMAPPINGENTRY"]._options = None
    _globals[
        "_EXTRACTORBINDRESPONSE_INDEXNAMETABLEMAPPINGENTRY"
    ]._serialized_options = b"8\001"
    _globals["_EXTRACTORBINDRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"]._options = None
    _globals[
        "_EXTRACTORBINDRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"
    ]._serialized_options = b"8\001"
    _globals["_CONTENTMETADATA_LABELSENTRY"]._options = None
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_options = b"8\001"
    _globals["_TASKOUTCOME"]._serialized_start = 4563
    _globals["_TASKOUTCOME"]._serialized_end = 4614
    _globals["_GETCONTENTMETADATAREQUEST"]._serialized_start = 51
    _globals["_GETCONTENTMETADATAREQUEST"]._serialized_end = 100
    _globals["_GETCONTENTMETADATARESPONSE"]._serialized_start = 102
    _globals["_GETCONTENTMETADATARESPONSE"]._serialized_end = 191
    _globals["_UPDATETASKREQUEST"]._serialized_start = 194
    _globals["_UPDATETASKREQUEST"]._serialized_end = 364
    _globals["_LISTSTATECHANGESREQUEST"]._serialized_start = 366
    _globals["_LISTSTATECHANGESREQUEST"]._serialized_end = 391
    _globals["_STATECHANGE"]._serialized_start = 393
    _globals["_STATECHANGE"]._serialized_end = 500
    _globals["_LISTSTATECHANGESRESPONSE"]._serialized_start = 502
    _globals["_LISTSTATECHANGESRESPONSE"]._serialized_end = 580
    _globals["_LISTTASKSREQUEST"]._serialized_start = 582
    _globals["_LISTTASKSREQUEST"]._serialized_end = 646
    _globals["_LISTTASKSRESPONSE"]._serialized_start = 648
    _globals["_LISTTASKSRESPONSE"]._serialized_end = 710
    _globals["_UPDATETASKRESPONSE"]._serialized_start = 712
    _globals["_UPDATETASKRESPONSE"]._serialized_end = 732
    _globals["_GETEXTRACTORCOORDINATESREQUEST"]._serialized_start = 734
    _globals["_GETEXTRACTORCOORDINATESREQUEST"]._serialized_end = 785
    _globals["_GETEXTRACTORCOORDINATESRESPONSE"]._serialized_start = 787
    _globals["_GETEXTRACTORCOORDINATESRESPONSE"]._serialized_end = 835
    _globals["_LISTINDEXESREQUEST"]._serialized_start = 837
    _globals["_LISTINDEXESREQUEST"]._serialized_end = 876
    _globals["_LISTINDEXESRESPONSE"]._serialized_start = 878
    _globals["_LISTINDEXESRESPONSE"]._serialized_end = 945
    _globals["_GETINDEXREQUEST"]._serialized_start = 947
    _globals["_GETINDEXREQUEST"]._serialized_end = 997
    _globals["_GETINDEXRESPONSE"]._serialized_start = 999
    _globals["_GETINDEXRESPONSE"]._serialized_end = 1061
    _globals["_CREATEINDEXREQUEST"]._serialized_start = 1063
    _globals["_CREATEINDEXREQUEST"]._serialized_end = 1127
    _globals["_CREATEINDEXRESPONSE"]._serialized_start = 1129
    _globals["_CREATEINDEXRESPONSE"]._serialized_end = 1150
    _globals["_INDEX"]._serialized_start = 1152
    _globals["_INDEX"]._serialized_end = 1274
    _globals["_EMBEDDING"]._serialized_start = 1276
    _globals["_EMBEDDING"]._serialized_end = 1306
    _globals["_ATTRIBUTES"]._serialized_start = 1308
    _globals["_ATTRIBUTES"]._serialized_end = 1340
    _globals["_FEATURE"]._serialized_start = 1343
    _globals["_FEATURE"]._serialized_end = 1472
    _globals["_CONTENT"]._serialized_start = 1474
    _globals["_CONTENT"]._serialized_end = 1560
    _globals["_REGISTEREXECUTORREQUEST"]._serialized_start = 1562
    _globals["_REGISTEREXECUTORREQUEST"]._serialized_end = 1674
    _globals["_REGISTEREXECUTORRESPONSE"]._serialized_start = 1676
    _globals["_REGISTEREXECUTORRESPONSE"]._serialized_end = 1723
    _globals["_HEARTBEATREQUEST"]._serialized_start = 1725
    _globals["_HEARTBEATREQUEST"]._serialized_end = 1764
    _globals["_HEARTBEATRESPONSE"]._serialized_start = 1766
    _globals["_HEARTBEATRESPONSE"]._serialized_end = 1849
    _globals["_TASK"]._serialized_start = 1852
    _globals["_TASK"]._serialized_end = 2215
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_start = 2158
    _globals["_TASK_OUTPUTINDEXMAPPINGENTRY"]._serialized_end = 2215
    _globals["_LISTEXTRACTORSREQUEST"]._serialized_start = 2217
    _globals["_LISTEXTRACTORSREQUEST"]._serialized_end = 2240
    _globals["_LISTEXTRACTORSRESPONSE"]._serialized_start = 2242
    _globals["_LISTEXTRACTORSRESPONSE"]._serialized_end = 2319
    _globals["_EXTRACTOR"]._serialized_start = 2322
    _globals["_EXTRACTOR"]._serialized_end = 2527
    _globals["_EXTRACTOR_OUTPUTSENTRY"]._serialized_start = 2481
    _globals["_EXTRACTOR_OUTPUTSENTRY"]._serialized_end = 2527
    _globals["_GETNAMESPACEREQUEST"]._serialized_start = 2529
    _globals["_GETNAMESPACEREQUEST"]._serialized_end = 2564
    _globals["_GETNAMESPACERESPONSE"]._serialized_start = 2566
    _globals["_GETNAMESPACERESPONSE"]._serialized_end = 2640
    _globals["_LISTCONTENTREQUEST"]._serialized_start = 2643
    _globals["_LISTCONTENTREQUEST"]._serialized_end = 2841
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_start = 2794
    _globals["_LISTCONTENTREQUEST_LABELSEQENTRY"]._serialized_end = 2841
    _globals["_LISTCONTENTRESPONSE"]._serialized_start = 2843
    _globals["_LISTCONTENTRESPONSE"]._serialized_end = 2925
    _globals["_LISTBINDINGSREQUEST"]._serialized_start = 2927
    _globals["_LISTBINDINGSREQUEST"]._serialized_end = 2967
    _globals["_LISTBINDINGSRESPONSE"]._serialized_start = 2969
    _globals["_LISTBINDINGSRESPONSE"]._serialized_end = 3049
    _globals["_CREATENAMESPACEREQUEST"]._serialized_start = 3051
    _globals["_CREATENAMESPACEREQUEST"]._serialized_end = 3147
    _globals["_CREATENAMESPACERESPONSE"]._serialized_start = 3149
    _globals["_CREATENAMESPACERESPONSE"]._serialized_end = 3208
    _globals["_LISTNAMESPACEREQUEST"]._serialized_start = 3210
    _globals["_LISTNAMESPACEREQUEST"]._serialized_end = 3232
    _globals["_LISTNAMESPACERESPONSE"]._serialized_start = 3234
    _globals["_LISTNAMESPACERESPONSE"]._serialized_end = 3310
    _globals["_EXTRACTORBINDING"]._serialized_start = 3313
    _globals["_EXTRACTORBINDING"]._serialized_end = 3528
    _globals["_EXTRACTORBINDING_FILTERSENTRY"]._serialized_start = 3482
    _globals["_EXTRACTORBINDING_FILTERSENTRY"]._serialized_end = 3528
    _globals["_EXTRACTORBINDREQUEST"]._serialized_start = 3530
    _globals["_EXTRACTORBINDREQUEST"]._serialized_end = 3648
    _globals["_EXTRACTORBINDRESPONSE"]._serialized_start = 3651
    _globals["_EXTRACTORBINDRESPONSE"]._serialized_end = 4085
    _globals["_EXTRACTORBINDRESPONSE_INDEXNAMETABLEMAPPINGENTRY"]._serialized_start = (
        3962
    )
    _globals["_EXTRACTORBINDRESPONSE_INDEXNAMETABLEMAPPINGENTRY"]._serialized_end = 4022
    _globals["_EXTRACTORBINDRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"]._serialized_start = (
        4024
    )
    _globals["_EXTRACTORBINDRESPONSE_OUTPUTINDEXNAMEMAPPINGENTRY"]._serialized_end = (
        4085
    )
    _globals["_CONTENTMETADATA"]._serialized_start = 4088
    _globals["_CONTENTMETADATA"]._serialized_end = 4359
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_start = 4314
    _globals["_CONTENTMETADATA_LABELSENTRY"]._serialized_end = 4359
    _globals["_CREATECONTENTREQUEST"]._serialized_start = 4361
    _globals["_CREATECONTENTREQUEST"]._serialized_end = 4439
    _globals["_CREATECONTENTRESPONSE"]._serialized_start = 4441
    _globals["_CREATECONTENTRESPONSE"]._serialized_end = 4476
    _globals["_NAMESPACE"]._serialized_start = 4478
    _globals["_NAMESPACE"]._serialized_end = 4561
    _globals["_COORDINATORSERVICE"]._serialized_start = 4617
    _globals["_COORDINATORSERVICE"]._serialized_end = 6565
# @@protoc_insertion_point(module_scope)
