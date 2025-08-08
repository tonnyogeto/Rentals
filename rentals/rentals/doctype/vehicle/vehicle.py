# Copyright (c) 2025, QWE and contributors
# For license information, please see license.txt

from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def before_save(self):
		self.set_title()

	def set_title(self):																							
		self.title=f"{self.make} {self.model}, {self.year}"

