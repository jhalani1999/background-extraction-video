<h2>background-extraction-video</h2>

Goal: Remove the vehicles from the video. And get the background by taking the mean of frames.

<table>
  <tr>
    <th><h3>Input</h3></th>
    <th><h3>Output</h3></th>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/31618900/89549391-de1c2f00-d825-11ea-9007-d0e18af5f76d.png" width="240"></td>
    <td><img src="https://user-images.githubusercontent.com/31618900/89549408-e2e0e300-d825-11ea-9cb4-65458bbf30b6.png" width="240"></td>
  </tr>
</table>

Input/Output is provided in Data Folder.

<h2>background-extraction-video-fixed-area</h2>
<p>In this file, running average concept is applied on the road section of the frame. That is done by the following steps.</p>
<ol>
  <li>Crop the road section from the frame.</li>
  <li>Apply the running average on the cropped frame.</li>
  <li>Absolute difference between original image and cropped image.</li>
  <li>Add the running average image and absolute difference image.</li>
</ol>
  
