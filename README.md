<h1 id="🌐-course-mini-projects-ee604---image-processing">🌐 Course Mini-Projects <strong>(EE604 - Image Processing)</strong></h1>
<p>Welcome to the repository showcasing solutions to image processing problems.
These assignments were tackled during a digital image processing course (EE604 - Image Processing under Prof. Tushar Sandhan), implementing solutions in Python using OpenCV and NumPy.</p>
<h2 id="🚩-problem-1---indian-flag-orientation-detection">🚩 Problem 1 - Indian Flag Orientation Detection</h2>
<h3 id="task-determine-the-orientation-of-the-indian-flag-in-various-images-and-generate-a-top-view-representation"><strong>Task:</strong> <em>Determine the orientation of the Indian flag in various images and generate a top-view representation.</em></h3>
<h3 id="approach"><strong>Approach:</strong></h3>
<ol>
<li>Utilized RGB values and converted them to HSV to detect the orange part of the flag.</li>
<li>Identified the orientation based on the detected orange region.</li>
<li>Generated the correct output image with the flag oriented from the top.</li>
</ol>
<h2 id="🎶-problem-2---material-type-detection-from-audio">🎶 Problem 2 - Material Type Detection from Audio</h2>
<h3 id="task-differentiate-between-metal-and-cardboard-sounds-in-provided-mp3-files"><strong>Task:</strong> <em>Differentiate between metal and cardboard sounds in provided .mp3 files.</em></h3>
<h3 id="approach-1"><strong>Approach:</strong></h3>
<ol>
<li>Calculated the Mel spectrogram of the audio.</li>
<li>Computed the mean amplitude, removing silent parts.</li>
<li>Determined the material type based on the amplitude (metal typically louder than cardboard).</li>
</ol>
<h2 id="📜-problem-3---sanskrit-shloka-text-rotation">📜 Problem 3 - Sanskrit Shloka Text Rotation</h2>
<h3 id="task-detect-the-angle-of-rotation-in-sanskrit-shlokas-and-rotate-the-text-back-to-its-upright-form"><strong>Task:</strong> <em>Detect the angle of rotation in Sanskrit Shlokas and rotate the text back to its upright form.</em></h3>
<h3 id="approach-2"><strong>Approach:</strong></h3>
<ol>
<li>Used contours to detect text and approximated it as a line to find the rotation angle.</li>
<li>Checked for specific &#39;T&#39; shaped patterns to decide the rotation direction.</li>
<li>Rotated the image accordingly to bring the text to an upright position.</li>
</ol>
<h2 id="🌋-problem-4---lava-image-segmentation">🌋 Problem 4 - Lava Image Segmentation</h2>
<h3 id="task-segment-lava-from-images-containing-lava-and-people"><strong>Task:</strong> <em>Segment lava from images containing lava and people.</em></h3>
<h3 id="approach-3"><strong>Approach:</strong></h3>
<ol>
<li>Applied mean-shift clustering to segment different sections of the image.</li>
<li>Converted to YCrCb color format for better sensitivity to lava color.</li>
<li>Employed K-means with K=2 to separate foreground from background.</li>
<li>Utilized Otsu&#39;s thresholding to refine segmentation.</li>
<li>Converted the grayscale image to binary format for final segmentation.</li>
</ol>
<h2 id="🧑🤝🧑-problem-5---real-vs-fake-raavana-head-detection">🧑‍🤝‍🧑 Problem 5 - Real vs. Fake Raavana Head Detection</h2>
<h3 id="task-differentiate-between-real-and-fake-raavana-heads-in-given-images"><strong>Task:</strong> <em>Differentiate between real and fake Raavana heads in given images.</em></h3>
<h3 id="approach-4"><strong>Approach:</strong></h3>
<ol>
<li>Applied k-means clustering with k=5 to blur and segment the image.</li>
<li>Employed morphological transformations to extract the heads of Raavana.</li>
<li>Counted the number of contours on the left and right of the central head.</li>
<li>Classified the image as &#39;real&#39; if there were 4 heads to the left and 5 heads to the right, else &#39;fake&#39;.</li>
</ol>
<p>Feel free to explore each problem folder for detailed implementations and results.</p>
