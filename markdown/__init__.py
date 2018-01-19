
from markdown.extensions import Extension
from markdown.treeprocessors import TreeProcessor

class SpectreCssClassAdder(TreeProcessor):

  def run(self, root):
    self.apply_classes(root)

  def apply_classes(self, element):

    for child in element:
      self.apply_classes(element)

    if element.tag == 'table':
      element.set('class', 'table')

class SpectreCssExtension(Extension):
  def extendMarkdown(self, md, md_globals):
    md.treeprocessors.add['spectreCss'] = SpectreCssClassAdder()
