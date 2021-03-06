from arm.logicnode.arm_nodes import *

class NotNode(ArmLogicTreeNode):
    """Inverts a plugged in boolean, so if its input is `true` it outputs `false`."""
    bl_idname = 'LNNotNode'
    bl_label = 'Inverse Bool'
    arm_version = 1

    def init(self, context):
        super(NotNode, self).init(context)
        self.add_input('NodeSocketBool', 'Bool In')
        self.add_output('NodeSocketBool', 'Bool Out')

add_node(NotNode, category=PKG_AS_CATEGORY)
