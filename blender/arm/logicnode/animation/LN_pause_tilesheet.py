from arm.logicnode.arm_nodes import *

class PauseTilesheetNode(ArmLogicTreeNode):
    """Pause a tilesheet action."""
    bl_idname = 'LNPauseTilesheetNode'
    bl_label = 'Pause Tilesheet'
    arm_version = 1

    def init(self, context):
        super(PauseTilesheetNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(PauseTilesheetNode, category=PKG_AS_CATEGORY, section='tilesheet')
