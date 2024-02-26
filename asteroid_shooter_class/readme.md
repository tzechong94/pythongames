# pygame with classes

one object for laser and the asteroid each that contains both surface and rect

1. sprite class -> class that must have rect and a surface
   1. can control graphics, positions, input and update mechanics
   2. each visible element should be a sprite
2. to display a sprite, need to put in a group. group draws sprite on a surface. group can also update sprite
3. updating a sprite
4. store position in vector2 instead of rect. (float, float)
5. rotating surface lowers quality a tiny bit, memory intensive. create an original surf that will be rotated once.
6. pygame.sprite.spritecollide(sprite, group, DoKill) -> check if sprite collides with any sprite inside of the group. DoKill will delete the sprite in the group wihen it happens
7. Mask is a separate object that checks which pixels are occupied in a surface -> for pixel perfect collisions
8. create mask for collision
