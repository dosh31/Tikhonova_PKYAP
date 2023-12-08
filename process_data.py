import json
import sys
from cm_timer import cm_timer_1
from print_result import print_result
from gen_random import gen_random
from field import field
from unique import Unique

path = sys.argv[1] if len(sys.argv) > 1 else "data_light.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ", с опытом Python", arg))


@print_result
def f4(arg):
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
