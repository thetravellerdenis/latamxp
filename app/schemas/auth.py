from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "invalid": "Invalid email format.",
        },
    )
    password = fields.String(
        required=True, error_messages={"required": "Password is required."}
    )


class UsuarioRegisterSchema(Schema):
    nombre = fields.String(
        required=True,
        validate=validate.Length(min=2, error="Name must be at least 2 characters."),
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "invalid": "Invalid email format.",
        },
    )
    password = fields.String(
        required=True,
        validate=validate.Length(
            min=8, error="Password must be at least 8 characters."
        ),
    )
    idioma = fields.String(required=False, load_default="es")
