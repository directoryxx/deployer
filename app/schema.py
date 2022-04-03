from app import app

from app.models import Instruction,WhiteList
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


"""
=============
schema classes
=============
"""

class InstructionSchema(ma.ModelSchema):
    class Meta:
        model = Instruction
        fields = ('user', 'step', 'command', 'tag', 'short_desc','target')

instruction_schema = InstructionSchema()
instruction_schemas = InstructionSchema(many=True)

class WhitelistSchema(ma.ModelSchema):
    class Meta:
        model = WhiteList
        fields = ('ip','allowed')

whitelist_schema = WhitelistSchema()