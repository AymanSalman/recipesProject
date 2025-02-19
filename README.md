# Recipes Project

This is a Django-based project for managing recipes. Follow the steps below to set up the project on your local machine.

## Prerequisites

Before you begin, ensure that you have the following installed:

- **Python 3.x** - Install Python from [here](https://www.python.org/downloads/).
- **Git** - Install Git from [here](https://git-scm.com/downloads).
- **Virtual Environment** (recommended for dependency management).

## Steps to Set Up the Project

### 1. Clone the Repository

Clone the repository from GitHub to your local machine. Open a terminal or PowerShell and run the following command:

```bash
git clone https://github.com/AymanSalman/recipesProject.git
```

### 2. Navigate to the Project Directory

Once the repository is cloned, navigate into the project directory:

```bash
cd recipesProject
```

### 3. Create a Virtual Environment

Create a virtual environment to manage the dependencies for the project. This ensures that your project dependencies do not conflict with other Python projects on your system:

```bash
python -m venv .venv  # for linux/mac : python3 -m venv .venv
```

### 4. Activate the Virtual Environment

Now, activate the virtual environment:

```bash
.\.venv\Scripts\Activate  # for linux/mac : source .venv/bin/activate
```


### 5. Install Project Dependencies

With the virtual environment activated, install the project dependencies by running the following command:

```bash
pip install -r requirements.txt
```


### 6. Run the Development Server

Now that the environment is set up, you can start the Django development server. Run the following command:

```bash
python manage.py runserver
```


----------------------------------------------------------------------------------------------------------
### 7. Deactivate the Virtual Environment (Optional)

When you are finished working on the project, deactivate the virtual environment by running:

```bash
deactivate
```




