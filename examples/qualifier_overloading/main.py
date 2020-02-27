from typing import List

from examples import Example
from examples.qualifier_overloading.services.sender_service import SenderService
from injectable import injectable, InjectionContainer, autowired, Autowired


@injectable  # make examples also injectable for testing
class QualifierOverloading(Example):
    @autowired
    def __init__(
        self, sender_services: Autowired(List[SenderService], exclude_groups=["old"]),
    ):
        self.sender_services = sender_services

    def send_message(self, message: str, recipient: str):
        for sender_service in self.sender_services:
            sender_service.send(message, recipient)

    def run(self):
        self.send_message(message="Hello!", recipient="World")


if __name__ == "__main__":
    InjectionContainer.load()
    example = QualifierOverloading()
    example.run()
