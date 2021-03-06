import time
from xmlrpc.client import ServerProxy, Fault

from locust import User, task


class XmlRpcClient(ServerProxy):
    """
    XmlRpcClient is a wrapper around the standard library's ServerProxy.
    It proxies any function calls and fires the *request* event when they finish,
    so that the calls get recorded in Locust.
    """

    def __init__(self, host, request_event):
        super().__init__(host)
        self._request_event = request_event

    def __getattr__(self, name):
        func = ServerProxy.__getattr__(self, name)

        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            request_meta = {
                "request_type": "xmlrpc",
                "name": name,
                "response_length": 0,  # calculating this for an xmlrpc.client response would be too hard
                "response": None,
                "context": {},  # see HttpUser if you actually want to implement contexts
                "exception": None,
            }
            try:
                request_meta["response"] = func(*args, **kwargs)
            except Fault as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
            self._request_event.fire(**request_meta)  # This is what makes the request actually get logged in Locust
            return request_meta["response"]

        return wrapper


class XmlRpcUser(User):
    """
    A minimal Locust user class that provides an XmlRpcClient to its subclasses
    """

    abstract = True  # dont instantiate this as an actual user when running Locust

    def __init__(self, environment):
        super().__init__(environment)
        self.client = XmlRpcClient(self.host, request_event=environment.events.request)