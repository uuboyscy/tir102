from prefect_github import GitHubRepository

from flows.hello_world import hello_world

hello_world.from_source(
    source=GitHubRepository.load("github-prefect-demo"),
    entrypoint="src/flows/hello_world.py:hello_world",
).deploy(
    name="test-deploy",
    tags=["test", "project_5"],
    work_pool_name="test-subproc",
    job_variables=dict(pull_policy="Never"),
    # parameters=dict(name="Marvin"),
    cron="*/30 0-8,9-15,16-23 * * *"
)