# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/lsp/v1/lsp.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16\x63halk/lsp/v1/lsp.proto\x12\x0c\x63halk.lsp.v1"\x83\x01\n\x03LSP\x12H\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32&.chalk.lsp.v1.PublishDiagnosticsParamsR\x0b\x64iagnostics\x12\x32\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\x18.chalk.lsp.v1.CodeActionR\x07\x61\x63tions"h\n\x18PublishDiagnosticsParams\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12:\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x18.chalk.lsp.v1.DiagnosticR\x0b\x64iagnostics"\xd8\x02\n\nDiagnostic\x12)\n\x05range\x18\x01 \x01(\x0b\x32\x13.chalk.lsp.v1.RangeR\x05range\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12<\n\x08severity\x18\x03 \x01(\x0e\x32 .chalk.lsp.v1.DiagnosticSeverityR\x08severity\x12\x17\n\x04\x63ode\x18\x04 \x01(\tH\x00R\x04\x63ode\x88\x01\x01\x12H\n\x10\x63ode_description\x18\x05 \x01(\x0b\x32\x1d.chalk.lsp.v1.CodeDescriptionR\x0f\x63odeDescription\x12[\n\x13related_information\x18\x06 \x03(\x0b\x32*.chalk.lsp.v1.DiagnosticRelatedInformationR\x12relatedInformationB\x07\n\x05_code"_\n\x05Range\x12,\n\x05start\x18\x01 \x01(\x0b\x32\x16.chalk.lsp.v1.PositionR\x05start\x12(\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x16.chalk.lsp.v1.PositionR\x03\x65nd"]\n\x08Position\x12\x17\n\x04line\x18\x01 \x01(\x05H\x00R\x04line\x88\x01\x01\x12!\n\tcharacter\x18\x02 \x01(\x05H\x01R\tcharacter\x88\x01\x01\x42\x07\n\x05_lineB\x0c\n\n_character"\x8f\x01\n\nCodeAction\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12:\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x18.chalk.lsp.v1.DiagnosticR\x0b\x64iagnostics\x12/\n\x04\x65\x64it\x18\x03 \x01(\x0b\x32\x1b.chalk.lsp.v1.WorkspaceEditR\x04\x65\x64it"Z\n\rWorkspaceEdit\x12I\n\x10\x64ocument_changes\x18\x01 \x03(\x0b\x32\x1e.chalk.lsp.v1.TextDocumentEditR\x0f\x64ocumentChanges"\x8b\x01\n\x10TextDocumentEdit\x12I\n\rtext_document\x18\x01 \x01(\x0b\x32$.chalk.lsp.v1.TextDocumentIdentifierR\x0ctextDocument\x12,\n\x05\x65\x64its\x18\x02 \x03(\x0b\x32\x16.chalk.lsp.v1.TextEditR\x05\x65\x64its"*\n\x16TextDocumentIdentifier\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri"P\n\x08TextEdit\x12)\n\x05range\x18\x01 \x01(\x0b\x32\x13.chalk.lsp.v1.RangeR\x05range\x12\x19\n\x08new_text\x18\x02 \x01(\tR\x07newText"%\n\x0f\x43odeDescription\x12\x12\n\x04href\x18\x01 \x01(\tR\x04href"l\n\x1c\x44iagnosticRelatedInformation\x12\x32\n\x08location\x18\x01 \x01(\x0b\x32\x16.chalk.lsp.v1.LocationR\x08location\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message"G\n\x08Location\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\x12)\n\x05range\x18\x02 \x01(\x0b\x32\x13.chalk.lsp.v1.RangeR\x05range*\xbc\x01\n\x12\x44iagnosticSeverity\x12#\n\x1f\x44IAGNOSTIC_SEVERITY_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x44IAGNOSTIC_SEVERITY_ERROR\x10\x01\x12\x1f\n\x1b\x44IAGNOSTIC_SEVERITY_WARNING\x10\x02\x12#\n\x1f\x44IAGNOSTIC_SEVERITY_INFORMATION\x10\x03\x12\x1c\n\x18\x44IAGNOSTIC_SEVERITY_HINT\x10\x04\x42n\n\x10\x63om.chalk.lsp.v1B\x08LspProtoP\x01\xa2\x02\x03\x43LX\xaa\x02\x0c\x43halk.Lsp.V1\xca\x02\x0c\x43halk\\Lsp\\V1\xe2\x02\x18\x43halk\\Lsp\\V1\\GPBMetadata\xea\x02\x0e\x43halk::Lsp::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "chalk.lsp.v1.lsp_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\020com.chalk.lsp.v1B\010LspProtoP\001\242\002\003CLX\252\002\014Chalk.Lsp.V1\312\002\014Chalk\\Lsp\\V1\342\002\030Chalk\\Lsp\\V1\\GPBMetadata\352\002\016Chalk::Lsp::V1"
    _globals["_DIAGNOSTICSEVERITY"]._serialized_start = 1548
    _globals["_DIAGNOSTICSEVERITY"]._serialized_end = 1736
    _globals["_LSP"]._serialized_start = 41
    _globals["_LSP"]._serialized_end = 172
    _globals["_PUBLISHDIAGNOSTICSPARAMS"]._serialized_start = 174
    _globals["_PUBLISHDIAGNOSTICSPARAMS"]._serialized_end = 278
    _globals["_DIAGNOSTIC"]._serialized_start = 281
    _globals["_DIAGNOSTIC"]._serialized_end = 625
    _globals["_RANGE"]._serialized_start = 627
    _globals["_RANGE"]._serialized_end = 722
    _globals["_POSITION"]._serialized_start = 724
    _globals["_POSITION"]._serialized_end = 817
    _globals["_CODEACTION"]._serialized_start = 820
    _globals["_CODEACTION"]._serialized_end = 963
    _globals["_WORKSPACEEDIT"]._serialized_start = 965
    _globals["_WORKSPACEEDIT"]._serialized_end = 1055
    _globals["_TEXTDOCUMENTEDIT"]._serialized_start = 1058
    _globals["_TEXTDOCUMENTEDIT"]._serialized_end = 1197
    _globals["_TEXTDOCUMENTIDENTIFIER"]._serialized_start = 1199
    _globals["_TEXTDOCUMENTIDENTIFIER"]._serialized_end = 1241
    _globals["_TEXTEDIT"]._serialized_start = 1243
    _globals["_TEXTEDIT"]._serialized_end = 1323
    _globals["_CODEDESCRIPTION"]._serialized_start = 1325
    _globals["_CODEDESCRIPTION"]._serialized_end = 1362
    _globals["_DIAGNOSTICRELATEDINFORMATION"]._serialized_start = 1364
    _globals["_DIAGNOSTICRELATEDINFORMATION"]._serialized_end = 1472
    _globals["_LOCATION"]._serialized_start = 1474
    _globals["_LOCATION"]._serialized_end = 1545
# @@protoc_insertion_point(module_scope)
