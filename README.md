## Python Example project
Creating a Python project from scratch involves several steps, including setting up a virtual environment, organizing your project structure, writing code, adding documentation, and setting up version control. Here's a step-by-step guide:

### Step-by-Step Guide

* **Set Up a Virtual Environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

* **Install Necessary Packages**:
   ```sh
   pip install --upgrade pip
   pip install sphinx  # For documentation
   pip install sphinx_rtd_theme # For the theme file
   ```

* **Add the project files into repo**:
  - Add the main source file `example.main.py` file into example directory
  - Add the unit test file `test_main.py` into tests directory

* **Set Up Sphinx for Documentation**:
   ```sh
   sphinx-quickstart docs 
   ```
   Please chooise sperate the build and source

* **Configure Sphinx**:
   - Edit `docs/source/conf.py` to include your project directory in the `sys.path`:
     ```python
     import os
     import sys
     sys.path.insert(0, os.path.abspath('../../'))

     # Add extends

     ```

* **Generate API Documentation**:
    - Use the `sphinx-apidoc` command to generate reStructuredText files from your Python modules:
      ```sh
      cd $ROOT
      sphinx-apidoc -o docs/source/ src
      ```
    - Build the HTML documentation:
      ```sh
      make -C docs html
      ```

### Example Project Structure

```
my_python_project/
├── docs/
│   ├── build/
│   ├── source/
│   ├── Makefile
│   └── conf.py
├── example/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── venv/
├── .gitignore
└── README.md
```

### Running Tests

To run your unit tests, you can use the following command:
```sh
python -m unittest discover tests
```

### Building Documentation

To build your documentation, navigate to the `docs` directory and run:
```sh
make html
```

This will generate the HTML documentation in the `docs/build/html` directory, which you can open in a web browser to view your API documentation.

For more information how to update the rst document, please checkout the [example-sphinx-basic](https://github.com/readthedocs-examples/example-sphinx-basic)
