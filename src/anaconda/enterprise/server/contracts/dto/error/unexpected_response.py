""" AE Unexpected Response Error Definition """

from .error import AEError


class AEUnexpectedResponseError(AEError):
    """AE Unexpected Response Error"""

    def __init__(self, response, method, url, **kwargs):
        if isinstance(response, str):
            msg = [f"Unexpected response: {response}"]
        else:
            msg = [
                f"Unexpected response: {response.status_code} {response.reason}",
                f"  {method.upper()} {url}",
            ]
            if response.headers:
                msg.append(f"  headers: {response.headers}")
            if response.text:
                msg.append(f"  text: {response.text}")
        if "params" in kwargs:
            msg.append(f'  params: {kwargs["params"]}')
        if "data" in kwargs:
            msg.append(f'  data: {kwargs["data"]}')
        if "json" in kwargs:
            msg.append(f'  json: {kwargs["json"]}')

        # TODO: Review the usage of super here.  The specific error:
        # R1725: Consider using Python 3 style super() without arguments (super-with-arguments)
        # pylint: disable=super-with-arguments
        super(AEUnexpectedResponseError, self).__init__("\n".join(msg))
