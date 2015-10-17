#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree

topic = etree.Element("topic", name="Checklist Manifesto", type="book")
list_of_words = ["stiffness", "rudder", "loafer"]
for word_element in list_of_words:
	word_phrase = etree.SubElement(topic, "word_phrase")
	word_tranlation = etree.SubElement(topic, "word_tranlation")
	word_phrase.text= word_element
	word_tranlation.text="use_utf_8" #жорсткість

print(etree.tostring(topic, pretty_print=True))

