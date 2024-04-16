## Koch Curves Generator

This Python program generates Koch curves using the Koch snowflake fractal. The Koch curve is a fractal that looks like a snowflake and is constructed using iterative methods.

### Requirements

- Python 3.x
- NumPy
- Matplotlib

### Installation

1. Install Python from [the official website](https://www.python.org/downloads/).
2. Install required libraries using pip:
   ```
   pip install numpy matplotlib
   ```

### Usage

1. Run the program by executing the provided Python script.
2. Upon running, a graphical user interface (GUI) will appear.
3. Enter the depth of the Koch curve (an integer between 1 and 7) in the input field.
4. Click the "Generate" button to generate the Koch curve.
5. The program will display the Koch curve in the GUI window and save it as an image file (`koch_curve_depth_<depth>.png`).
6. Additionally, an animation showing the construction process of the Koch curve will be saved as a GIF file (`koch_curves.gif`).

### Functionality

- The program uses the Tkinter library for the GUI.
- It utilizes NumPy for mathematical computations and Matplotlib for plotting.
- The Koch curve generation is based on recursive algorithms.
- An animation is created to visualize the iterative construction of the Koch curve.

### Contributors

- Developed by [ahilah](https://github.com/ahilah)

### License

This project is licensed under the [MIT License](LICENSE).

---
For more information, contact anastasiia.hileta.kn.2021@lpnu.ua.