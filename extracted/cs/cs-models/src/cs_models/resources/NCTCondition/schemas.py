from marshmallow import (
    Schema,
    fields,
    validate,
)


class NCTConditionResourceSchema(Schema):
    not_blank = validate.Length(min=1, error="Field cannot be blank")

    id = fields.Integer(dump_only=True)
    nct_study_id = fields.Integer(required=True)
    condition_id = fields.Integer(required=True)
    is_deleted = fields.Boolean(allow_none=True)
    updated_at = fields.DateTime(dump_only=True)
