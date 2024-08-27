from prefect_github import GitHubRepository

from flows.f_01_quick_start import f_01_quick_start


f_01_quick_start.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flows/f_01_quick_start.py:f_01_quick_start",
).deploy(
    name="test-deploy",
    tags=["test", "project_1"],
    work_pool_name="docker",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="1 * * * *"
)
