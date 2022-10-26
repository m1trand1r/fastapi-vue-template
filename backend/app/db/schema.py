from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)
from sqlalchemy import MetaData

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    # indexes
    'ix': 'ix__%(tablename)s__%(all_column_names)s',

    # unique indexes
    'uq': 'uq__%(table_name)s__%(all_column_names)s',

    # CHECK-constrait ix
    'ck': 'ck__%(table_name)s__%(constraint_name)s',

    # fk
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',

    # pk
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False, unique=True),
    Column('password', String, nullable=False),
    Column('is_active', Boolean, nullable=False),
    Column('is_superuser', Boolean, nullable=False)
)

role_table = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('description', String(255), nullable=False),
)

user_role_table = Table(
    'user_role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('id_user', ForeignKey('users.id')),
    Column('id_role', ForeignKey('role.id')),
)
