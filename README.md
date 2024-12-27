# The client_assets Repo Structure

- **`dump-archive`** - Use to dump anything and everything, and also to archive old models/files.
- **`working`** - Used as a working-repo for in-progress assets.
- **`export`** - Used for completed assets, ready to be added to the boilerplate asset-pack, or generally availible assets. ** Engine-ready assets only, models must be .GLTF!
- **`boilerplate`** - A collection of assets to be delivered as the “base” assets for the Hytopia SDK. - Engine-ready assets only, models must be .GLTF!
    - models
        - entities
            - player
            - npcs
            - environment
            - projectiles
            - structures
        - items
    - blocks
        - <Block Name> / <block texture>.png
    - textures
        - skybox/ <6 face textures, `-x.png`, `+x.png`, `-y.png`, `+y.png`, `-z.png`, `+z.png`>
    - ui
        - Any UI assets
    - sound
        - sfx
        - music

# Asset Types

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
