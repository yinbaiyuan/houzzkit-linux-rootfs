# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/uploader/proto/server_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/uploader/proto/server_info.proto',
  package='tensorboard.service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,tensorboard/uploader/proto/server_info.proto\x12\x13tensorboard.service\"$\n\x11ServerInfoRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\"\xc1\x01\n\x12ServerInfoResponse\x12\x39\n\rcompatibility\x18\x01 \x01(\x0b\x32\".tensorboard.service.Compatibility\x12\x32\n\napi_server\x18\x02 \x01(\x0b\x32\x1e.tensorboard.service.ApiServer\x12<\n\nurl_format\x18\x03 \x01(\x0b\x32(.tensorboard.service.ExperimentUrlFormat\"\\\n\rCompatibility\x12:\n\x07verdict\x18\x01 \x01(\x0e\x32).tensorboard.service.CompatibilityVerdict\x12\x0f\n\x07\x64\x65tails\x18\x02 \x01(\t\"\x1d\n\tApiServer\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\"?\n\x13\x45xperimentUrlFormat\x12\x10\n\x08template\x18\x01 \x01(\t\x12\x16\n\x0eid_placeholder\x18\x02 \x01(\t*`\n\x14\x43ompatibilityVerdict\x12\x13\n\x0fVERDICT_UNKNOWN\x10\x00\x12\x0e\n\nVERDICT_OK\x10\x01\x12\x10\n\x0cVERDICT_WARN\x10\x02\x12\x11\n\rVERDICT_ERROR\x10\x03\x62\x06proto3')
)

_COMPATIBILITYVERDICT = _descriptor.EnumDescriptor(
  name='CompatibilityVerdict',
  full_name='tensorboard.service.CompatibilityVerdict',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERDICT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_OK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_WARN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERDICT_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=493,
  serialized_end=589,
)
_sym_db.RegisterEnumDescriptor(_COMPATIBILITYVERDICT)

CompatibilityVerdict = enum_type_wrapper.EnumTypeWrapper(_COMPATIBILITYVERDICT)
VERDICT_UNKNOWN = 0
VERDICT_OK = 1
VERDICT_WARN = 2
VERDICT_ERROR = 3



_SERVERINFOREQUEST = _descriptor.Descriptor(
  name='ServerInfoRequest',
  full_name='tensorboard.service.ServerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorboard.service.ServerInfoRequest.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=105,
)


_SERVERINFORESPONSE = _descriptor.Descriptor(
  name='ServerInfoResponse',
  full_name='tensorboard.service.ServerInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='compatibility', full_name='tensorboard.service.ServerInfoResponse.compatibility', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_server', full_name='tensorboard.service.ServerInfoResponse.api_server', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url_format', full_name='tensorboard.service.ServerInfoResponse.url_format', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=301,
)


_COMPATIBILITY = _descriptor.Descriptor(
  name='Compatibility',
  full_name='tensorboard.service.Compatibility',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verdict', full_name='tensorboard.service.Compatibility.verdict', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='tensorboard.service.Compatibility.details', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=395,
)


_APISERVER = _descriptor.Descriptor(
  name='ApiServer',
  full_name='tensorboard.service.ApiServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='tensorboard.service.ApiServer.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=426,
)


_EXPERIMENTURLFORMAT = _descriptor.Descriptor(
  name='ExperimentUrlFormat',
  full_name='tensorboard.service.ExperimentUrlFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template', full_name='tensorboard.service.ExperimentUrlFormat.template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_placeholder', full_name='tensorboard.service.ExperimentUrlFormat.id_placeholder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=491,
)

_SERVERINFORESPONSE.fields_by_name['compatibility'].message_type = _COMPATIBILITY
_SERVERINFORESPONSE.fields_by_name['api_server'].message_type = _APISERVER
_SERVERINFORESPONSE.fields_by_name['url_format'].message_type = _EXPERIMENTURLFORMAT
_COMPATIBILITY.fields_by_name['verdict'].enum_type = _COMPATIBILITYVERDICT
DESCRIPTOR.message_types_by_name['ServerInfoRequest'] = _SERVERINFOREQUEST
DESCRIPTOR.message_types_by_name['ServerInfoResponse'] = _SERVERINFORESPONSE
DESCRIPTOR.message_types_by_name['Compatibility'] = _COMPATIBILITY
DESCRIPTOR.message_types_by_name['ApiServer'] = _APISERVER
DESCRIPTOR.message_types_by_name['ExperimentUrlFormat'] = _EXPERIMENTURLFORMAT
DESCRIPTOR.enum_types_by_name['CompatibilityVerdict'] = _COMPATIBILITYVERDICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfoRequest = _reflection.GeneratedProtocolMessageType('ServerInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFOREQUEST,
  '__module__' : 'tensorboard.uploader.proto.server_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ServerInfoRequest)
  })
_sym_db.RegisterMessage(ServerInfoRequest)

ServerInfoResponse = _reflection.GeneratedProtocolMessageType('ServerInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERINFORESPONSE,
  '__module__' : 'tensorboard.uploader.proto.server_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ServerInfoResponse)
  })
_sym_db.RegisterMessage(ServerInfoResponse)

Compatibility = _reflection.GeneratedProtocolMessageType('Compatibility', (_message.Message,), {
  'DESCRIPTOR' : _COMPATIBILITY,
  '__module__' : 'tensorboard.uploader.proto.server_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.Compatibility)
  })
_sym_db.RegisterMessage(Compatibility)

ApiServer = _reflection.GeneratedProtocolMessageType('ApiServer', (_message.Message,), {
  'DESCRIPTOR' : _APISERVER,
  '__module__' : 'tensorboard.uploader.proto.server_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ApiServer)
  })
_sym_db.RegisterMessage(ApiServer)

ExperimentUrlFormat = _reflection.GeneratedProtocolMessageType('ExperimentUrlFormat', (_message.Message,), {
  'DESCRIPTOR' : _EXPERIMENTURLFORMAT,
  '__module__' : 'tensorboard.uploader.proto.server_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.service.ExperimentUrlFormat)
  })
_sym_db.RegisterMessage(ExperimentUrlFormat)


# @@protoc_insertion_point(module_scope)
