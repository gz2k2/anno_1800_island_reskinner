"""RD3D object categories derived from rd3d_cleaned.csv and tmc_cleaned.csv.

Order matters: the first matching category wins.
Keywords are matched case-insensitively against the complete prop path.
Keep specific categories above broad fallback categories.
Colors are generated automatically by the application.
"""

RD3D_CATEGORIES = {
    # Terrain / geology. Pebbles deliberately remain separate from rocks.
    "Pebbles Ice": ("pebbles_ice",),
    "Pebbles Snow": ("pebbles_snow",),
    "Pebbles Jungle": ("pebbles_jungle", "rocks_pebbles_jungle"),
    "Pebbles Enbesa": ("pebbles_colony02",),
    "Pebbles": ("/pebbles_", "rocks_pebbles/"),
    "Rocks Ice": ("rocks_ice", "rock_ice_"),
    "Rocks Snow No Skirt": ("rocks_snow_noskirt", "rock_snow_noskirt_"),
    "Rocks Snow": ("rocks_snow", "rock_snow_"),
    "Rocks Jungle": ("rocks_jungle", "rock_jungle_"),
    "Rocks Enbesa": ("rocks_colony02", "rock_colony02_"),
    "Rocks Moderate": ("rocks_moderate", "rock_moderate_"),
    "Rocks Coast": ("rocks_coast", "rock_coast_"),
    "Rocks Decoration": ("rocks_decoration",),
    "Rocks Cave": ("rocks_cave",),
    "Rocks": ("/rocks/", "/rock_", "rock_anno_union", "cliff"),

    # Vegetation. Underwater plants, bushes, flowers and grasses stay distinct.
    "Underwater Plants": ("underwater_plant_", "/vegetation/water/"),
    "Bushes Arctic": ("bush_arctic_",),
    "Bushes Dry": ("bush_dry_", "bushes_dry"),
    "Bushes Dead": ("bush_dead_", "bushes_dead"),
    "Bushes Jungle": ("bush_jungle_",),
    "Bushes Moderate": ("bush_moderate_",),
    "Bushes Building Bushes": ("building_bush_",),
    "Bushes": ("/bushes/", "/bush_"),
    "Flowers Jungle": ("flowers_jungle_",),
    "Flowers Moderate": ("flowers_moderate_",),
    "Flowers": ("/flowers_", "flower_"),
    "Grass Arctic": ("grass_arctic_",),
    "Grass Dry": ("grass_dry_", "grass_dry/"),
    "Grass Jungle": ("grass_jungle_",),
    "Grass Moderate": ("grass_moderate_",),
    "Reeds": ("grass_reed_",),
    "Grass": ("/grass/", "/grass_"),

    # Trees. Preserve region/type distinctions visible in the file names.
    "Tree Dead Trees Snow": ("tree_dead_snow_",),
    "Tree Dead Trees Jungle": ("tree_dead_jungle_", "tree_dead_palm_"),
    "Tree Dead Trees": ("/trees/dead/", "/trees_dead/", "tree_dead_", "dead_tree_", "burned_tree_"),
    "Tree Jungle Palms": ("tree_jungle_palm_",),
    "Tree Jungle Mountain Trees": ("jungle_mountain", "mountain_jungle_tree_"),
    "Tree Jungle Trees": ("tree_jungle_",),
    "Tree Fir Trees Snow": ("tree_fir_snow_",),
    "Tree Fir Trees Moderate": ("tree_fir_",),
    "Tree Cypress Trees": ("cypress_tree_",),
    "Tree Acacia Trees": ("/acacia_",),
    "Tree Baobab Trees": ("baobab_tree_",),
    "Tree Stone Pine Trees": ("stone_pine_",),
    "Tree Orange Trees": ("orange_tree_",),
    "Tree Moderate Trees": ("tree_moderate_",),
    "Tree Building Trees": ("building_deco_tree_",),
    "Tree Trees": ("/trees/", "/tree_", "palm_"),

    # Man-made props. Split the obvious families instead of one broad 'Other'.
    "Deco Fences": ("/fences/", "fence_", "wall_clay_", "white_wall_", "hedge_", "sandbag_wall_", "chain_fence_"),
    "Deco Furniture": ("/furniture/", "chair_", "table_", "bench", "desk_", "book_shelf_", "stool_"),
    "Deco Lamps": ("/lamps/", "lamp_", "lightpost_", "lantern_"),
    "Deco Storage Barrels": ("barrel_",),
    "Deco Storage Boxes Crates": ("wooden_box", "box_covered_", "crate_", "ammo_crate", "larg_copper_box"),
    "Deco Storage Cloth": ("cloth_", "clothroll", "carpetroll", "sailing_cloth", "wool_"),
    "Deco Storage Wood": ("wood_log_", "wood_plank_"),
    "Deco Storage Pots Baskets": ("/pot_", "pot_pile_", "basket_", "vase_", "bucket_"),
    "Deco Storage": ("/storage/",),
    "Deco Harbor": ("/harbor/", "fishtrap_", "single_wooden_beam_"),
    "Deco Vehicles": ("/vehicles/", "carriage_", "wagon_", "high_wheeler"),
    "Deco Bones": ("/bones/", "bone_heap_"),
    "Deco Decoration": ("/decoration/",),
    "Deco Electricity": ("/electricity/", "electricity_line_"),
    "Deco Tools": ("/tools/",),

    "Other": (),
}

DEFAULT_RD3D_CATEGORY = "Other"
