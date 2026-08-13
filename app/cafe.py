from datetime import date
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name: str):
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError

        vaccine = visitor["vaccine"]

        if "expiration_date" in vaccine:
            exp_date = vaccine["expiration_date"]
            
            if isinstance(exp_date, str):
                exp_date = date.fromisoformat(exp_date)

            if exp_date < date.today():
                raise OutdatedVaccineError

        if not vaccine.get("wearing_a_mask", False):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
