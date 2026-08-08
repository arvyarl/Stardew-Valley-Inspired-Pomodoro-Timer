# ⭐️ Stardew Valley-Inspired Pomodoro Timer

A desktop-based Pomodoro Timer application developed using **Python, Tkinter, and Pillow**. The application provides a fullscreen graphical interface for managing focused work sessions and scheduled breaks through the Pomodoro Technique.

<p align="center">
  <img src="opening_screen" width="700">
</p>

## Overview

The Pomodoro Timer is designed to help users structure their study or work sessions into focused intervals followed by short and long breaks.

The application automatically manages the session sequence, updates the countdown in real time, and transitions between work and break periods without requiring manual input.

## Features

* 25-minute work sessions
* 5-minute short breaks
* 20-minute long breaks
* Automatic transition between sessions
* Long break after four completed work sessions
* Start and reset controls
* Fullscreen graphical interface
* Custom graphical backgrounds and buttons
* Information screen explaining the Pomodoro cycle
* Automatic font detection with fallback support
* Image-based user interface using Tkinter Canvas

## Pomodoro Cycle

The application follows the following cycle:

| Session     |   Duration |
| ----------- | ---------: |
| Work        | 25 minutes |
| Short Break |  5 minutes |
| Work        | 25 minutes |
| Short Break |  5 minutes |
| Work        | 25 minutes |
| Short Break |  5 minutes |
| Work        | 25 minutes |
| Long Break  | 20 minutes |

After the long break, the cycle repeats.

## Technologies Used

* **Python 3** — Core programming language
* **Tkinter** — Graphical User Interface
* **Pillow (PIL)** — Image loading, resizing, and rendering

## Project Structure

```text
pomodoro-timer/
│
├── main.py
├── opening_bg.jpg
├── start_button.png
├── info_button.png
├── info_bg.jpg
├── timer_bg.jpg
├── timer_start.png
├── timer_reset.png
└── README.md
```

> The image filenames above represent the recommended organization of the project's graphical assets. Ensure that the filenames referenced in `main.py` match the actual files in the project directory.

## Installation

### Prerequisites

Make sure Python 3.x is installed on your system.

Verify your Python installation:

```bash
python --version
```

### Install Dependencies

Install Pillow using pip:

```bash
pip install Pillow
```

Tkinter is included with most standard Python installations. On some Linux distributions, it may need to be installed separately through the system package manager.

## Running the Application

Clone the repository:

```bash
git clone https://github.com/your-username/pomodoro-timer.git
```

Navigate to the project directory:

```bash
cd pomodoro-timer
```

Run the application:

```bash
python main.py
```

The application launches in fullscreen mode.

Press **Escape** to exit fullscreen mode.

## Implementation

### Session Management

The application uses a session counter to determine whether the next interval should be a work session, short break, or long break.

The session logic follows:

```text
Odd-numbered sessions → Work
Even-numbered sessions → Short Break
Every fourth work session → Long Break
```

The countdown is managed using Tkinter's `after()` method, which schedules the next countdown update after one second.

```python
timer = root.after(1000, count_down, count - 1)
```

When the countdown reaches zero, the current timer is cleared and the next Pomodoro session begins automatically.

### Font Detection

The application checks the fonts available on the system and attempts to locate the **Pixel Operator** font.

If the preferred font is unavailable, the program searches for other pixel-style fonts and ultimately falls back to Arial to ensure the application remains functional.

### User Interface

The interface is built using Tkinter's `Canvas` widget. Custom images are used for backgrounds and interactive controls to create the application's visual design.

The application consists of three primary views:

1. **Opening Screen**

   * Start button
   * Information button
   * Custom background

2. **Information Screen**

   * Pomodoro session durations
   * Explanation of the long-break interval

3. **Timer Screen**

   * Countdown display
   * Start button
   * Reset button
   * Custom background

## Reset Functionality

The reset function cancels the active countdown, resets the session counter, and returns the timer to its default 25-minute work interval.

This allows the user to restart the Pomodoro cycle at any point.

## Future Improvements

Potential improvements include:

* Pause and resume functionality
* Customizable work and break durations
* Audio notifications
* Desktop notifications
* Session statistics and productivity tracking
* Persistent session history
* Additional interface themes
* Improved responsiveness across different screen resolutions

## Purpose

This project was developed as a practical application of Python programming, GUI development, event-driven programming, and basic software design concepts.

## Author

**Arvy Aral**

BS Electronics Engineering
