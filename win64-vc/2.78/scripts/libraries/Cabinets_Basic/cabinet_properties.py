import bpy
import os
from mv import fd_types, unit, utils

enum_cabinet_types = [('Base',"Base","Base Cabinet"),
                      ('Tall',"Tall","Tall Cabinet"),
                      ('Upper',"Upper","Upper Cabinet"),
                      ('Sink',"Sink","Sink Cabinet"),
                      ('Suspended',"Suspended","Suspended Cabinet")]

class PROPERTIES_Cabinet_Sizes(bpy.types.PropertyGroup):
    base_cabinet_depth = bpy.props.FloatProperty(name="Base Cabinet Depth",
                                                 description="Default depth for base cabinets",
                                                 default=unit.inch(23.0),
                                                 unit='LENGTH')
    
    base_cabinet_height = bpy.props.FloatProperty(name="Base Cabinet Height",
                                                  description="Default height for base cabinets",
                                                  default=unit.inch(34.0),
                                                  unit='LENGTH')
    
    base_inside_corner_size= bpy.props.FloatProperty(name="Base Inside Corner Size",
                                                     description="Default width and depth for the inside base corner cabinets",
                                                     default=unit.inch(36.0),
                                                     unit='LENGTH')
    
    tall_cabinet_depth = bpy.props.FloatProperty(name="Tall Cabinet Depth",
                                                 description="Default depth for tall cabinets",
                                                 default=unit.inch(25.0),
                                                 unit='LENGTH')
    
    tall_cabinet_height = bpy.props.FloatProperty(name="Tall Cabinet Height",
                                                  description="Default height for tall cabinets",
                                                  default=unit.inch(84.0),
                                                  unit='LENGTH')
    
    upper_cabinet_depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                  description="Default depth for upper cabinets",
                                                  default=unit.inch(12.0),
                                                  unit='LENGTH')
    
    upper_cabinet_height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                   description="Default height for upper cabinets",
                                                   default=unit.inch(34.0),
                                                   unit='LENGTH')
    
    upper_inside_corner_size= bpy.props.FloatProperty(name="Upper Inside Corner Size",
                                                      description="Default width and depth for the inside upper corner cabinets",
                                                      default=unit.inch(24.0),
                                                      unit='LENGTH')
    
    sink_cabinet_depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                 description="Default depth for sink cabinets",
                                                 default=unit.inch(23.0),
                                                 unit='LENGTH')
    
    sink_cabinet_height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                  description="Default height for sink cabinets",
                                                  default=unit.inch(34.0),
                                                  unit='LENGTH')

    suspended_cabinet_depth = bpy.props.FloatProperty(name="Upper Cabinet Depth",
                                                      description="Default depth for suspended cabinets",
                                                      default=unit.inch(23.0),
                                                      unit='LENGTH')
    
    suspended_cabinet_height = bpy.props.FloatProperty(name="Upper Cabinet Height",
                                                       description="Default height for suspended cabinets",
                                                       default=unit.inch(6.0),
                                                       unit='LENGTH')

    column_width = bpy.props.FloatProperty(name="Column Width",
                                           description="Default width for cabinet columns",
                                           default=unit.inch(2),
                                           unit='LENGTH')

    width_1_door = bpy.props.FloatProperty(name="Width 1 Door",
                                           description="Default width for one door wide cabinets",
                                           default=unit.inch(18.0),
                                           unit='LENGTH')
    
    width_2_door = bpy.props.FloatProperty(name="Width 2 Door",
                                           description="Default width for two door wide and open cabinets",
                                           default=unit.inch(36.0),
                                           unit='LENGTH')
    
    width_drawer = bpy.props.FloatProperty(name="Width Drawer",
                                           description="Default width for drawer cabinets",
                                           default=unit.inch(18.0),
                                           unit='LENGTH')
    
    base_width_blind = bpy.props.FloatProperty(name="Base Width Blind",
                                               description="Default width for base blind corner cabinets",
                                               default=unit.inch(48.0),
                                               unit='LENGTH')
    
    tall_width_blind = bpy.props.FloatProperty(name="Tall Width Blind",
                                               description="Default width for tall blind corner cabinets",
                                               default=unit.inch(48.0),
                                               unit='LENGTH')
    
    blind_panel_reveal = bpy.props.FloatProperty(name="Blind Panel Reveal",
                                                 description="Default reveal for blind panels",
                                                 default=unit.inch(3.0),
                                                 unit='LENGTH')
    
    inset_blind_panel = bpy.props.BoolProperty(name="Inset Blind Panel",
                                               description="Check this to inset the blind panel into the cabinet carcass",
                                               default=True)
    
    upper_width_blind = bpy.props.FloatProperty(name="Upper Width Blind",
                                                description="Default width for upper blind corner cabinets",
                                                default=unit.inch(36.0),
                                                unit='LENGTH')

    height_above_floor = bpy.props.FloatProperty(name="Height Above Floor",
                                                 description="Default height above floor for upper cabinets",
                                                 default=unit.inch(84.0),
                                                 unit='LENGTH')
    
    equal_drawer_stack_heights = bpy.props.BoolProperty(name="Equal Drawer Stack Heights", 
                                                        description="Check this make all drawer stack heights equal. Otherwise the Top Drawer Height will be set.", 
                                                        default=True)
    
    top_drawer_front_height = bpy.props.FloatProperty(name="Top Drawer Front Height",
                                                      description="Default top drawer front height.",
                                                      default=unit.inch(6.0),
                                                      unit='LENGTH')

    def draw(self,layout):
        col = layout.column(align=True)

        box = col.box()
        box.label("Standard Frameless Cabinet Sizes:")
        
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self,"base_cabinet_height",text="Height")
        row.prop(self,"base_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Tall:")
        row.prop(self,"tall_cabinet_height",text="Height")
        row.prop(self,"tall_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self,"upper_cabinet_height",text="Height")
        row.prop(self,"upper_cabinet_depth",text="Depth")

        row = box.row(align=True)
        row.label("Sink:")
        row.prop(self,"sink_cabinet_height",text="Height")
        row.prop(self,"sink_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("Suspended:")
        row.prop(self,"suspended_cabinet_height",text="Height")
        row.prop(self,"suspended_cabinet_depth",text="Depth")
        
        row = box.row(align=True)
        row.label("1 Door Wide:")
        row.prop(self,"width_1_door",text="Width")
        
        row = box.row(align=True)
        row.label("2 Door Wide:")
        row.prop(self,"width_2_door",text="Width")
        
        row = box.row(align=True)
        row.label("Drawer Stack Width:")
        row.prop(self,"width_drawer",text="Width")
        
        box = col.box()
        box.label("Blind Cabinet Widths:")
        
        row = box.row(align=True)
        row.label('Base:')
        row.prop(self,"base_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Tall:')
        row.prop(self,"tall_width_blind",text="Width")
        
        row = box.row(align=True)
        row.label('Upper:')
        row.prop(self,"upper_width_blind",text="Width")
        
        box = col.box()
        box.label("Inside Corner Cabinet Sizes:")
        row = box.row(align=True)
        row.label("Base:")
        row.prop(self,"base_inside_corner_size",text="")
        
        row = box.row(align=True)
        row.label("Upper:")
        row.prop(self,"upper_inside_corner_size",text="")
        
        box = col.box()
        box.label("Placement:")
        row = box.row(align=True)
        row.label("Height Above Floor:")
        row.prop(self,"height_above_floor",text="")
        
        box = col.box()
        box.label("Drawer Heights:")
        row = box.row(align=True)
        row.prop(self,"equal_drawer_stack_heights")
        if not self.equal_drawer_stack_heights:
            row.prop(self,"top_drawer_front_height")

bpy.utils.register_class(PROPERTIES_Cabinet_Sizes)

class PROPERTIES_Exterior_Defaults(bpy.types.PropertyGroup):
    inset_door = bpy.props.BoolProperty(name="Inset Door", 
                              description="Check this to use inset doors", 
                              default=False)
    
    inset_reveal = bpy.props.FloatProperty(name="Inset Reveal",
                                 description="This sets the reveal for inset doors.",
                                 default=unit.inch(.125),
                                 unit='LENGTH',
                                 precision=4)
    
    left_reveal = bpy.props.FloatProperty(name="Left Reveal",
                                description="This sets the left reveal for overlay doors.",
                                default=unit.inch(.0625),
                                unit='LENGTH',
                                precision=4)
    
    right_reveal = bpy.props.FloatProperty(name="Right Reveal",
                                 description="This sets the right reveal for overlay doors.",
                                 default=unit.inch(.0625),
                                 unit='LENGTH',
                                 precision=4)
    
    base_top_reveal = bpy.props.FloatProperty(name="Base Top Reveal",
                                    description="This sets the top reveal for base overlay doors.",
                                    default=unit.inch(.25),
                                    unit='LENGTH',
                                    precision=4)
    
    tall_top_reveal = bpy.props.FloatProperty(name="Tall Top Reveal",
                                    description="This sets the top reveal for tall overlay doors.",
                                    default=unit.inch(0),
                                    unit='LENGTH',
                                    precision=4)
    
    upper_top_reveal = bpy.props.FloatProperty(name="Upper Top Reveal",
                                     description="This sets the top reveal for upper overlay doors.",
                                     default=unit.inch(0),
                                     unit='LENGTH',
                                     precision=4)
    
    base_bottom_reveal = bpy.props.FloatProperty(name="Base Bottom Reveal",
                                       description="This sets the bottom reveal for base overlay doors.",
                                       default=unit.inch(0),
                                       unit='LENGTH',
                                       precision=4)
    
    tall_bottom_reveal = bpy.props.FloatProperty(name="Tall Bottom Reveal",
                                       description="This sets the bottom reveal for tall overlay doors.",
                                       default=unit.inch(0),
                                       unit='LENGTH',
                                       precision=4)
    
    upper_bottom_reveal = bpy.props.FloatProperty(name="Upper Bottom Reveal",
                                        description="This sets the bottom reveal for upper overlay doors.",
                                        default=unit.inch(.25),
                                        unit='LENGTH',
                                        precision=4)
    
    vertical_gap = bpy.props.FloatProperty(name="Vertical Gap",
                                 description="This sets the distance between double doors.",
                                 default=unit.inch(.125),
                                 unit='LENGTH',
                                 precision=4)
    
    door_to_cabinet_gap = bpy.props.FloatProperty(name="Door to Cabinet Gap",
                                        description="This sets the distance between the back of the door and the front cabinet edge.",
                                        default=unit.inch(.125),
                                        unit='LENGTH',
                                        precision=4)
    
    #PULL OPTIONS
    base_pull_location = bpy.props.FloatProperty(name="Base Pull Location",
                                       description="Z Distance from the top of the door edge to the top of the pull",
                                       default=unit.inch(2),
                                       unit='LENGTH') 
    
    tall_pull_location = bpy.props.FloatProperty(name="Tall Pull Location",
                                       description="Z Distance from the bottom of the door edge to the center of the pull",
                                       default=unit.inch(40),
                                       unit='LENGTH')
    
    upper_pull_location = bpy.props.FloatProperty(name="Upper Pull Location",
                                        description="Z Distance from the bottom of the door edge to the bottom of the pull",
                                        default=unit.inch(2),
                                        unit='LENGTH') 
    
    center_pulls_on_drawers = bpy.props.BoolProperty(name="Center Pulls on Drawers",
                                           description="Center pulls on the drawer heights. Otherwise the pull z location is controlled with Drawer Pull From Top",
                                           default=False) 
    
    no_pulls = bpy.props.BoolProperty(name="No Pulls",
                            description="Check this option to turn off pull hardware",
                            default=False) 
    
    pull_from_edge = bpy.props.FloatProperty(name="Pull From Edge",
                                   description="X Distance from the door edge to the pull",
                                   default=unit.inch(1.5),
                                   unit='LENGTH') 
    
    drawer_pull_from_top = bpy.props.FloatProperty(name="Drawer Pull From Top",
                                         description="When Center Pulls on Drawers is off this is the amount from the top of the drawer front to the enter pull",
                                         default=unit.inch(1.5),unit='LENGTH') 
    
    pull_rotation = bpy.props.FloatProperty(name="Pull Rotation",
                                  description="Rotation of pulls on doors",
                                  default=0,
                                  subtype='ANGLE') 

    pull_name = bpy.props.StringProperty(name="Pull Name",default="Test Pull")

    def draw(self,layout):
        col = layout.column(align=True)
        
        box = col.box()
        box.label("Door & Drawer Defaults:")
        
        row = box.row(align=True)
        row.prop(self,"inset_door")
        row.prop(self,"no_pulls")
        
        if not self.no_pulls:
            box = col.box()
            box.label("Pull Placement:")
            
            row = box.row(align=True)
            row.label("Base Doors:")
            row.prop(self,"base_pull_location",text="From Top of Door")
            
            row = box.row(align=True)
            row.label("Tall Doors:")
            row.prop(self,"tall_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Upper Doors:")
            row.prop(self,"upper_pull_location",text="From Bottom of Door")
            
            row = box.row(align=True)
            row.label("Distance From Edge:")
            row.prop(self,"pull_from_edge",text="")
            
            row = box.row(align=True)
            row.prop(self,"center_pulls_on_drawers")
    
            if not self.center_pulls_on_drawers:
                row.prop(self,"drawer_pull_from_top",text="Distance From Top")
        
        box = col.box()
        box.label("Door & Drawer Reveals:")
        
        if self.props.exterior_defaults.inset_door:
            row = box.row(align=True)
            row.label("Inset Reveals:")
            row.prop(self,"inset_reveal",text="")
        else:
            row = box.row(align=True)
            row.label("Standard Reveals:")
            row.prop(self,"left_reveal",text="Left")
            row.prop(self,"right_reveal",text="Right")
            
            row = box.row(align=True)
            row.label("Base Door Reveals:")
            row.prop(self,"base_top_reveal",text="Top")
            row.prop(self,"base_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Tall Door Reveals:")
            row.prop(self,"tall_top_reveal",text="Top")
            row.prop(self,"tall_bottom_reveal",text="Bottom")
            
            row = box.row(align=True)
            row.label("Upper Door Reveals:")
            row.prop(self,"upper_top_reveal",text="Top")
            row.prop(self,"upper_bottom_reveal",text="Bottom")
            
        row = box.row(align=True)
        row.label("Vertical Gap:")
        row.prop(self,"vertical_gap",text="")
    
        row = box.row(align=True)
        row.label("Door To Cabinet Gap:")
        row.prop(self,"door_to_cabinet_gap",text="")

bpy.utils.register_class(PROPERTIES_Exterior_Defaults)

class PROPERTIES_Scene_Properties(bpy.types.PropertyGroup):
    
    defaults_tabs = bpy.props.EnumProperty(name="Main Tabs",
                                           items=[('SIZES',"Sizes",'Show the default sizes and placement location for cabinets'),
                                                  ('EXTERIOR',"Exterior",'Show the default door and drawer settings')],
                                           default = 'SIZES')
    
    #POINTERS
    size_defaults = bpy.props.PointerProperty(name="Sizes",type=PROPERTIES_Cabinet_Sizes)
    exterior_defaults = bpy.props.PointerProperty(name="Exterior Options",type=PROPERTIES_Exterior_Defaults)

    def draw(self,layout):
        box = layout.box()
        row = box.row()
        row.prop(self,'defaults_tabs',expand=True)
        
        if self.defaults_tabs == 'SIZES':
            self.size_defaults.draw(box)
        
        if self.defaults_tabs == 'EXTERIOR':
            self.exterior_defaults.draw(box)

class PROPERTIES_Object_Properties(bpy.types.PropertyGroup):
    
    cabinet_type = bpy.props.EnumProperty(name="Cabinet Type",
                                          items=enum_cabinet_types)
    
    cabinet_shape = bpy.props.EnumProperty(name="Group Type",
                                           items=[('RECTANGLE',"Rectangle","Rectangle"),
                                                  ('INSIDE_NOTCH',"Inside Notch","Inside Notch"),
                                                  ('INSIDE_DIAGONAL',"Inside Diagonal","Inside Diagonal"),
                                                  ('OUTSIDE_DIAGONAL',"Outside Diagonal","Outside Diagonal"),
                                                  ('OUTSIDE_RADIUS',"Outside Radius","Outside Radius"),
                                                  ('TRANSITION',"Transition","Transition")],
                                           description="Stores the shape of the product. Used by automated molding placement.",
                                           default='RECTANGLE')    
    
    is_cabinet = bpy.props.BoolProperty(name="Is Cabinet",
                                        description="Determines if a product is a cabinet. Used to determine if a product should get crown molding.",
                                        default=False)
    
    is_crown_molding = bpy.props.BoolProperty(name="Is Crown Molding",
                                              description="Used to Delete Molding When Using Auto Add Molding Operator",
                                              default=False)
    
    is_base_molding = bpy.props.BoolProperty(name="Is Base Molding",
                                             description="Used to Delete Molding When Using Auto Add Molding Operator",
                                             default=False)

    is_column = bpy.props.FloatProperty(name="Is Column",
                                        description="Used to determine if an assembly is a column so it can be replaced",
                                        default=False)       

class PANEL_Basic_Cabinet_Options(bpy.types.Panel):
    """Panel to Store all of the Cabinet Options"""
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_label = "Basic Cabinet Options"
    bl_category = "Fluid Designer"
    
    def draw_header(self, context):
        layout = self.layout
        layout.label('',icon='BLANK1')    
    
    def draw(self, context):
        props = get_scene_props()
        props.draw(self.layout)

#Functions used to get properties 
def get_scene_props():
    return bpy.context.scene.lm_basic_cabinets 

def get_object_props(obj):
    return obj.lm_basic_cabinets

bpy.utils.register_class(PANEL_Basic_Cabinet_Options)
bpy.utils.register_class(PROPERTIES_Scene_Properties)
bpy.utils.register_class(PROPERTIES_Object_Properties)
bpy.types.Scene.lm_basic_cabinets = bpy.props.PointerProperty(type = PROPERTIES_Scene_Properties)
bpy.types.Object.lm_basic_cabinets = bpy.props.PointerProperty(type = PROPERTIES_Object_Properties)