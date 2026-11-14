# oc-pipelines-cicd

A beginner-friendly Python project demonstrating Continuous Integration (CI) with
GitHub Actions and test execution with OpenShift Pipelines (Tekton).

## Project contents

- `app.py`: small Python application with testable functions.
- `tests/test_app.py`: unit tests executed by `nose`.
- `.flake8`: lint configuration.
- `.github/workflows/workflow.yml`: GitHub Actions workflow that installs dependencies,
  runs `flake8`, and runs unit tests with `nose`.
- `.tekton/tasks.yml`: Tekton `cleanup` and `nose` Tasks.

## Run locally

```bash
python -m pip install -r requirements.txt
flake8 .
nosetests -v
```

## GitHub Actions

Push this repository to GitHub. The workflow runs on pushes and pull requests to
`main` and `master`. Open the repository's **Actions** tab to inspect the run.

## OpenShift Pipelines

Apply the Tekton tasks in a project/namespace where OpenShift Pipelines is installed:

```bash
oc apply -f .tekton/tasks.yml
```

The Tasks expect a shared workspace named `source` that already contains the
checked-out repository. In your Pipeline, first check out/clone the repository into
that workspace, then invoke `cleanup` and `nose`, binding the same workspace to
both tasks. Run that Pipeline and inspect the PipelineRun and TaskRun logs in the
OpenShift console.

> Screenshots and cluster logs must come from your own OpenShift environment.
> They cannot be generated truthfully from this source-code package.

## Project name

`oc-pipelines-cicd`
