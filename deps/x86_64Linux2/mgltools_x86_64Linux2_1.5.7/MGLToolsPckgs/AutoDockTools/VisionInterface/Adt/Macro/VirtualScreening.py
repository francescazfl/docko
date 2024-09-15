########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Tuesday 29 June 2010 18:26:50 
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
# $Header: /mnt/raid/services/cvs/python/packages/share1.5/AutoDockTools/VisionInterface/Adt/Macro/VirtualScreening.py,v 1.12 2010/07/02 00:23:01 jren Exp $
#
# $Id: VirtualScreening.py,v 1.12 2010/07/02 00:23:01 jren Exp $
#

from NetworkEditor.macros import MacroNode
from NetworkEditor.macros import MacroNode
class VirtualScreening(MacroNode):

    '''
    Macro node that contains PrepareReceptor, ComputeGrids and AutodockVS.

    Inputs:
    port 1: receptor object
    port 2: LigandDB object
    port 3: gpf_template object
    port 4: dpf_template object
    port 5: boolean value, the user should use CheckButton from Standard library to pass the value 
            to this port. 
            If checked, then Prepare Receptor will preserve all input charges ie. do not add new charges 
            (default is addition of gasteiger charges)

    Outputs:
    port 1: URL to Autodock virtual screening results
    '''

    def __init__(self, constrkw={}, name='VirtualScreening', **kw):
        kw['name'] = name
        apply( MacroNode.__init__, (self,), kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        from AutoDockTools.VisionInterface.Adt import Adt
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        net.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://ws.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass

    def afterAddingToNetwork(self):
        masterNet = self.macroNetwork
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        from AutoDockTools.VisionInterface.Adt import Adt
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        ## building macro network ##
        VirtualScreening_0 = self
        from traceback import print_exc
        from AutoDockTools.VisionInterface.Adt import Adt
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://ws.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            ## saving node input Ports ##
            input_Ports_1 = self.macroNetwork.ipNode
            apply(input_Ports_1.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork"
            print_exc()
            input_Ports_1=None

        try:
            ## saving node output Ports ##
            output_Ports_2 = self.macroNetwork.opNode
            apply(output_Ports_2.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            output_Ports_2.move(217, 346)
        except:
            print "WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork"
            print_exc()
            output_Ports_2=None

        try:
            ## saving node PrepareReceptor ##
            from Adt.Macro.PrepareReceptor import PrepareReceptor
            PrepareReceptor_3 = PrepareReceptor(constrkw={}, name='PrepareReceptor', library=Adt)
            self.macroNetwork.addNode(PrepareReceptor_3,96,114)
            apply(PrepareReceptor_3.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            Pdb2pqrWS_6 = PrepareReceptor_3.macroNetwork.nodes[2]
            Pdb2pqrOpalService_ws_nbcr_net_10 = Pdb2pqrWS_6.macroNetwork.nodes[3]
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['noopt'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['phi'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['psi'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['verbose'].widget.set(1, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['chain'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['nodebump'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['chi'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['ligand'].widget.set(r"", run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['hbond'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['with_ph'].widget.set(r"", run=False)
            apply(Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['forcefield'].widget.configure, (), {'choices': ('AMBER', 'CHARMM', 'PARSE', 'TYL06')})
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['forcefield'].widget.set(r"AMBER", run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['clean'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['inId'].widget.set(r"", run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['apbs_input'].widget.set(0, run=False)
            apply(Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['ffout'].widget.configure, (), {'choices': ('AMBER', 'CHARMM', 'PARSE', 'TYL06')})
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['ffout'].widget.set(r"", run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['localRun'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['rama'].widget.set(0, run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['execPath'].widget.set(r"", run=False)
            Pdb2pqrOpalService_ws_nbcr_net_10.inputPortByName['assign_only'].widget.set(0, run=False)
            GetURLFromList_11 = Pdb2pqrWS_6.macroNetwork.nodes[4]
            GetURLFromList_11.inputPortByName['ext'].widget.set(r"pqr", run=False)

            ## saving connections for network Pdb2pqrWS ##
            Pdb2pqrWS_6.macroNetwork.freeze()
            Pdb2pqrWS_6.macroNetwork.unfreeze()

            ## modifying MacroInputNode dynamic ports
            input_Ports_7 = Pdb2pqrWS_6.macroNetwork.ipNode
            input_Ports_7.outputPorts[1].configure(name='CheckFileFormat_value')

            ## modifying MacroOutputNode dynamic ports
            output_Ports_8 = Pdb2pqrWS_6.macroNetwork.opNode
            output_Ports_8.inputPorts[1].configure(singleConnection='auto')
            output_Ports_8.inputPorts[2].configure(singleConnection='auto')
            output_Ports_8.inputPorts[1].configure(name='UpdateReceptor_receptor_obj')
            output_Ports_8.inputPorts[2].configure(name='UpdateReceptor_pdb2pqr_result')
            Pdb2pqrWS_6.inputPorts[0].configure(name='CheckFileFormat_value')
            Pdb2pqrWS_6.inputPorts[0].configure(datatype='receptor')
            ## configure MacroNode input ports
            Pdb2pqrWS_6.outputPorts[0].configure(name='UpdateReceptor_receptor_obj')
            Pdb2pqrWS_6.outputPorts[0].configure(datatype='receptor')
            Pdb2pqrWS_6.outputPorts[1].configure(name='UpdateReceptor_pdb2pqr_result')
            Pdb2pqrWS_6.outputPorts[1].configure(datatype='string')
            ## configure MacroNode output ports
            Pdb2pqrWS_6.shrink()
            PrepareReceptorWS_13 = PrepareReceptor_3.macroNetwork.nodes[3]
            PrepareReceptorOpalService_ws_nbcr_net_17 = PrepareReceptorWS_13.macroNetwork.nodes[3]
            PrepareReceptorOpalService_ws_nbcr_net_17.inputPortByName['o'].widget.set(r"", run=False)
            PrepareReceptorOpalService_ws_nbcr_net_17.inputPortByName['v'].widget.set(0, run=False)
            PrepareReceptorOpalService_ws_nbcr_net_17.inputPortByName['localRun'].widget.set(0, run=False)
            PrepareReceptorOpalService_ws_nbcr_net_17.inputPortByName['execPath'].widget.set(r"", run=False)
            GetURLFromList_18 = PrepareReceptorWS_13.macroNetwork.nodes[4]
            GetURLFromList_18.inputPortByName['ext'].widget.set(r"pdbqt", run=False)
            DownloadToFile_19 = PrepareReceptorWS_13.macroNetwork.nodes[5]
            DownloadToFile_19.inputPortByName['overwrite'].widget.set(1, run=False)

            ## saving connections for network PrepareReceptorWS ##
            PrepareReceptorWS_13.macroNetwork.freeze()
            PrepareReceptorWS_13.macroNetwork.unfreeze()

            ## modifying MacroInputNode dynamic ports
            input_Ports_14 = PrepareReceptorWS_13.macroNetwork.ipNode
            input_Ports_14.outputPorts[1].configure(name='CheckFileFormat_value')
            input_Ports_14.outputPorts[2].configure(name='PrepareReceptorOpalService_ws_nbcr_net_C')

            ## modifying MacroOutputNode dynamic ports
            output_Ports_15 = PrepareReceptorWS_13.macroNetwork.opNode
            output_Ports_15.inputPorts[1].configure(singleConnection='auto')
            output_Ports_15.inputPorts[2].configure(singleConnection='auto')
            output_Ports_15.inputPorts[1].configure(name='UpdateReceptor_receptor_prepared_obj')
            output_Ports_15.inputPorts[2].configure(name='UpdateReceptor_receptor_result')
            PrepareReceptorWS_13.inputPorts[0].configure(name='CheckFileFormat_value')
            PrepareReceptorWS_13.inputPorts[0].configure(datatype='receptor')
            PrepareReceptorWS_13.inputPorts[1].configure(name='PrepareReceptorOpalService_ws_nbcr_net_C')
            PrepareReceptorWS_13.inputPorts[1].configure(datatype='boolean')
            ## configure MacroNode input ports
            PrepareReceptorWS_13.outputPorts[0].configure(name='UpdateReceptor_receptor_prepared_obj')
            PrepareReceptorWS_13.outputPorts[0].configure(datatype='receptor_prepared')
            PrepareReceptorWS_13.outputPorts[1].configure(name='UpdateReceptor_receptor_result')
            PrepareReceptorWS_13.outputPorts[1].configure(datatype='string')
            ## configure MacroNode output ports
            PrepareReceptorWS_13.shrink()

            ## saving connections for network PrepareReceptor ##
            PrepareReceptor_3.macroNetwork.freeze()
            PrepareReceptor_3.macroNetwork.unfreeze()

            ## modifying MacroInputNode dynamic ports
            input_Ports_4 = PrepareReceptor_3.macroNetwork.ipNode
            input_Ports_4.outputPorts[1].configure(name='Pdb2pqrWS_CheckFileFormat_value')
            input_Ports_4.outputPorts[2].configure(name='PrepareReceptorWS_PrepareReceptorOpalService_ws_nbcr_net_C')

            ## modifying MacroOutputNode dynamic ports
            output_Ports_5 = PrepareReceptor_3.macroNetwork.opNode
            output_Ports_5.inputPorts[1].configure(singleConnection='auto')
            output_Ports_5.inputPorts[2].configure(singleConnection='auto')
            output_Ports_5.inputPorts[1].configure(name='PrepareReceptorWS_UpdateReceptor_receptor_prepared_obj')
            output_Ports_5.inputPorts[2].configure(name='PrepareReceptorWS_UpdateReceptor_receptor_result')
            PrepareReceptor_3.inputPorts[0].configure(name='Pdb2pqrWS_CheckFileFormat_value')
            PrepareReceptor_3.inputPorts[0].configure(datatype='receptor')
            PrepareReceptor_3.inputPorts[1].configure(name='PrepareReceptorWS_PrepareReceptorOpalService_ws_nbcr_net_C')
            PrepareReceptor_3.inputPorts[1].configure(datatype='boolean')
            ## configure MacroNode input ports
            PrepareReceptor_3.outputPorts[0].configure(name='PrepareReceptorWS_UpdateReceptor_receptor_prepared_obj')
            PrepareReceptor_3.outputPorts[0].configure(datatype='receptor_prepared')
            PrepareReceptor_3.outputPorts[1].configure(name='PrepareReceptorWS_UpdateReceptor_receptor_result')
            PrepareReceptor_3.outputPorts[1].configure(datatype='string')
            ## configure MacroNode output ports
            PrepareReceptor_3.shrink()
            apply(PrepareReceptor_3.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore PrepareReceptor named PrepareReceptor in network self.macroNetwork"
            print_exc()
            PrepareReceptor_3=None

        try:
            ## saving node ComputeGrids ##
            from Adt.Macro.ComputeGrids import ComputeGrids
            ComputeGrids_21 = ComputeGrids(constrkw={}, name='ComputeGrids', library=Adt)
            self.macroNetwork.addNode(ComputeGrids_21,187,205)
            apply(ComputeGrids_21.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            prepareGPF_kryptonite_nbcr_net_25 = ComputeGrids_21.macroNetwork.nodes[3]
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['singlelib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['r_url'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['zpoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['filter_file_url'].widget.set(r"", run=False)
            apply(prepareGPF_kryptonite_nbcr_net_25.inputPortByName['lib'].widget.configure, (), {'choices': ('sample', 'NCIDS_SC', 'NCI_DS1', 'NCI_DS2', 'oldNCI', 'human_metabolome', 'chembridge_building_blocks', 'drugbank_nutraceutics', 'drugbank_smallmol', 'fda_approved')})
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['lib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['ypoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['xcenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['p'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['o'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['zcenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['v'].widget.set(0, run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['userlib'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['xpoints'].widget.set(r"", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['localRun'].widget.set(0, run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['ycenter'].widget.set(r"auto", run=False)
            prepareGPF_kryptonite_nbcr_net_25.inputPortByName['execPath'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_26 = ComputeGrids_21.macroNetwork.nodes[4]
            autogrid_kryptonite_nbcr_net_26.inputPortByName['infile_url'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_26.inputPortByName['l'].widget.set(r"output.glg", run=False)
            autogrid_kryptonite_nbcr_net_26.inputPortByName['o'].widget.set(0, run=False)
            autogrid_kryptonite_nbcr_net_26.inputPortByName['p'].widget.set(r"", run=False)
            autogrid_kryptonite_nbcr_net_26.inputPortByName['localRun'].widget.set(0, run=False)
            autogrid_kryptonite_nbcr_net_26.inputPortByName['execPath'].widget.set(r"", run=False)
            GetURLFromList_29 = ComputeGrids_21.macroNetwork.nodes[7]
            GetURLFromList_29.inputPortByName['ext'].widget.set(r"gpf", run=False)

            ## saving connections for network ComputeGrids ##
            ComputeGrids_21.macroNetwork.freeze()
            ComputeGrids_21.macroNetwork.unfreeze()

            ## modifying MacroInputNode dynamic ports
            input_Ports_22 = ComputeGrids_21.macroNetwork.ipNode
            input_Ports_22.outputPorts[1].configure(name='GetComputeGridsInputs_ligands')
            input_Ports_22.outputPorts[2].configure(name='GetComputeGridsInputs_receptor_pdbqt')
            input_Ports_22.outputPorts[3].configure(name='GetComputeGridsInputs_gpf_obj')

            ## modifying MacroOutputNode dynamic ports
            output_Ports_23 = ComputeGrids_21.macroNetwork.opNode
            output_Ports_23.inputPorts[1].configure(singleConnection='auto')
            output_Ports_23.inputPorts[2].configure(singleConnection='auto')
            output_Ports_23.inputPorts[1].configure(name='MakeAutogridResultObj_autogrid_result_obj')
            output_Ports_23.inputPorts[2].configure(name='GetMainURLFromList_newurl')
            ComputeGrids_21.inputPorts[0].configure(name='GetComputeGridsInputs_ligands')
            ComputeGrids_21.inputPorts[0].configure(datatype='LigandDB')
            ComputeGrids_21.inputPorts[1].configure(name='GetComputeGridsInputs_receptor_pdbqt')
            ComputeGrids_21.inputPorts[1].configure(datatype='receptor_prepared')
            ComputeGrids_21.inputPorts[2].configure(name='GetComputeGridsInputs_gpf_obj')
            ComputeGrids_21.inputPorts[2].configure(datatype='gpf_template')
            ## configure MacroNode input ports
            ComputeGrids_21.outputPorts[0].configure(name='MakeAutogridResultObj_autogrid_result_obj')
            ComputeGrids_21.outputPorts[0].configure(datatype='autogrid_results')
            ComputeGrids_21.outputPorts[1].configure(name='GetMainURLFromList_newurl')
            ComputeGrids_21.outputPorts[1].configure(datatype='string')
            ## configure MacroNode output ports
            ComputeGrids_21.shrink()
            apply(ComputeGrids_21.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore ComputeGrids named ComputeGrids in network self.macroNetwork"
            print_exc()
            ComputeGrids_21=None

        try:
            ## saving node AutodockVS ##
            from Adt.Macro.AutodockVS import AutodockVS
            AutodockVS_30 = AutodockVS(constrkw={}, name='AutodockVS', library=Adt)
            self.macroNetwork.addNode(AutodockVS_30,234,289)
            apply(AutodockVS_30.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            autodock_kryptonite_nbcr_net_34 = AutodockVS_30.macroNetwork.nodes[3]
            autodock_kryptonite_nbcr_net_34.inputPortByName['ga_run'].widget.set(r"", run=False)
            apply(autodock_kryptonite_nbcr_net_34.inputPortByName['lib'].widget.configure, (), {'choices': ('sample', 'NCIDS_SC', 'NCI_DS1', 'NCI_DS2', 'human_metabolome', 'chembridge_building_blocks', 'drugbank_nutraceutics', 'drugbank_smallmol', 'fda_approved')})
            autodock_kryptonite_nbcr_net_34.inputPortByName['lib'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['filter_file_url'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['ga_num_evals'].widget.set(r"", run=False)
            apply(autodock_kryptonite_nbcr_net_34.inputPortByName['sched'].widget.configure, (), {'choices': ('SGE', 'CSF')})
            autodock_kryptonite_nbcr_net_34.inputPortByName['sched'].widget.set(r"SGE", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['ga_num_generations'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['userlib'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['ga_pop_size'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['localRun'].widget.set(0, run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['email'].widget.set(r"", run=False)
            autodock_kryptonite_nbcr_net_34.inputPortByName['execPath'].widget.set(r"", run=False)

            ## saving connections for network AutodockVS ##
            AutodockVS_30.macroNetwork.freeze()
            AutodockVS_30.macroNetwork.unfreeze()

            ## modifying MacroInputNode dynamic ports
            input_Ports_31 = AutodockVS_30.macroNetwork.ipNode
            input_Ports_31.outputPorts[1].configure(name='PrepareADVSInputs_ligands')
            input_Ports_31.outputPorts[2].configure(name='PrepareADVSInputs_autogrid_results')
            input_Ports_31.outputPorts[3].configure(name='PrepareADVSInputs_dpf_template_obj')

            ## modifying MacroOutputNode dynamic ports
            output_Ports_32 = AutodockVS_30.macroNetwork.opNode
            output_Ports_32.inputPorts[1].configure(singleConnection='auto')
            output_Ports_32.inputPorts[1].configure(name='GetMainURLFromList_newurl')
            AutodockVS_30.inputPorts[0].configure(name='PrepareADVSInputs_ligands')
            AutodockVS_30.inputPorts[0].configure(datatype='LigandDB')
            AutodockVS_30.inputPorts[1].configure(name='PrepareADVSInputs_autogrid_results')
            AutodockVS_30.inputPorts[1].configure(datatype='autogrid_results')
            AutodockVS_30.inputPorts[2].configure(name='PrepareADVSInputs_dpf_template_obj')
            AutodockVS_30.inputPorts[2].configure(datatype='dpf_template')
            ## configure MacroNode input ports
            AutodockVS_30.outputPorts[0].configure(name='GetMainURLFromList_newurl')
            AutodockVS_30.outputPorts[0].configure(datatype='string')
            ## configure MacroNode output ports
            AutodockVS_30.shrink()
            apply(AutodockVS_30.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore AutodockVS named AutodockVS in network self.macroNetwork"
            print_exc()
            AutodockVS_30=None

        #self.macroNetwork.run()
        self.macroNetwork.freeze()

        ## saving connections for network VirtualScreening ##
        input_Ports_1 = self.macroNetwork.ipNode
        if input_Ports_1 is not None and PrepareReceptor_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, PrepareReceptor_3, "new", "Pdb2pqrWS_CheckFileFormat_value", blocking=True
                    , splitratio=[0.73953989601548642, 0.35343455296743803])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and PrepareReceptor_3 in network self.macroNetwork"
        if input_Ports_1 is not None and ComputeGrids_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, ComputeGrids_21, "new", "GetComputeGridsInputs_ligands", blocking=True
                    , splitratio=[0.46529144721861959, 0.40210922169933605])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and ComputeGrids_21 in network self.macroNetwork"
        if input_Ports_1 is not None and AutodockVS_30 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, AutodockVS_30, "ComputeGrids_GetComputeGridsInputs_ligands", "PrepareADVSInputs_ligands", blocking=True
                    , splitratio=[0.48337865988456058, 0.41105508936996049])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and AutodockVS_30 in network self.macroNetwork"
        if PrepareReceptor_3 is not None and ComputeGrids_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    PrepareReceptor_3, ComputeGrids_21, "PrepareReceptorWS_UpdateReceptor_receptor_prepared_obj", "GetComputeGridsInputs_receptor_pdbqt", blocking=True
                    , splitratio=[0.32656364590133868, 0.43316260938324158])
            except:
                print "WARNING: failed to restore connection between PrepareReceptor_3 and ComputeGrids_21 in network self.macroNetwork"
        if ComputeGrids_21 is not None and AutodockVS_30 is not None:
            try:
                self.macroNetwork.connectNodes(
                    ComputeGrids_21, AutodockVS_30, "MakeAutogridResultObj_autogrid_result_obj", "PrepareADVSInputs_autogrid_results", blocking=True
                    , splitratio=[0.25195726140883218, 0.37435524480319915])
            except:
                print "WARNING: failed to restore connection between ComputeGrids_21 and AutodockVS_30 in network self.macroNetwork"
        if input_Ports_1 is not None and ComputeGrids_21 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, ComputeGrids_21, "new", "GetComputeGridsInputs_gpf_obj", blocking=True
                    , splitratio=[0.3610566319618409, 0.20507643166097597])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and ComputeGrids_21 in network self.macroNetwork"
        if input_Ports_1 is not None and AutodockVS_30 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, AutodockVS_30, "new", "PrepareADVSInputs_dpf_template_obj", blocking=True
                    , splitratio=[0.41221000935616448, 0.71284031297323347])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and AutodockVS_30 in network self.macroNetwork"
        output_Ports_2 = self.macroNetwork.opNode
        if AutodockVS_30 is not None and output_Ports_2 is not None:
            try:
                self.macroNetwork.connectNodes(
                    AutodockVS_30, output_Ports_2, "GetMainURLFromList_newurl", "new", blocking=True
                    , splitratio=[0.28632220295352073, 0.59933112675886213])
            except:
                print "WARNING: failed to restore connection between AutodockVS_30 and output_Ports_2 in network self.macroNetwork"
        if input_Ports_1 is not None and PrepareReceptor_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, PrepareReceptor_3, "new", "PrepareReceptorWS_PrepareReceptorOpalService_ws_nbcr_net_C", blocking=True
                    , splitratio=[0.66210822612399844, 0.69280049494960727])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and PrepareReceptor_3 in network self.macroNetwork"
        self.macroNetwork.runOnNewData.value = False

        ## modifying MacroInputNode dynamic ports
        input_Ports_1 = self.macroNetwork.ipNode
        input_Ports_1.outputPorts[1].configure(name='PrepareReceptor_Pdb2pqrWS_CheckFileFormat_value')
        input_Ports_1.outputPorts[2].configure(name='ComputeGrids_GetComputeGridsInputs_ligands')
        input_Ports_1.outputPorts[3].configure(name='ComputeGrids_GetComputeGridsInputs_gpf_obj')
        input_Ports_1.outputPorts[4].configure(name='AutodockVS_PrepareADVSInputs_dpf_template_obj')
        input_Ports_1.outputPorts[5].configure(name='PrepareReceptor_PrepareReceptorWS_PrepareReceptorOpalService_ws_nbcr_net_C')

        ## modifying MacroOutputNode dynamic ports
        output_Ports_2 = self.macroNetwork.opNode
        output_Ports_2.inputPorts[1].configure(singleConnection='auto')
        output_Ports_2.inputPorts[1].configure(name='AutodockVS_GetMainURLFromList_newurl')
        ## configure MacroNode input ports
        VirtualScreening_0.inputPorts[0].configure(name='PrepareReceptor_Pdb2pqrWS_CheckFileFormat_value')
        VirtualScreening_0.inputPorts[0].configure(datatype='receptor')
        VirtualScreening_0.inputPorts[1].configure(name='ComputeGrids_GetComputeGridsInputs_ligands')
        VirtualScreening_0.inputPorts[1].configure(datatype='LigandDB')
        VirtualScreening_0.inputPorts[2].configure(name='ComputeGrids_GetComputeGridsInputs_gpf_obj')
        VirtualScreening_0.inputPorts[2].configure(datatype='gpf_template')
        VirtualScreening_0.inputPorts[3].configure(name='AutodockVS_PrepareADVSInputs_dpf_template_obj')
        VirtualScreening_0.inputPorts[3].configure(datatype='dpf_template')
        VirtualScreening_0.inputPorts[4].configure(name='PrepareReceptor_PrepareReceptorWS_PrepareReceptorOpalService_ws_nbcr_net_C')
        VirtualScreening_0.inputPorts[4].configure(datatype='boolean')
        ## configure MacroNode output ports
        VirtualScreening_0.outputPorts[0].configure(name='AutodockVS_GetMainURLFromList_newurl')
        VirtualScreening_0.outputPorts[0].configure(datatype='string')

        VirtualScreening_0.shrink()

        ## reset modifications ##
        VirtualScreening_0.resetTags()
        VirtualScreening_0.buildOriginalList()
