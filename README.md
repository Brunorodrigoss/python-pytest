# python-pytest

| Command | Description |
| ----------- | ----------- |
| pytest | Run all tests |
| pytest -v | Run all test in verbose mode |
| pytest --html="results.html" | Run all tests and generates a file with the results named results.html |
| pytest --junitxml="results.xml"| Run all tests and generates a file with the results named results.xml |
| - | - |
| pytest --markers | List all markers availables |
| pytest -m ui | Run all tests with markers equals "ui"|
| pytest -m "entertainment or engine" | Run all tests marked by entertainment or engine |
| pytest -m "entertainment and engine" | Run all tests marked by entertainment and engine on the same test |
| pytest -m "not engine" | Run all tests except maked by engine |