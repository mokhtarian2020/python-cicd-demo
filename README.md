# Python CI/CD Application

# 🚀 Python CI/CD Learning Demo

> **A hands-on project to learn Continuous Integration and Continuous Deployment with GitHub Actions**

This project demonstrates a complete CI/CD pipeline using GitHub Actions, perfect for learning how modern software development workflows work!

## 📚 What You'll Learn

- ✅ **Continuous Integration (CI)**: Automatically test code when changes are made
- 🚢 **Continuous Deployment (CD)**: Automatically deploy code to different environments
- 🧪 **Automated Testing**: Run tests across multiple Python versions
- 🔍 **Code Quality**: Linting, formatting, and security checks
- 🏗️ **Build Automation**: Package and artifact management
- 🎭 **Environment Management**: Staging vs Production deployments

## 🏗️ Project Structure

```
python-cicd-app/
├── .github/workflows/          # GitHub Actions workflows
│   ├── ci.yml                 # Continuous Integration pipeline
│   └── cd.yml                 # Continuous Deployment pipeline
├── src/                       # Source code
│   ├── main.py               # Main application logic
│   └── utils/                # Utility functions
│       └── math_helpers.py   # Math helper functions
├── tests/                     # Test files
│   ├── test_main.py          # Tests for main.py
│   └── test_utils.py         # Tests for utils
├── requirements.txt           # Production dependencies
├── requirements-dev.txt       # Development dependencies
├── pytest.ini               # Test configuration
└── README.md                 # This file!
```

## 🚀 How the CI/CD Works

### 🔄 CI Pipeline (Continuous Integration)

When you push code or create a pull request, the CI pipeline automatically:

1. **📝 Code Quality & Linting**
   - Checks code style with `flake8`
   - Verifies formatting with `black`

2. **🧪 Run Tests**
   - Tests on Python 3.8, 3.9, and 3.10
   - Generates test coverage reports
   - Ensures all tests pass

3. **🔒 Security Scan**
   - Scans code for security vulnerabilities with `bandit`

4. **🏗️ Build Application**
   - Compiles Python code
   - Creates deployment artifacts

### 🚢 CD Pipeline (Continuous Deployment)

After CI passes successfully:

1. **🎭 Deploy to Staging**
   - Automatically deploys to staging environment
   - Runs smoke tests
   - Available for testing

2. **🏭 Deploy to Production**
   - Requires manual approval (in GitHub environments)
   - Deploys to production environment
   - Runs health checks
   - Sends notifications

3. **⏪ Rollback Plan**
   - Automatically rolls back if deployment fails

## 🎯 Try It Yourself!

### 1. 🧪 Test Locally First

```bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Check code quality
flake8 src/ tests/
black --check src/ tests/

# Run the app
python src/main.py
```

### 2. 🚀 Trigger CI/CD

1. **Push to GitHub** - This will trigger the CI pipeline
2. **Create a Pull Request** - Shows CI status checks
3. **Merge to main** - Triggers both CI and CD pipelines

### 3. 👀 Watch the Magic Happen

Go to your GitHub repo → **Actions** tab to see:
- ✅ CI pipeline running tests, linting, security checks
- 🚢 CD pipeline deploying to staging and production
- 📊 Detailed logs for each step

## 🧪 Example Test Results

The project includes comprehensive tests:

```python
# Tests basic math functions
def test_add_numbers():
    assert add_numbers(2, 3) == 5

# Tests error handling  
def test_calculate_area_negative_values():
    with pytest.raises(ValueError):
        calculate_area(-5, 3)

# Tests utility functions
def test_factorial():
    assert factorial(5) == 120
```

## 🔍 Understanding the Workflows

### CI Workflow Features:
- **Matrix builds**: Tests on multiple Python versions
- **Dependency caching**: Speeds up builds
- **Parallel jobs**: Runs linting, testing, security in parallel
- **Artifact upload**: Saves build results for CD

### CD Workflow Features:
- **Environment protection**: Manual approval for production
- **Conditional deployment**: Only runs if CI passes
- **Health checks**: Verifies deployment success
- **Rollback capability**: Handles deployment failures

## 🎓 Learning Exercises

Try these to deepen your understanding:

1. **Break a test** - Change a function and see CI fail
2. **Add a new feature** - Write code + tests + watch CI/CD run
3. **Modify workflows** - Add new steps or change environments
4. **Security testing** - Add a security vulnerability and see it detected

## 🛠️ Technologies Used

- **GitHub Actions**: CI/CD platform
- **Python**: Programming language
- **pytest**: Testing framework
- **flake8**: Code linting
- **black**: Code formatting
- **bandit**: Security scanning
- **pytest-cov**: Test coverage

## 🎯 Key CI/CD Concepts Demonstrated

| Concept | What It Does | Where to See It |
|---------|--------------|-----------------|
| **Continuous Integration** | Automatically test every code change | `.github/workflows/ci.yml` |
| **Continuous Deployment** | Automatically deploy passing code | `.github/workflows/cd.yml` |
| **Pipeline Stages** | Break CI/CD into logical steps | Jobs in workflow files |
| **Environment Promotion** | Deploy through staging → production | `deploy-staging` → `deploy-production` |
| **Quality Gates** | Block deployment if quality checks fail | `needs:` dependencies in workflows |
| **Rollback Strategy** | Automatic recovery from failed deployments | `rollback:` job in CD |

## 🚨 Common Issues & Solutions

- **Tests failing?** Check the test output in GitHub Actions
- **Linting errors?** Run `black src/ tests/` to auto-format
- **Import errors?** Make sure `__init__.py` files exist
- **Workflow not running?** Check if `.github/workflows/` path is correct

## 🎉 Success!

If you see ✅ green checkmarks in your GitHub Actions, congratulations! You've successfully:

- Set up automated testing
- Implemented code quality checks
- Created a deployment pipeline
- Learned core CI/CD concepts

**Next steps**: Try adding Docker, deploying to cloud platforms, or setting up monitoring!

---

*Happy learning! 🎓 CI/CD makes software development faster, safer, and more reliable.* The application includes basic functionality and automated testing to ensure code quality.

## Project Structure

```
python-cicd-app
├── .github
│   └── workflows
│       ├── ci.yml
│       └── cd.yml
├── src
│   ├── __init__.py
│   ├── main.py
│   └── utils
│       └── __init__.py
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── pytest.ini
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-cicd-app.git
   cd python-cicd-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```bash
python src/main.py
```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## CI/CD

This project is configured with GitHub Actions for CI/CD. The CI workflow runs tests automatically on code push to the main branch. The CD workflow can be configured to deploy the application after successful tests.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.