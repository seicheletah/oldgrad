from app import oldgrad, oldgrad_db
import sqlalchemy as sql
import sqlalchemy.orm as sqlorm
from app.models import User, EventPost, JobPost, Donations

@oldgrad.shell_context_processor
def make_shell_context():
    return {'sql':sql, 'sqlorm':sqlorm, 'oldgrad_db':oldgrad_db, 'User':User, 'EventPost':EventPost, 'JobPost':JobPost, 'Donations':Donations}