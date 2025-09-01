# Contributing to pyRapid

Thank you for your interest in contributing to pyRapid! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, please include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (Python version, OS, etc.)
- Any relevant code snippets or error messages

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Any possible alternatives you've considered
- Examples of how the enhancement would be used

### Pull Requests

1. Fork the repository and create your branch from `master`
2. Install development dependencies: `pip install -e .[dev]`
3. Make your changes and add tests if applicable
4. Ensure all tests pass: `pytest`
5. Update documentation as needed
6. Create a pull request with a clear description of your changes

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/pyrapid.git
cd pyrapid

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e .[dev]

# Run tests
pytest
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to all public functions and classes
- Keep line length under 100 characters

## Testing

- Write tests for any new functionality
- Ensure all tests pass before submitting a PR
- Aim for high test coverage

## License

By contributing, you agree that your contributions will be licensed under the MIT License.