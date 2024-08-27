from prefect_github import GitHubRepository

from flows.f_04_forloop_submit import f_04_forloop_submit


f_04_forloop_submit.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flows/f_04_forloop_submit.py:f_04_forloop_submit",
).deploy(
    name="test-deploy",
    tags=["test", "project_4"],
    work_pool_name="test-subproc",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/30 0-8,9-15,16-23 * * *"
)
