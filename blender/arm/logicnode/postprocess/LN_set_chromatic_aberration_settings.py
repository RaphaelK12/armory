from arm.logicnode.arm_nodes import *

class ChromaticAberrationSetNode(ArmLogicTreeNode):
    """Use to set the chromatic aberration post-processing settings."""
    bl_idname = 'LNChromaticAberrationSetNode'
    bl_label = 'Set Chromatic Aberration Settings'
    arm_version = 1

    def init(self, context):
        super(ChromaticAberrationSetNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketFloat', 'Strength', default_value=2.0)
        self.add_input('NodeSocketInt', 'Samples', default_value=32)
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ChromaticAberrationSetNode, category=PKG_AS_CATEGORY)
