# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"\x18\n\x07Request\x12\r\n\x05query\x18\x01 \x01(\t\"=\n\x08Response\x12\x0f\n\x07usd_chf\x18\x01 \x01(\x02\x12\x0f\n\x07\x65ur_usd\x18\x02 \x01(\x02\x12\x0f\n\x07\x63hf_eur\x18\x03 \x01(\x02\x32\x30\n\tMyService\x12#\n\nStreamData\x12\x08.Request\x1a\t.Response0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=17
  _globals['_REQUEST']._serialized_end=41
  _globals['_RESPONSE']._serialized_start=43
  _globals['_RESPONSE']._serialized_end=104
  _globals['_MYSERVICE']._serialized_start=106
  _globals['_MYSERVICE']._serialized_end=154
# @@protoc_insertion_point(module_scope)
