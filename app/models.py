#for database structure creation
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sql
import sqlalchemy.orm as sqlorm
from app import oldgrad_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

class User(UserMixin, oldgrad_db.Model): #needs to create 2 User table(with current company, position column)
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    name: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50), index=True)
    email: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(20), index=True, unique=True)
    password_hash: sqlorm.Mapped[Optional[str]] = sqlorm.mapped_column(sql.String(256))
    phone_number: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.String(10), index=True)
    branch: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50), index=True)
    location: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50), index=True)
    passout_year: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.String(4), index=True)
    eventpost: sqlorm.WriteOnlyMapped['EventPost'] = sqlorm.relationship(back_populates='author')
    jobpost: sqlorm.WriteOnlyMapped['JobPost'] = sqlorm.relationship(back_populates='author')
    donations: sqlorm.WriteOnlyMapped['Donations'] = sqlorm.relationship(back_populates='author')

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<user> {self.name}'
    
class EventPost(oldgrad_db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    event_title: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(100))
    event_location: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50))
    event_description: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(500))
    event_date: sqlorm.Mapped[datetime] = sqlorm.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.ForeignKey(User.id), index=True)
    author: sqlorm.Mapped[User] = sqlorm.relationship(back_populates='eventpost')

    def __repr__(self):
        return f'<event_title> {self.event_title}'
    
class JobPost(oldgrad_db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    job_title: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(100))
    job_location: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(50))
    job_description: sqlorm.Mapped[str] = sqlorm.mapped_column(sql.String(500))
    last_apply_date: sqlorm.Mapped[datetime] = sqlorm.mapped_column(index=True, default=lambda: datetime.now(timezone.utc)) #change lambda to manual
    user_id: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.ForeignKey(User.id), index=True)
    author: sqlorm.Mapped[User] = sqlorm.relationship(back_populates='jobpost')

    def __repr__(self):
        return f'<job_title> {self.job_title}'

class Donations(oldgrad_db.Model):
    id: sqlorm.Mapped[int] = sqlorm.mapped_column(primary_key=True)
    ammount: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.String(20), index=True)
    donation_time: sqlorm.Mapped[datetime] = sqlorm.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: sqlorm.Mapped[int] = sqlorm.mapped_column(sql.ForeignKey(User.id), index=True)
    author: sqlorm.Mapped[User] = sqlorm.relationship(back_populates='donations')

    def __repr__(self):
        return f'<ammount> {self.ammount}' #later add time too

@login_manager.user_loader
def load_user(id: str):
    return oldgrad_db.session.get(User, int(id))