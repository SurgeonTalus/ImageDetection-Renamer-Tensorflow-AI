# ImageDetectionRenamer-LocalAI-IntelOnly-
Select a folder with images. Tensorflow will create a new name of the images based on their content. 

<h1><b>Description</b></h1>
<p>This script uses TensorFlow to perform object detection on a set of image files in a specified folder. It identifies the object in each image, renames the image file to include the predicted object name, and adds a version number if necessary to avoid overwriting existing files.</p>
<h2><b>Dependencies</b></h2>
<ul>
  <li><code>tkinter</code>: for the GUI used to select the folder.</li>
  <li><code>tensorflow</code>: for the image processing and object detection.</li>
</ul>
<p>To install these dependencies, you can use the following command:</p>
<pre><code>pip install tkinter tensorflow</code></pre>
<h2><b>How to Use</b></h2>
<ol>
  <li>Install the dependencies listed above.</li>
  <li>Download or create a set of image files to process.</li>
  <li>Run the script using a Python interpreter.</li>
  <li>A GUI window will appear allowing you to select the folder containing the image files.</li>
  <li>The script will process each image file in the selected folder, renaming them with the predicted object name and a version number if necessary.</li>
  <li>The original image files will be replaced with the renamed files.</li>
</ol>
<p>Note: The script expects the image files to be in JPEG or PNG format, and will only process files with those extensions. If the script encounters any errors during processing, it will print an error message but continue processing the remaining images.</p>


![Screenshot](Choose%20Files.png)
![Screenshot](Renamed%20Files.png)

https://github.com/SurgeonTalus/ImageDetectionRenamer-LocalAI-IntelOnly-/blob/main/Choose%20Files.png

https://github.com/SurgeonTalus/ImageDetectionRenamer-LocalAI-IntelOnly-/blob/main/Renamed%20Files.png
