from marshmallow import (
    Schema,
    fields,
    validate,
)


class PatentApplicationSubsidiaryResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    patent_application_id = fields.Integer(required=True)
    subsidiary_id = fields.Integer(required=True)
    score = fields.Float(required=True)
    published_date = fields.DateTime(allow_none=True)
    updated_at = fields.DateTime()
