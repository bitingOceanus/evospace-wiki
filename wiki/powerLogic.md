# Power Logic Circuit Example
A simple circuit which solves the problem where there may not be sufficient power to run the Fusion Reactor.

*Put right here a picture of electricity usage*

Observe our power plant does produce enough energy to create Neutronium, but not continuously. We can't run the thing full out because it will drain the battery buffer and entiirely consume electricity production.

One way to solve this is by controlling the Fusion Reactor with a switch. Keep the switch off until sufficient electricity and heat buffer storage is available, then turn the switch off and let it run until storage is exhausted.
* If the reactor is off and the battery is full, turn the smelter on
* If the reactor is on and the battery is empty, turn the smelter off

Break this down into 4 components
* Read the battery, compare to full. Set X=1 when battery is full, set X=0 when battery is not full
* Read the battery, compare to empty. Set Y=0 when battery is empty, set Y=0 when battery is not empty
* Read the state of the switch, a function provided by the Logic Interface device. Easy money
* Set the state of the switch, a function provided by the Logic Controller. This is the output of our circuit

The three inputs determine our desired output.

*Here is where the truth table goes*

My smart cousin helped me with the algorithm to make this happen. He said something about http://www.32x8.com/var3.html and provided the answer:

```CONTROL = X OR (NOT Y and SWITCH)```

We can do this! Here is my solution, not as tidy as I would like but sufficient.

*Picture of actual circuit*

## walk through the details of each part

* Interface and Circuit which checks empty (Y)
* Const and Circuit which sets NOT Y
* Interface which checks state of switch
* Circuit which sets AND condition for (NOT Y and SWITCH)
* Interface and Circuit which checks full (X)
* Circuit which sets output, the OR part
* Controller which applies result to switch

And there you have it. I am certain someone smarter will come up with a more elegant solution. Hopefully you've found this entertaining and helpful. Hit us up on Discord with problems, suggestions, comments.

-- Quazar

This page also serves as an example of adding a page to the wiki :) 
* Start by creating a new page under evospace-wiki/wiki, I called this one powerLogic.md
* https://wavelet-noise.github.io/evospace-wiki/editing has some clues. 
* Need to figure out how to add images...
