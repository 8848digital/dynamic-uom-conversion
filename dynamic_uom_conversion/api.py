import frappe
from frappe.utils import flt
from frappe.email.doctype.notification.notification import get_context

def item_validate(self,method):
	set_uom_conversion_factor(self)

def set_uom_conversion_factor(self):
	if self.uoms and not self.has_variants:
		for uom in self.uoms:
			if uom.formula:
				formula = uom.formula.strip().lower().replace("\n", "").replace("\r", "")		
				if formula:
					try:
						uom.conversion_factor = flt(frappe.safe_eval(get_formula_with_values(self, formula), None, get_context(self.as_dict())))
					except Exception as e:
						frappe.throw(str(e))

def get_formula_with_values(self, formula):
	for variant_attribute in self.attributes:
		if variant_attribute.attribute_value:
			attribute_field_name = variant_attribute.attribute.strip().lower().replace(" ", '_')
			if attribute_field_name in formula:
				formula = formula.replace('{' + attribute_field_name + '}', str(variant_attribute.attribute_value))
		else:
			if attribute_field_name in formula:
				formula = formula.replace('{' + attribute_field_name + '}', '0.0')

	return formula


