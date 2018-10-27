from flask_restplus import fields
from flask_restplus.model import Model
from objects import api

ErrorSchema: Model = api.model("Error", {
    "message": fields.String(readOnly=True)
})
