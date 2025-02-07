# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:57:13 2025

@author: losat
"""

class Entry:
    def __init__(self, text, date, category):
        self.text = text
        self.date = date
        self.category = category
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text

class Noun(Entry):
    def __init__(self, article, text, date, category):
        super().__init__(text, date, category)
        # Un sustantivo se diferencia de una instancia general de la clase Entry
        # por contar con un articulo antes.
        self.article = article
    def __repr__(self):
        return f"{self.article} {self.text}"
