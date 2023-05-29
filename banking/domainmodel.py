# coding=utf-8

from hashlib import sha512
from re import fullmatch
from uuid import UUID, uuid4

from eventsourcing.domain import Aggregate, event


class Account(Aggregate):
    """
    This is the model of the aggregate, it has
    many events that happen, and when you load
    a model using the application object (Bank)
    you get all events saved for the id of the
    individual model. This never saves itself,
    all saving happens in the Bank application.
    """

    _id: UUID

    @event("Opened")
    def __init__(
        self,
        id: UUID,
        full_name: str,
        email_address: str,
        password: str,
    ):
        self._id = id
        self.full_name = full_name
        # complete this function and others below as needed

    @event("Credited")
    def credit(self, amount_in_cents: int) -> None:
        """todo"""


class TransactionError(Exception):
    pass


class AccountClosedError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class BadCredentials(Exception):
    pass
