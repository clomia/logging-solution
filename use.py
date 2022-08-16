from object import Logging


@Logging(description="더하기 10을 하는 함수", level="INFO", error_comment="인수 number는 10을 더할 수 있는 숫자여야만 합니다.")
def plus_10(number: int) -> int:
    """입력받은 숫자에 10을 더해서 반환합니다"""
    result = number + 10

    return result


today_num = "10을 더할 수 없는 문자열"

plus_result = plus_10(today_num, log_suffix="today_num")
