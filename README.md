Blueprint Analyzer

Blueprint Analyzer is a Python project that uses OpenCV to process and analyze blueprint images. The script detects contours, calculates their areas, and converts pixel-based areas to real-world units (e.g., square meters). This is particularly useful for tasks like room measurement and blueprint analysis.
Features

    Detects edges and contours from blueprint images.
    Calculates the area of each detected contour in pixels and converts it to real-world units.
    Saves the following processed images:
        Original Blueprint
        Edges (processed image)
        Outlined Blueprint
        Outlined Blueprint with Unit Conversion
    Designed to work with opencv-python-headless for environments without GUI support.

How to Use

    Clone the repository:

git clone git@github.com:your-username/blueprint-analyzer.git

Navigate to the project directory:

cd blueprint-analyzer

Install the required dependencies:

pip install -r requirements.txt

Run the script and provide the path to a blueprint image:

    python3 blueprint_analyzer.py

Example Output

    Console Output:

    Contour 0: Area = 25.30 square meters
    Contour 1: Area = 15.75 square meters
    ...

    Saved Images:
        original_blueprint.jpg
        edges.jpg
        outlined_blueprint.jpg
        outlined_blueprint_with_units.jpg

Requirements

    Python 3.6 or higher
    OpenCV (opencv-python-headless)
