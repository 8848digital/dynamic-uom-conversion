
import frappe
from frappe.utils import flt
from frappe.email.doctype.notification.notification import get_context

def item_validate(self,method):
	uom_conversion_factor_based_formaula(self)

def uom_conversion_factor_based_formaula(self):
	if self.uoms and not self.has_variants:
		for item in self.uoms:
			if item.formula:
				formula = item.formula.strip().lower().replace("\n", " ") if item.formula else None
				if formula:
					try:
						item.conversion_factor = flt(frappe.safe_eval(get_eval_statement(self,formula), None, get_context(self.as_dict())))
					except Exception as e:
						frappe.throw(str(e))

def get_eval_statement(self, formula):
		my_eval_statement = formula.replace("\r", "").replace("\n", "")
		for var in self.attributes:
			if var.attribute_value:
				if var.attribute.lower() in my_eval_statement:
					my_eval_statement = my_eval_statement.replace('{' + var.attribute.lower() + '}', str(var.attribute_value))
			else:
				if var.attribute.lower() in my_eval_statement:
					my_eval_statement = my_eval_statement.replace('{' + var.attribute.lower() + '}', '0.0')
		return my_eval_statement