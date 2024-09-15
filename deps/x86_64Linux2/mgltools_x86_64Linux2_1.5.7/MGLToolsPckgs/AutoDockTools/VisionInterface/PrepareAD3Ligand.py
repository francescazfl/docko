########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Thursday 01 June 2006 11:29:09 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /mnt/raid/services/cvs/python/packages/share1.5/AutoDockTools/VisionInterface/PrepareAD3Ligand.py,v 1.1 2006/06/05 22:45:41 rhuey Exp $
#
# $Id: PrepareAD3Ligand.py,v 1.1 2006/06/05 22:45:41 rhuey Exp $
#

from NetworkEditor.macros import MacroNode
class PrepareAD3Ligand(MacroNode):

    def __init__(self, constrkw={}, name='Prepare AD3 Ligand', **kw):
        kw['name'] = name
        apply( MacroNode.__init__, (self,), kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        ## loading libraries ##
        from AutoDockTools.VisionInterface.AdtNodes import adtlib
        net.editor.addLibraryInstance(adtlib,"AutoDockTools.VisionInterface.AdtNodes", "adtlib")

        from MolKit.VisionInterface.MolKitNodes import molkitlib
        net.editor.addLibraryInstance(molkitlib,"MolKit.VisionInterface.MolKitNodes", "molkitlib")


    def afterAddingToNetwork(self):
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        ## loading libraries ##
        from AutoDockTools.VisionInterface.AdtNodes import adtlib
        from MolKit.VisionInterface.MolKitNodes import molkitlib
        ## building macro network ##
        Prepare_AD3_Ligand_0 = self
        from traceback import print_exc

        ## loading libraries ##
        from AutoDockTools.VisionInterface.AdtNodes import adtlib
        self.macroNetwork.getEditor().addLibraryInstance(adtlib,"AutoDockTools.VisionInterface.AdtNodes", "adtlib")

        from MolKit.VisionInterface.MolKitNodes import molkitlib
        self.macroNetwork.getEditor().addLibraryInstance(molkitlib,"MolKit.VisionInterface.MolKitNodes", "molkitlib")

        try:
            ## saving node input Ports ##
            input_Ports_1 = self.macroNetwork.ipNode
            input_Ports_1.move(183, 27)
        except:
            print "WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork"
            print_exc()
            input_Ports_1=None

        try:
            ## saving node output Ports ##
            output_Ports_2 = self.macroNetwork.opNode
            output_Ports_2.move(181, 338)
        except:
            print "WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork"
            print_exc()
            output_Ports_2=None

        try:
            ## saving node Calculate Gasteiger Charges ##
            from MolKit.VisionInterface.MolKitNodes import CalculateGasteigerCharges
            Calculate_Gasteiger_Charges_3 = CalculateGasteigerCharges(constrkw = {}, name='Calculate Gasteiger Charges', library=molkitlib)
            self.macroNetwork.addNode(Calculate_Gasteiger_Charges_3,200,131)
            apply(Calculate_Gasteiger_Charges_3.inputPortByName['mols'].configure, (), {'color': '#c64e70', 'cast': True, 'shape': 'oval'})
            apply(Calculate_Gasteiger_Charges_3.outputPortByName['mols'].configure, (), {'color': '#c64e70', 'shape': 'oval'})
            apply(Calculate_Gasteiger_Charges_3.outputPortByName['charge_total'].configure, (), {'color': 'green', 'shape': 'circle'})
        except:
            print "WARNING: failed to restore CalculateGasteigerCharges named Calculate Gasteiger Charges in network self.macroNetwork"
            print_exc()
            Calculate_Gasteiger_Charges_3=None

        try:
            ## saving node Add Hydrogens ##
            from MolKit.VisionInterface.MolKitNodes import AddHydrogens
            Add_Hydrogens_4 = AddHydrogens(constrkw = {}, name='Add Hydrogens', library=molkitlib)
            self.macroNetwork.addNode(Add_Hydrogens_4,200,80)
            apply(Add_Hydrogens_4.inputPortByName['molecules'].configure, (), {'color': '#c64e70', 'cast': True, 'shape': 'oval'})
            apply(Add_Hydrogens_4.outputPortByName['molecules'].configure, (), {'color': '#c64e70', 'shape': 'oval'})
            apply(Add_Hydrogens_4.outputPortByName['new_h_ct'].configure, (), {'color': 'yellow', 'shape': 'circle'})
        except:
            print "WARNING: failed to restore AddHydrogens named Add Hydrogens in network self.macroNetwork"
            print_exc()
            Add_Hydrogens_4=None

        try:
            ## saving node Merge NonPolar Hydrogens ##
            from AutoDockTools.VisionInterface.AdtNodes import MergeNonPolarHydrogens
            Merge_NonPolar_Hydrogens_5 = MergeNonPolarHydrogens(constrkw = {}, name='Merge NonPolar Hydrogens', library=adtlib)
            self.macroNetwork.addNode(Merge_NonPolar_Hydrogens_5,200,182)
            apply(Merge_NonPolar_Hydrogens_5.inputPortByName['mols'].configure, (), {'color': '#c64e70', 'cast': True, 'shape': 'oval'})
            apply(Merge_NonPolar_Hydrogens_5.inputPortByName['renumber'].configure, (), {'color': 'yellow', 'cast': True, 'shape': 'circle'})
            apply(Merge_NonPolar_Hydrogens_5.outputPortByName['mols'].configure, (), {'color': '#c64e70', 'shape': 'oval'})
            apply(Merge_NonPolar_Hydrogens_5.outputPortByName['num_nphs'].configure, (), {'color': 'yellow', 'shape': 'circle'})
        except:
            print "WARNING: failed to restore MergeNonPolarHydrogens named Merge NonPolar Hydrogens in network self.macroNetwork"
            print_exc()
            Merge_NonPolar_Hydrogens_5=None

        try:
            ## saving node Manage Rotatable Bonds ##
            from AutoDockTools.VisionInterface.AdtNodes import ManageRotatableBonds
            Manage_Rotatable_Bonds_6 = ManageRotatableBonds(constrkw = {}, name='Manage Rotatable Bonds', library=adtlib)
            self.macroNetwork.addNode(Manage_Rotatable_Bonds_6,200,235)
            apply(Manage_Rotatable_Bonds_6.inputPortByName['mols'].configure, (), {'color': '#c64e70', 'cast': True, 'shape': 'oval'})
            apply(Manage_Rotatable_Bonds_6.inputPortByName['root'].configure, (), {'color': 'white', 'cast': True, 'shape': 'oval'})
            apply(Manage_Rotatable_Bonds_6.inputPortByName['allowed_bonds'].configure, (), {'color': 'white', 'cast': True, 'shape': 'oval'})
            apply(Manage_Rotatable_Bonds_6.inputPortByName['check_for_fragments'].configure, (), {'color': 'yellow', 'cast': True, 'shape': 'circle'})
            apply(Manage_Rotatable_Bonds_6.inputPortByName['bonds_to_inactivate'].configure, (), {'color': 'white', 'cast': True, 'shape': 'oval'})
            apply(Manage_Rotatable_Bonds_6.inputPortByName['limit_torsions'].configure, (), {'color': 'white', 'cast': True, 'shape': 'oval'})
            apply(Manage_Rotatable_Bonds_6.outputPortByName['mol'].configure, (), {'color': '#c64e70', 'shape': 'oval'})
        except:
            print "WARNING: failed to restore ManageRotatableBonds named Manage Rotatable Bonds in network self.macroNetwork"
            print_exc()
            Manage_Rotatable_Bonds_6=None

        try:
            ## saving node AD4_typer ##
            from AutoDockTools.VisionInterface.AdtNodes import Assign_AD4Types
            AD4_typer_7 = Assign_AD4Types(constrkw = {}, name='AD4_typer', library=adtlib)
            self.macroNetwork.addNode(AD4_typer_7,198,288)
            apply(AD4_typer_7.inputPortByName['mols'].configure, (), {'color': '#c64e70', 'cast': True, 'shape': 'oval'})
            apply(AD4_typer_7.inputPortByName['renameAtoms'].configure, (), {'color': 'yellow', 'cast': True, 'shape': 'circle'})
            apply(AD4_typer_7.inputPortByName['set_aromatic_carbons'].configure, (), {'color': 'yellow', 'cast': True, 'shape': 'circle'})
            apply(AD4_typer_7.inputPortByName['reassign'].configure, (), {'color': 'yellow', 'cast': True, 'shape': 'circle'})
            apply(AD4_typer_7.outputPortByName['typed_mols'].configure, (), {'color': '#c64e70', 'shape': 'oval'})
        except:
            print "WARNING: failed to restore Assign_AD4Types named AD4_typer in network self.macroNetwork"
            print_exc()
            AD4_typer_7=None

        self.macroNetwork.freeze()

        ## saving connections for network Prepare AD3 Ligand ##
        input_Ports_1 = self.macroNetwork.ipNode
        if input_Ports_1 is not None and Add_Hydrogens_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, Add_Hydrogens_4, "new", "molecules", blocking=True)
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and Add_Hydrogens_4 in network self.macroNetwork"
        if Add_Hydrogens_4 is not None and Calculate_Gasteiger_Charges_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Add_Hydrogens_4, Calculate_Gasteiger_Charges_3, "molecules", "mols", blocking=True)
            except:
                print "WARNING: failed to restore connection between Add_Hydrogens_4 and Calculate_Gasteiger_Charges_3 in network self.macroNetwork"
        if Calculate_Gasteiger_Charges_3 is not None and Merge_NonPolar_Hydrogens_5 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Calculate_Gasteiger_Charges_3, Merge_NonPolar_Hydrogens_5, "mols", "mols", blocking=True)
            except:
                print "WARNING: failed to restore connection between Calculate_Gasteiger_Charges_3 and Merge_NonPolar_Hydrogens_5 in network self.macroNetwork"
        if Merge_NonPolar_Hydrogens_5 is not None and Manage_Rotatable_Bonds_6 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Merge_NonPolar_Hydrogens_5, Manage_Rotatable_Bonds_6, "mols", "mols", blocking=True)
            except:
                print "WARNING: failed to restore connection between Merge_NonPolar_Hydrogens_5 and Manage_Rotatable_Bonds_6 in network self.macroNetwork"
        if Manage_Rotatable_Bonds_6 is not None and AD4_typer_7 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Manage_Rotatable_Bonds_6, AD4_typer_7, "mol", "mols", blocking=True)
            except:
                print "WARNING: failed to restore connection between Manage_Rotatable_Bonds_6 and AD4_typer_7 in network self.macroNetwork"
        output_Ports_2 = self.macroNetwork.opNode
        if AD4_typer_7 is not None and output_Ports_2 is not None:
            try:
                self.macroNetwork.connectNodes(
                    AD4_typer_7, output_Ports_2, "typed_mols", "new", blocking=True)
            except:
                print "WARNING: failed to restore connection between AD4_typer_7 and output_Ports_2 in network self.macroNetwork"
        self.macroNetwork.unfreeze()

        Prepare_AD3_Ligand_0.shrink()

        ## reset modifications ##
        Prepare_AD3_Ligand_0.resetTags()
        Prepare_AD3_Ligand_0.buildOriginalList()
