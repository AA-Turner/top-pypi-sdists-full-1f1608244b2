from marshmallow import (
    Schema,
    fields,
    validate,
)


class NewswireCompanyUpdateOutboxResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    news_id = fields.Integer(required=True)
    submitted = fields.Boolean(allow_none=True)
    historical = fields.Boolean(allow_none=True)
    updated_at = fields.DateTime()
