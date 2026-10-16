"""Regression checks for the JSON Schema subset used by the upload models.

Requires PyYAML and jsonschema. Run: python -m unittest discover -s tests -v
No server, credentials, network requests, or model files are required.
"""

from copy import deepcopy
from pathlib import Path
import unittest

from jsonschema import Draft4Validator
import yaml


SPECIFICATION = yaml.safe_load(
    (Path(__file__).resolve().parents[1] / "swagger.yaml").read_text()
)
PART = {
    "url": "https://cde.example.test/upload/part/1",
    "http_method": "PUT",
    "content_range_start": 0,
    "content_range_end": 1023,
}


def validator(model):
    # These models use the Draft 4-compatible subset of OpenAPI 3.0 Schema.
    # Keep references rooted in the complete, unmodified specification.
    return Draft4Validator({
        "$ref": "#/components/schemas/" + model,
        "components": SPECIFICATION["components"],
    })


class UploadFilePartInstructionTests(unittest.TestCase):
    def test_minimal_instruction(self):
        for method in ("POST", "PUT"):
            with self.subTest(method=method):
                validator("UploadFilePartInstruction").validate({
                    **PART, "http_method": method,
                })

    def test_all_optional_properties(self):
        validator("UploadFilePartInstruction").validate({
            **PART,
            "additional_headers": {
                "values": [{"name": "Content-Type", "value": "application/octet-stream"}],
            },
            "include_authorization": True,
            "multipart_form_data": {"prefix": "cHJlZml4", "suffix": "c3VmZml4"},
        })

    def test_each_required_property(self):
        for name in PART:
            with self.subTest(property=name):
                incomplete = deepcopy(PART)
                del incomplete[name]
                self.assertFalse(validator("UploadFilePartInstruction").is_valid(incomplete))

    def test_empty_url(self):
        self.assertFalse(validator("UploadFilePartInstruction").is_valid({**PART, "url": ""}))

    def test_unsupported_http_method(self):
        self.assertFalse(validator("UploadFilePartInstruction").is_valid({
            **PART, "http_method": "GET",
        }))

    def test_property_types(self):
        for name, value in (
            ("url", 42),
            ("content_range_start", "0"),
            ("content_range_end", 1.5),
            ("include_authorization", "false"),
        ):
            with self.subTest(property=name):
                self.assertFalse(validator("UploadFilePartInstruction").is_valid({
                    **PART, name: value,
                }))

    def test_unknown_property(self):
        self.assertFalse(validator("UploadFilePartInstruction").is_valid({
            **PART, "unexpected": True,
        }))

    def test_link_data_remains_closed(self):
        validator("LinkData").validate({"url": PART["url"]})
        for invalid in ({}, {"url": ""}, PART):
            with self.subTest(link=invalid):
                self.assertFalse(validator("LinkData").is_valid(invalid))

    def test_instruction_in_documents_to_upload_response(self):
        validator("DocumentsToUpload").validate({
            "documents_to_upload": [{
                "session_file_id": "file-1",
                "upload_file_parts": [PART],
                "upload_completion": {"url": "https://cde.example.test/upload/complete"},
                "upload_cancellation": {"url": "https://cde.example.test/upload/cancel"},
            }],
        })


if __name__ == "__main__":
    unittest.main()
