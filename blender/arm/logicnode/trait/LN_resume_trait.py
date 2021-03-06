from arm.logicnode.arm_nodes import *

class ResumeTraitNode(ArmLogicTreeNode):
    """Use to resume a trait."""
    bl_idname = 'LNResumeTraitNode'
    bl_label = 'Resume Trait'
    arm_version = 1

    def init(self, context):
        super(ResumeTraitNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Trait')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ResumeTraitNode, category=PKG_AS_CATEGORY)
