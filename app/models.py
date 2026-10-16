"""Database tables, written as Python classes. One class = one table."""
from datetime import datetime

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Trip(Base):
    __tablename__ = "trips"  # the table's name in the database

    # id: a whole number, and the primary key (unique for each row)
    id: Mapped[int] = mapped_column(primary_key=True)

    # name: text, at most 100 characters, required
    name: Mapped[str] = mapped_column(String(100))

    # created_at: a date and time; the database fills it in automatically
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"))  # which trip they're on
    name: Mapped[str] = mapped_column(String(100))

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"))   # which trip
    paid_by: Mapped[int] = mapped_column(ForeignKey("members.id"))   # which member paid
    description: Mapped[str] = mapped_column(String(200))
    amount_cents: Mapped[int] = mapped_column()

class ExpenseSplit(Base):
    __tablename__ = "expense_splits"

    id: Mapped[int] = mapped_column(primary_key=True)
    expense_id: Mapped[int] = mapped_column(ForeignKey("expenses.id"))
    member_id: Mapped[int] = mapped_column(ForeignKey("members.id"))
    share_cents: Mapped[int] = mapped_column()