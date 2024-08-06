import sys; sys.path.append("/workspaces/tir102/prefect-demo/src")

from prefect import flow
from flow.f_02_async_task import f_02_async_task
from flow.f_04_forloop_submit import f_04_forloop_submit

@flow(name="dependency_flow")
def dependency_flow() -> None:
    f_02_async_task()
    f_04_forloop_submit()

if __name__ == "__main__":
    dependency_flow()
