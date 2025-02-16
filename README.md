# Lab 2
Kyle Johnsen

<img src="https://github.com/user-attachments/assets/7eec003e-b2cd-4dbb-b50e-36e0966e4b14" width=300/>

# Problem 3 Prompts

## Gemini Flash 2.0

**Prompt:** I want to a python program that allows a user to draw out a polygon by clicking on a canvas at various points. These points should be connected by a line, and when complete (when the clicks a button on the interface) the polygon should be filled. After it is filled, label the coordinates of each point. Allow the labels to be dragged around.

**Result:** This worked okay, but the labels were generated as I clicked and could not be dragged around.  I tried to refine, but was getting nowhere, so I tried a Chat GPT (Free)

## Chat GPT Results (same initial prompt)

**Result:** This worked much better.  At first I thought the result didn't work, as I couldn't drag the labels.  But, then I realized that it had made right click how you drag.

**Refinement:** Add the perimeter and area on the diagram, make the points red, the lines blue, and the fill color gray.  Add a restart button, and do not allow the addition of new points after complete polygon is pressed.  

**Result:** This worked near perfectly.  Subsequent refinements could improve the visibility of the labels a bit, or allow loop closure by clicking on the first point again, or allowing for undo.

## DeepSeek Results (same initial prompt)

**Result:** This added a cool preview line, but the labels were not draggable.  

**Refinement:** The labels are not draggable.  I want to be able to drag them with the right mouse button.  Do not allow points to be added after the polygon is complete.

**Result:** This generally worked, but it left the preview line drawn, which was not nice.  

**Refinement:** Make sure you clear the preview line when completing the polygon.  Also, show the position of the cursor as you move the mouse, so you know where you are clicking. 

**Result:** Almost perfect, but I forgot to add some thigns

**Refinement:** Also, calculate the perimeter and area and add these to the top bottom left corner of the window.  Draw the points as red, and the lines as blue, and the fill color as gray.
