# Apply Gevent monkey patching of stdlib
from gevent import monkey as _monkey
_monkey.patch_all()


from .user.sequential_taskset import SequentialTaskSet
from .user import wait_time
from .user.task import task, tag, TaskSet
from .user.users import HttpUser, User
from .user.wait_time import between, constant, constant_pacing

from .event import Events
events = Events()

__version__ = "0.999"
__all__ = (
    "SequentialTaskSet",
    "wait_time",
    "task", "tag", "TaskSet",
    "HttpUser", "User"
    "between", "constant", "constant_pacing"
    "events",
)

# Used for raising a DeprecationWarning if old Locust/HttpLocust is used
from .util.deprecation import DeprecatedLocustClass as Locust
from .util.deprecation import DeprecatedHttpLocustClass as HttpLocust
