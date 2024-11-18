
import os
import trimesh
#import pymeshlab

class Model:
    def __init__(self, mesh, type):
        # TODO Load mesh
        self.mesh = trimesh.load(mesh)
        self.type = type

    def get_mesh(self):
        return self.mesh

    def get_volume(self):
        return self.mesh.volume
    
    def get_surface_area(self):
        return self.mesh.area
    
    def get_bounding_box(self):
        return self.mesh.bounds
    
    def get_center_of_mass(self):
        return self.mesh.center_mass
    
    def get_inertia(self):
        return self.mesh.moment_inertia
    
    def visualize(self):
        self.mesh.show()

cwd = os.getcwd()
path = cwd + "/models/chair.stl"

model = Model(path)
model.visualize()
print(f"volume is {model.get_volume()}")
print(f"surface area is {model.get_surface_area()}")
print(f"bounding box is {model.get_bounding_box()}")
print(f"center of mass is {model.get_center_of_mass()}")
print(f"inertia is {model.get_inertia()}")

# Assembly planner module
class TrinketPrinter:
    def __init__(self, model):
        self.model = model
    """
    check if the model can be printed with one print
    [A]yes:
        check the best printing orientation
        check if the model needs support
        [E]yes:
            add support
            [F]send to print
        [F]no: no support
            [F]
    [B]no:
        add slices, index sliced models
        evaluate if sliced models can be printed with one print
            [C]yes:
                [A]
            [D]no:
                [B]
    """
class JointMember:
    def __init__(self, model, type):
        self.model = model
        self.type = type
    
class PartMember:
    def __init__(self, model):
        self.model = model

class JointLibrary:
    def __init__(self,library):
        self.library = library

class PartLibrary:
    def __init__(self, library):
        self.library = library

# Evaluate the model in regard to function (table, chair, shelf, etc.) 
class FunctionEvaluator:
    def __init__(self, model, definition):
        self.model = model
        self.definition = definition
    def classify(self):
        # TODO
        return None

# Evaluate the model in regard to aesthetics (color, texture, etc.)
class AestheticEvaluator:
    def __init__(self, model):
        self.model = model
    def evaluate(self):
        # TODO
        return None

# Evaluate the members in regard to adjacency (clash, condition for accessory joints, condition for integrated joints, etc.)
class AdjacencyEvaluator:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def evaluate(self):
        # TODO
        return None

# Evaluate the a joint member (geometry, strength, etc.)
class JointEvaluator:
    def __init__(self, part, joint):
        self.part = part
        self.joint = joint

# Evaluate the design model and the assembled model in regard to similarity
class ViewEvaluator:
    def __init__(self, design_model, assembled_model):
        self.design_model = design_model
        self.assembled_model = assembled_model

# Evaluate the assembled model in regard to the overall structural viability
class StructuralEvaluator:
    def __init__(self, assembled_model):
        self.assembled_model = assembled_model
    def evaluate(self):
        # TODO
        return

# Evaluate the assembled model in regard to its cost (material, labor, etc.)
class CostEvaluator:
    def __init__(self, assembled_model):
        self.assembled_model = assembled_model
    def evaluate(self):
        # TODO

# Evaluate the assembled model in regard to its fabrication time
class TimeEvaluator:
    def __init__(self, assembled_model):
        self.assembled_model = assembled_model
    def evaluate(self):
        # TODO
        return

# Define the minimum requirements for a table
class TableDefinition:
    def __init__(self): 
        pass
    def define(self):
        # TODO
        return

# Define the minimum requirements for a shelf
class ShelfDefinition:
    def __init__(self):
        pass
    def define(self):
        # TODO
        return

"""
class PLAPrinterModule:
    def __init__(self):
        pass
    def canAssemble(self, model):
        # TODO Check if the model fits in the printer
        # TODO check if its physically possible
        return True

    def cost(self, model):
        # TODO Calculate cost of printing model

class JointFinder:
    def __init__(self):
        pass
    def canMakeConnection(self, model1, model2):
        # TODO Check if the two models can be connected
        return False

class SingleSplitModule:
    def __init__(self):
        pass
    def find_split(self, model):
        # TODO
        return None
    def canPrint(self, model, printer, jointFinder):
        part1, part2 = self.find_split(model)
        if printer.canAssemble(part1) and printer.canAssemble(part2):
            if jointFinder.canMakeConnection(part1, part2):
                return True
        return False
    def cost(self, model):
        # TODO Calculate cost of splitting model
        return 0

class AssemblyPlanner:
    def __init__(self, modules):
        self.modules = modules
    def plan(self, model):
        # TODO
        return None
"""