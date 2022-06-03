from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Thing(Model):
    id = columns.Integer(primary_key=True)
    name = columns.Text()
    description = columns.Text()
    content = columns.Text()
    create_at = columns.DateTime()
    updated_at = columns.DateTime()
    deleted_at = columns.DateTime
    deleted = columns.Boolean(default=False)
