from prefect_github import GitHubRepository

from flows.f_03_map import f_03_map


f_03_map.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flows/f_03_map.py:f_03_map",
).deploy(
    name="test-deploy",
    tags=["test", "project_3"],
    work_pool_name="test-subproc",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/10 * * * *"
)
