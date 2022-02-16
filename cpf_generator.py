import random
import re
from typing import List


class CpfHandler:
    """
    author: <Erick Duarte erickod@gmail.com>
    """
    multipliers: List[int] = [value for value in range(2, 12)][::-1]

    @classmethod
    def __generate_random_digits(cls) -> List[str]:
        return [
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
        ]

    @classmethod
    def __calc_first_check_digit(cls, partial_cpf: List[str]) -> List[str]:
        sum = 0
        for d, m in zip(partial_cpf, cls.multipliers[1:]):
            sum += int(d) * int(m)

        rest = sum % 11
        partial_cpf.append(str(0 if rest < 2 else 11 - rest))
        return partial_cpf

    @classmethod
    def __calc_second_check_digit(cls, partial_cpf: List[str]) -> List[str]:
        sum = 0
        for d, m in zip(partial_cpf, cls.multipliers):
            sum += int(d) * int(m)

        rest = sum % 11
        partial_cpf.append(str(0 if rest < 2 else 11 - rest))
        return partial_cpf

    @classmethod
    def generate(
        cls,
    ):
        partial_cpf = cls.__generate_random_digits()
        partial_cpf = cls.__calc_first_check_digit(partial_cpf)
        partial_cpf = cls.__calc_second_check_digit(partial_cpf)
        return "".join(partial_cpf)

    @classmethod
    def validate(cls, cpf: str):
        if re.match(r"^(.)\1*$", cpf):
            return False

        cpf_list = list(cpf)
        partial_cpf = cls.__calc_first_check_digit(cpf_list[0:9])
        resulting_cpf = cls.__calc_second_check_digit(partial_cpf)

        return True if "".join(resulting_cpf) == cpf else False
