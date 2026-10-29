# Virtual 8086 Stepper Motor Laboratory

A small educational mini-project that simulates the 8086 stepper-motor interfacing experiment.
It demonstrates clockwise/anticlockwise rotation, selectable step size, the 8086 ALP listings,
and a simple agent-style plan → validate → execute → verify workflow.

> **Important:** This is a software simulation. It does not control a physical 8086 trainer kit,
> 8255/PPI, driver board, or motor. The I/O addresses and byte sequences below reproduce the
> supplied lab-manual listing for study; verify your trainer-kit's actual interface before
> connecting hardware.

## Project contents

- `Virtual_8086_Stepper_Lab.ipynb` — run interactively in Google Colab.
- `src/stepper_simulator.py` — reusable motor model and 8086-style sequence generator.
- `docs/8086_ALP_Listings.md` — clockwise and anticlockwise assembly listings.
- `docs/Hardware_Notes.md` — lab-manual connection summary and safety notes.
- `requirements.txt` — Python dependencies.

## Run in Google Colab

1. Upload `Virtual_8086_Stepper_Lab.ipynb` to Google Drive, or open it directly in Colab.
2. In Colab, select **Runtime → Run all**.
3. Use the direction, step-count, step-size, and delay controls in the interactive panel.
4. The rotor diagram, execution log, and assembly listing update when you press **Run simulation**.

The notebook installs/imports only common Python packages. If widgets do not display, run:
`!pip install -q ipywidgets matplotlib` and refresh the notebook output.

## Run locally

```bash
python -m pip install -r requirements.txt
jupyter notebook Virtual_8086_Stepper_Lab.ipynb
```

## Simulation model

The simulator uses a four-state full-step sequence:

| State | Coil pattern (A B C D) |
|---|---|
| 0 | 1000 |
| 1 | 0100 |
| 2 | 0010 |
| 3 | 0001 |

Clockwise advances through the sequence; anticlockwise traverses it in reverse. The chosen
step size is the number of electrical full-steps per requested movement unit. This is a
teaching abstraction, not a claim about the physical motor's exact step angle.

## Repository upload

Extract this ZIP, create a GitHub repository, and upload the extracted files (or push them with
Git). Do not upload personal credentials or hardware access details.
