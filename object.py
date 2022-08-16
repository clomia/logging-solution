import os
import json
import logging
import logging.config
import traceback
import ssl
from pprint import pformat

ssl._create_default_https_context = ssl._create_unverified_context

CONFIG_PATH = "config.json"

logging.config.dictConfig(json.load(open(CONFIG_PATH)))
log = logging.getLogger("basic")


class Logging:
    """함수 로깅을 위한 데코레이터"""

    level = {
        "DEBUG": log.debug,
        "INFO": log.info,
        "WARNING": log.warning,
        "ERROR": log.error,
        "CRITICAL": log.critical,
    }

    def __init__(self, *, description: str = "", level: str = "INFO", error_comment: str = ""):
        """
        input:
            description: 함수를 설명하는 문장
            level: 로그 레벨
            error_comment: 에러가 발생할 시 추가할 코멘트
        """
        self.description = description
        self.log = self.level[level]
        self.error_comment = error_comment

    def __call__(self, func):
        def wrapper(*args, log_suffix="", **kwargs):
            execute_description = f"/{log_suffix}" if log_suffix else ""
            try:
                try:
                    self.log(f"({func.__name__}{execute_description}) {self.description} - start")
                    result = func(*args, **kwargs)
                except Exception as e:
                    if self.error_comment:
                        raise Exception(self.error_comment) from e
                    else:
                        raise e
            except Exception as e:
                exception_contents = traceback.format_exc()
                # 100 이상의 길이를 가진 bytes는 출력하지 않도록 한다.
                strainer = lambda arg: arg if not (isinstance(arg, bytes) and len(arg) > 100) else f"bytes(length:{len(arg)})"
                _args, _kwargs = (tuple(strainer(i) for i in args), {k: strainer(v) for k, v in kwargs.items()})
                log.error(
                    "\n".join(
                        [
                            f"({func.__name__}) {self.description}",
                            f"\n(Error contents)\n{exception_contents}\n",
                            "------------- function arguments -------------",
                            "(position arguments)",
                            f"-> {pformat(_args)}",
                            f"(keyword arguments)",
                            f"-> {pformat(_kwargs)}",
                            "------------- environment variables -------------",
                            f"{pformat(dict(os.environ))}",
                        ]
                    )
                )
                raise e
            else:
                self.log(f"({func.__name__}{execute_description}) - done")
            return result

        return wrapper
