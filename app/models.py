from typing import Optional
import sqlalchemy as sql
import sqlalchemy.orm as sqlorm
from app import oldgrad_db

class User(oldgrad_db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    name: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50), index=True, unique=False)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(20), index=True, unique=True)
    password_hash: sqlorm.Mapped[Optional[str]] = sqlorm.mapped_column(sql.String(256), index=True, unique=True)

    def __repr__(self):
        return f'<user> {self.name}'