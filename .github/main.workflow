workflow "Release to pypi" {
  on = "release"
  resolves = ["publish"]
}

action "publish" {
  uses = "mariamrf/py-package-publish-action@master"
  secrets = [
    "TWINE_USERNAME",
    "TWINE_PASSWORD",
  ]
  env = {
    PYTHON_VERSION = "3.7.3"
  }
}

workflow "Test" {
  on = "push"
  resolves = ["Test with tox"]
}

action "Test with tox" {
  uses = "njzjz/actions/tox-conda@master"
  secrets = [
    "COVERALLS_REPO_TOKEN",
    "CODECOV_TOKEN",
  ]
}
