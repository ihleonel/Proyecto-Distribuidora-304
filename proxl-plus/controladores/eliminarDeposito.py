# -*- coding: utf-8 -*-
import wx
from vistas.frame_eliminar_deposito import FrameEliminarDeposito
from modelos.modelEnvios import ModeloEnvios
from validadores.validarNumerico import ValidarFlotante 

class ControladorEliminarDeposito:
	mdlEnv = ModeloEnvios()
	def __init__(self, parent, depos):
		self.parent = parent
		self.depos = depos

	def run(self):
		self.frame = FrameEliminarDeposito(self.parent)
		self.frame.tc_monto.SetFocus()
		self.cargarValidadores()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Eliminar()

	def cargarValidadores(self):
		self.frame.tc_monto.SetValidator(ValidarFlotante())


	def cargarDatos(self):
		titulo = str(self.depos['numero']) +'-'+str(self.depos['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.frame.tc_numero.SetValue(self.depos['env_num'])
		self.frame.tc_monto.SetValue(self.depos['env_monto'])
		self.frame.tc_fecha.SetValue(self.depos['env_fecha'])

	def Eliminar(self):
		self.mdlEnv.ecam_anio =  int(self.depos['anio'])
		self.mdlEnv.ecam_num = int(self.depos['numero'])
		self.mdlEnv.env_num = int(self.depos['env_num'])

		self.mdlEnv.delete()