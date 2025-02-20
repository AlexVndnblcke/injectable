"""
In this example you'll see how we can declare a function as a factory of injectable
instances.

A common use case for using factories is to wrap some class external to your code or
which you cannot declare as injectable for some reason, we declare a ``ExternalClient``
class to represent such a case.

The ``client_factory`` function is declared as a factory for the ``ExternalClient``
class through the :meth:`@injectable_factory <injectable.injectable_factory>` decorator
and will deal with all the necessary logic to instantiate an ``ExternalClient``.

Now our ``Factory`` example class can be injected with an ``ExternalClient`` without
having the responsibility of knowing how to actually instantiate it.

.. seealso::

    The :meth:`injectable_factory <injectable.injectable_factory>` decorator can also be
    used in lambdas for simpler cases. The :ref:`injecting_existing_instance_example`
    shows how to use it like so.
"""

# sphinx-start
from typing import Annotated

from examples import Example
from examples.factory.external_client import ExternalClient
from injectable import autowired, Autowired, load_injection_container


class Factory(Example):
    @autowired
    def __init__(
        self,
        client: Annotated[ExternalClient, Autowired],
    ):
        self.client = client

    def run(self):
        print(self.client.connect())
        # ExternalClient connected to https://dummy/endpoint


def run_example():
    load_injection_container()
    example = Factory()
    example.run()


if __name__ == "__main__":
    run_example()
