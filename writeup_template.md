#**Finding Lane Lines on the Road** 
This is my first project on self driving car. It was a good experince, though I had to put lot of efforts to complete it since I am new to lot of things like python, computer vision, openCV etc.

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

### Reflection

###1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 7 steps. 

1. First step is to convert image to grayscale
2. Blur image using GaussainBlur
3. Using Canny for edge detection
4. Limiting the area to two lanes
5. Using Hough for getting line coordinates
6. Using draw_lines to connect the lines. Most of the work is done in this section.
   This fucntion calcuates the slope first to determine right and left lane. It also further divides the image vertically to reduce noise. After that function calculates average slope seperate for right and left lane. This slope is further used to derive intercept and then finally to derive corresponding x cordinates for given y cordinates. Finally, it draws line between the derived coordinates.
7. Using weighted_imag to draw line on original image




###2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when I tried to test this for multiple images and creating video. Since slope is not perfect few lines has slight variance with actual lanes. 

Another shortcoming could be to run this thourgh curved lanes.


###3. Suggest possible improvements to your pipeline

A possible improvement would be to tune the parameters further and ignoring lines that has unusually different slope.

Another potential improvement could be to make it work with curved lanes.
