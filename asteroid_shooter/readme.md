# Asteroid shooter without classes

1. Create a blank window
   use while loop to get input, get updates, update screen
   set caption to change window name

2. to show images, we need a surface

   1. display surface and a surface
      1. display surface is the main canvas, single display surface, always shown
   2. surface is an image, can have unlimited surfaces, will be visible if it's on the display surface
      surfaces can be created in 3 ways: import image, create one in game, creating text
   3. placing a surface -> surfaces are placed in the display surface with the blit method (block image transfer)
   4. blit(surface, position) -> places the topleft of the surface. position x,y

3. color -> pygame has inbuilt colors, or use rgb tuple

4. placing elements -> x,y but starts from top left
5. images and text -> images can be imported with pygame.image.load('path'). Convert image for better performance. text requires font object, font object can render a string and it returns a surface
6. movement: update position while placing. draw new display surface always, so update position every frame. - cap maximum framerate to make it consistent.
7. rectangle -> make it easeir to place surfaces. eg trying to place surface in the middle. used for collisions and drawing. surface store image, ret stores position and movement.
8. input: mouse, keyboard, touchscreen, controllers. use event loop or separate methods outside of it. Usually done via methods outside event loop. input should be inside player class.
9. rects can be used to draw shapes. pygame.draw.rect ellipse etc.
10. surfaces can be transformed with pygame.transform -> scale/flip
11. delta time -> measures how long it took to create one frame. 1/fps. Can use to keep same at a constant speed regardless of framerate. multiply any movement with delta time -> delta movement. delta time x speed (pixels per frame) x frames per second

Problem with delta time

- when moving rects, we always place integers. This cannot be changed because we need to place them in pixel positions.
- when moving with delta time, we move via floating point numbers.
- this implicit conversation leads to data loss and inconsistent speed.

Laser - created when player clicks the mouse, laser should be in front of the ship 12. pygame can get the time since we started the game. we can create repeated timers.

12. Vector2 -> list that contains x and y. Can do dot product.
13. collision: pygame can detect collisions.
    1.  check if point is in a rect
    2.  check if 2 rects collide
    3.  check how close objects are to each other
    4.  do pixel perfect collisions
