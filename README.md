# pre-commit-hooks
Our custom pre-commit hooks

## Example
```yaml
repos:
-   repo: https://github.com/team5499/pre-commit-hooks
    rev: v0.3.1
    hooks:
    -   id: ktlint-wrapper
        args: [--color, --format, --relative, --verbose]
    -   id: detekt-wrapper
        args: [--config .detekt-config.yml]
```
It's highly recommended that you use a config file with `detekt-wrapper`, and set `maxIssues` to 0. The default is 10, and the hook will pass with failures present as long as there are less than 10 of them. This allows failures to slip in a few at a time with each commit, until there are several throughout the repo. Setting `maxIssues` to 0 will prevent any failures from slipping in.
