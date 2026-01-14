# MaCFP Python Utilities

This directory contains the Python utilities used by the MaCFP database tools, including a vendored copy of `fdsplotlib.py`.

To keep things simple for users, MaCFP uses a single Python virtual environment and does not require installing Python packages system-wide.

---

## Quick Start (Most Users)

From the root of the `macpf-db` repository, run:

```bash
source ./Utilities/setup_python_env.sh
```

If everything is working, you should see:
- A Python version check
- A virtual environment created or activated
- Required packages installed (first run only)
- A successful `hello_world.py` test

---

## What the Setup Script Does

The setup script performs the following steps:

1. Verifies that Python **3.7 or newer** is available
2. Creates a virtual environment at:
   ```
   macfp-db/.github/macfp_python_env
   ```
3. Installs required Python packages from:
   ```
   macfp-db/.github/requirements.txt
   ```
4. Sets `PYTHONPATH` so MaCFP can find:
   ```
   macfp-db/Utilities/fdsplotlib.py
   ```
5. Runs a small test script (`hello_world.py`) to confirm the environment is working

No system Python files are modified.

---

## Re-running the Script

If the virtual environment already exists, you will be prompted:

```
Do you want to reinstall everything? (y/N)
```

- Enter **N** (default) to reuse the existing environment
- Enter **Y** to delete and recreate it from scratch

---

## Batch / CI Mode

For automated runs (CI jobs or scripts), use:

```bash
source macfp-db/Utilities/setup_python_env.sh --batchmode
```

This will:
- Recreate the virtual environment automatically
- Install all required packages without prompting

---

## Activating the Environment Manually

If the environment already exists and you just want to activate it:

```bash
source macfp-db/.github/macfp_python_env/bin/activate
```

You do not need to rerun the setup script unless dependencies change.

---

## Troubleshooting

### Python Version Error

If you see:

```
Python 3.7 or higher is required
```

Check your Python version:

```bash
python3 --version
```

Ensure that `python3` points to a supported version.

---

### `fdsplotlib` Import Errors

If a script reports:

```
ModuleNotFoundError: No module named 'fdsplotlib'
```

Make sure you have run:

```bash
source macfp-db/Utilities/setup_python_env.sh
```

This script sets `PYTHONPATH` automatically.

---

### Resetting the Environment

To completely reset the Python environment:

```bash
rm -rf macfp-db/.github/macfp_python_env
source macfp-db/Utilities/setup_python_env.sh
```

---

## Notes for Developers

- `fdsplotlib.py` is vendored from the FDS repository
- Updates are performed manually by the MaCFP repository maintainer
- This approach avoids requiring users to manage multiple Python environments or Git submodules

---

## Summary

For most users, this single command is sufficient:

```bash
source macfp-db/Utilities/setup_python_env.sh
```

If it completes successfully, the MaCFP Python tools are ready to use.

