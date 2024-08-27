from prefect_github import GitHubRepository

from flows.f_02_async_task import f_02_async_task


f_02_async_task.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flows/f_02_async_task.py:f_02_async_task",
).deploy(
    name="test-deploy",
    tags=["test", "project_2"],
    work_pool_name="test-subproc",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/5 * * * *"
)
