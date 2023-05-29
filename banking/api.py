# coding=utf-8
# flake8: noqa E402

import logging
import typing
from uuid import UUID
from eventsourcing.application import AggregateNotFound
from flask import Flask, Response, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity  # type: ignore
from flask_restful import Resource, Api  # type: ignore

from banking.applicationmodel import AccountNotFoundError, Bank


app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret"

api = Api(app, prefix="/api/v1")

_bank = Bank()


def bank() -> Bank:
    return _bank


class User:
    id: str


def user() -> User:
    return User()  # return current api user logged in


class AccountResource(Resource):
    @jwt_required()
    def get(self) -> typing.Dict[str, typing.Any]:
        logging.info("account get")
        account = bank().get_account(UUID(user().id))
        return {
            "balance": str(account.balance),
            "identity": user().id,
        }


api.add_resource(AccountResource, "/account")
