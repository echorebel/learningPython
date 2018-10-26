#import os, os.path, sys
#import glob
from xml.etree import ElementTree as et
'''
def run(files):
    xml_files = glob.glob(files +"/*.xml")
    xml_element_tree = None
    for xml_file in xml_files:
        data = ElementTree.parse(xml_file).getroot()
        # print ElementTree.tostring(data)
        for result in data.iter('results'):
            if xml_element_tree is None:
                xml_element_tree = data
                insertion_point = xml_element_tree.findall("./results")[0]
            else:
                insertion_point.extend(result)
    if xml_element_tree is not None:
        print ElementTree.tostring(xml_element_tree)

run(".")
'''

class XMLCombiner(object):
    def __init__(self, filenames):
        assert len(filenames) > 0, 'No filenames!'
        # save all the roots, in order, to be processed later
        self.roots = [et.parse(f).getroot() for f in filenames]

    def combine(self):
        for r in self.roots[1:]:
            # combine each element with the first one, and update that
            self.combine_element(self.roots[0], r)
        # return the string representation
        return et.tostring(self.roots[0])

    def combine_element(self, one, other):
        """
        This function recursively updates either the text or the children
        of an element if another element is found in `one`, or adds it
        from `other` if not found.
        """
        # Create a mapping from tag name to element, as that's what we are fltering with
        mapping = {el.tag: el for el in one}
        for el in other:
            if len(el) == 0:
                # Not nested
                try:
                    # Update the text
                    mapping[el.tag].text = el.text
                except KeyError:
                    # An element with this name is not in the mapping
                    mapping[el.tag] = el
                    # Add it
                    one.append(el)
            else:
                try:
                    # Recursively process the element, and update it in the same way
                    self.combine_element(mapping[el.tag], el)
                except KeyError:
                    # Not in the mapping
                    mapping[el.tag] = el
                    # Just add it
                    one.append(el)

if __name__ == '__main__':
    r = XMLCombiner(('inputA.xml', 'inputB.xml')).combine()
    print '-'*20
    print r
