from datetime import date

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        vaccine = visitor["vaccine"]

        if "expiration_date" in vaccine:
            exp_date = vaccine["expiration_date"]

            if isinstance(exp_date, str):
                exp_date = date.fromisoformat(exp_date)

            if exp_date < date.today():
                raise OutdatedVaccineError("Visitor has outdated vaccination")

        if not vaccine.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
