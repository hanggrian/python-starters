# Python Starters

![The repository logo.](https://github.com/hendraanggrian/python-starters/raw/assets/logo.png)

Personal Gradle project templates with emphasis on **Python,** separated by
target platform and kind of distribution.

| | Testing | Publishing | Coverage
--- | :---: | :---: | :---:
app | [Pytest] | &cross; | &check;
library | [Pytest] | [Package Index] | &check;
notebook | &cross; | &cross; | &cross;

## Python frameworks

- Built-in Unittest testing framework.
- [Pylint](https://pylint.pycqa.org/en/stable/index.html) code linter with
  third-party ruleset [Rulebook](https://github.com/hendraanggrian/rulebook/).
- [Coverage plugin](https://github.com/pytest-dev/pytest-cov) for Pytest.

## Project layout

- Root directory:
  - GitHub [README](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes/),
    [LICENSE](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository/),
    and [gitignore](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files/)
    file.
  - [EditorConfig](https://editorconfig.org/) enforces IDE settings.
  - [CircleCI](https://circleci.com/) to run test every commit, also triggers
    [Codecov](https://codecov.io/) coverage.
- Website module:
  - [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for
    generating webpages displaying README and other content.
  - The webpages are manually deployed with `mkdocs gh-deploy`.

[Pytest]: https://docs.pytest.org/en/stable/
[Package Index]: https://pypi.org/
