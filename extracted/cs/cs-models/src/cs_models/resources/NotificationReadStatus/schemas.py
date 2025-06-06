from marshmallow import (
    Schema,
    fields,
    validate,
)


class NotificationReadStatusResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    notification_id = fields.Integer(required=True)
    user_id = fields.String(required=True)
    seen_at = fields.DateTime(allow_none=True)
    updated_at = fields.DateTime()
