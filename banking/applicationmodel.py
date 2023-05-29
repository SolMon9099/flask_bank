# coding=utf-8

from uuid import NAMESPACE_URL, UUID, uuid5

from eventsourcing.application import AggregateNotFound, Application

from banking.domainmodel import Account, BadCredentials


class Bank(Application):
    """
    This is the model of the application, it has
    all of its events in the from of aggregate
    events that it loads. This loads and
    saves aggregates and forms the business logic
    for reading and writing.

    To create an aggregate run:
      new_account = Account(...)

    To load existing aggregates run:
      account1 = self.repository.get(account_id1)
      account2 = self.repository.get(account_id2)

    To save any aggregates run:
      self.save(account1, account2, new_account)
    """

    def open_account(
        self,
        full_name: str,
        email_address: str,
        password: str,
    ) -> UUID:
        """
        The first few lines of this function are
        completed, but there is more to do.
        """
        account = Account(
            self.get_account_id_by_email(email_address),
            full_name=full_name,
            email_address=email_address,
            password=password,
        )

        # complete this function and other below
        return account.id


class AccountNotFoundError(Exception):
    pass
