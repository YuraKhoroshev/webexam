import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import os
from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin 
from flask import url_for
from users_policy import UsersPolicy

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desciption = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())

    role = db.relationship('Role')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name or ''])

    @property
    def is_admin(self):
        return app.config.get('ADMIN_ROLE_ID') == self.role_id

    @property
    def is_moder(self):
        return app.config.get('MODER_ROLE_ID') == self.role_id
    
    @property
    def is_user(self):
        return app.config.get('USER_ROLE_ID') == self.role_id

    def can(self, action):
        users_policy = UsersPolicy()
        method = getattr(users_policy, action)
        if method is not None:
            return method()
        return False

    def __repr__(self):
        return '<User %r>' % self.login
