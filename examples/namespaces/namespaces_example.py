"""
In this example you'll see how namespaces work in the framework.

Each namespace has its own independent injectables registry and one namespace cannot
see the others injectables.

To illustrate how this works we declare two classes, ``InternationalMeasuringService``
and ``UnitedStatesMeasuringService``, both implementing the ``MeasuringService``
abstract base class but each is assigned to a different namespace, ``"INTL"`` and
``"US"`` respectively.

In our ``Namespace`` example class we inject three parameters with
``MeasuringService`` injectables: first without specifying any particular namespace
and also declaring the injection as optional; then specifying the ``"INTL"`` namespace;
and at last specifying the ``"US"`` namespace.

By running the example we can see that the ``default_measuring_service`` is not injected
and that the other ones are successfully injected without conflicts in resolving the
qualifier.

What we see for the ``default_measuring_service`` argument is that without specifying a
namespace the default namespace is used and no injectable that resolves the
``MeasuringService`` dependency were registered in the default namespace. Then, for
the ``intl_measuring_service`` and ``us_measuring_service`` arguments we only have a
single injectable resolving the ``MeasuringService`` dependency declared in each
namespace, therefore no conflicts.

.. seealso::

    The :ref:`optional_injection_example` details how declaring an injection as
    optional works.
"""

# sphinx-start
from typing import Annotated, Optional

from examples import Example
from examples.namespaces.measuring_service_abc import MeasuringService
from injectable import Autowired, autowired, load_injection_container


class Namespaces(Example):
    @autowired
    def __init__(
        self,
        default_measuring_service: Annotated[Optional[MeasuringService], Autowired],
        intl_measuring_service: Annotated[
            MeasuringService, Autowired(namespace="INTL")
        ],
        us_measuring_service: Annotated[MeasuringService, Autowired(namespace="US")],
    ):
        self.default_measuring_service = default_measuring_service
        self.intl_measuring_service = intl_measuring_service
        self.us_measuring_service = us_measuring_service

    def run(self):
        print(self.default_measuring_service)
        # None

        print(self.intl_measuring_service.earth_to_sun_distance())
        # 151.38 million km

        print(self.us_measuring_service.earth_to_sun_distance())
        # 94.06 million miles


def run_example():
    load_injection_container()
    example = Namespaces()
    example.run()


if __name__ == "__main__":
    run_example()
