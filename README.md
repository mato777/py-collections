# py-collections

A Python collections library providing enhanced collection types with additional functionality.

## Development Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and Python environment management.

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) installed

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Running Tests

To run all tests:
```bash
uv run pytest
```

To run tests with verbose output:
```bash
uv run pytest -v
```

To run tests with coverage:
```bash
uv run pytest --cov=src/py_collections
```

To run a specific test file:
```bash
uv run pytest tests/test_first.py
```

To run tests in watch mode (re-runs on file changes):
```bash
uv run pytest --watch
```

### Development Commands

- **Install dev dependencies**: `uv sync --group dev`
- **Run linting**: `uv run ruff check .`
- **Format code**: `uv run ruff format .`
- **Type checking**: `uv run mypy src/`

## Project Structure

```
py-collections/
├── src/py_collections/     # Main package source code
├── tests/                  # Test files
├── examples/               # Example usage and demonstrations
├── pyproject.toml         # Project configuration and dependencies
└── README.md              # This file
```

## Features

- Enhanced collection types with additional utility methods
- Type-safe implementations
- Comprehensive test coverage
- Modern Python features (3.13+)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run tests: `uv run pytest`
6. Submit a pull request

## License

[Add your license information here]
