# Repo Structure

### **assets/models**

- players
- npcs
- environment
- projectiles
- structures
- items
- particles
- misc

### **assets/blocks**

- `<Block Name>`  /  `<block texture>`.png
- or `<Block Name>` / <6 different face textures, `-x.png`, `+x.png`, `-y.png`, `+y.png`, `-z.png`, `+z.png`>

### **assets/skyboxes**

- `<skybox descriptive name>`/ <6 face textures, `-x.png`, `+x.png`, `-y.png`, `+y.png`, `-z.png`, `+z.png`>

### **assets/ui**

- fonts
- icons
- logos
- Any other UI assets

### **assets/audio**

- sfx
- music

### **assets/maps**

- boilerplate.json (default map)



# Asset Definition / Terminology

- `Entity` - A non-block game object such as an NPC, an interactable Chest, a Door, etc.
    - Example. Zombie, Pig, Chest, Door, Booster Pad, Portal.

- `Misc` - A misc. asset that would be outside of the bounds of the other categories.
    - Example: A muzzle-flash from a gun, footstep marks on ground, bullet hole.

- `Item` - A player-held object.
    - Example: Sword, Axe, Pickaxe, Shield, Fishing Rod, Potion.

- `Block` - A voxel cube that makes up the world’s terrain.
    - Example: Dirt, Wood, Sand, Grass, Stone, Iron, Gold.

- `Sound` - Any sound related asset such as music and effects.
    - Example: Theme Song, Sword Clash, Punch Hit, Level Up Noise, Ambient weather.

- `Particle` - 2D or (more rarely) 3D objects intended to be used as particle effects.
    - Example: Smoke, Dust, Sparks, Fire.

- `Projectile` - 2D or 3D objects intended to be used as projectiles.
    - Examples: Arrows, Lasers, Fireballs, Bullets, Flying Rocks.

- `Environment` - Assets intended to be used for environmental detail / visual enhancements.
    - Examples: Rocks, grasses, flowers, swarms of bugs, rubble.

- `Structure` - Non-block assets that make up structures within the environment
    - Examples: Fences, Light Poles, Signs.
    
- `UI` - Any asset intended to be used in the UI.
    - Examples: Icons, Images, Backgrounds, Fonts.
