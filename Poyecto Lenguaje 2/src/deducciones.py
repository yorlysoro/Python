from constantes import CJA, SSO, FAOV, PIE
__name__ = "deducciones"
def calculaDescuentaA(AfCajaH, sueldoBase):
	return sueldoBase * CJA if AfCajaH == "S" else 0.00 

def calculaSSO(sueldoBase):
	return sueldoBase * SSO

def calculaFAOV(sueldoBase):
	return sueldoBase * FAOV

def calculaPIE(sueldoBase):
	return sueldoBase * PIE