# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_httpserver.status`
====================================================
* Author(s): Dan Halbert, Michał Pokusa
"""


class Status:  # pylint: disable=too-few-public-methods
    """HTTP status code."""

    def __init__(self, code: int, text: str):
        """
        Define a status code.

        :param int code: Numeric value: 200, 404, etc.
        :param str text: Short phrase: "OK", "Not Found', etc.
        """
        self.code = code
        self.text = text

    def __repr__(self):
        return f'Status({self.code}, "{self.text}")'

    def __str__(self):
        return f"{self.code} {self.text}"

    def __eq__(self, other: "Status"):
        return self.code == other.code and self.text == other.text


class CommonHTTPStatus(HTTPStatus):  # pylint: disable=too-few-public-methods
    """Common HTTP status codes."""

    OK_200 = HTTPStatus(200, "OK")
    """200 OK"""

    BAD_REQUEST_400 = HTTPStatus(400, "Bad Request")
    """400 Bad Request"""

    UNAUTHORIZED_401 = HTTPStatus(401, "Unauthorized")
    """401 Unauthorized"""

    FORBIDDEN_403 = HTTPStatus(403, "Forbidden")
    """403 Forbidden"""

    NOT_FOUND_404 = HTTPStatus(404, "Not Found")
    """404 Not Found"""

    INTERNAL_SERVER_ERROR_500 = HTTPStatus(500, "Internal Server Error")
    """500 Internal Server Error"""
