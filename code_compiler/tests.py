#!/usr/bin/env python


from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTests(TestCase):

	def test_index_view_in_general(self):
		"""
		Testing for status code returned as well checking for text matching from different parts of index view
		"""
		response = self.client.get(reverse('code_compiler:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "code_compiler")
		self.assertContains(response, "Use custom input to test the code")
		self.assertContains(response, "Powered by")


"""
TODO: Write some Selenium tests - testing UI for different features
"""
