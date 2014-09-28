#!/usr/bin/env python2

import ricerous.JsonInfoReader
import ricerous.State
import ricerous.Outputer
import unittest


class RicerTest(unittest.TestCase):

    def testInfoReader(self):
        info = ricerous.JsonInfoReader.JsonInfoReader("json/info.json")
        self.assertTrue(len(info.listCategories()) > 1)
        self.assertTrue(len(info.listInsideCategories("raw")) > 1)
        self.assertFalse(len(info.listInsideCategories("Not Real Category")) > 0)
        self.assertTrue(len(info.getInfo("Bootloader")) > 10)
        self.assertFalse(len(info.getInfo("Not Real Info")) > 0)
        self.assertTrue(info.getCategory("Bootloader") == "raw")
        self.assertFalse(info.getCategory("Not Real Category") == "raw")
        self.assertFalse(info.getCategory("Not Real Category") != "")

    def testState(self):
        state = ricerous.State.State()
        state.addSelect("Bootloader")
        state.addComment("Bootloader", "I use a magenta... blah blah")
        self.assertTrue(len(state.comments) == 1)
        self.assertTrue(len(state.selected) == 1)
        state.addSelect("Window manager")
        state.addComment("Window manager", "SuperWM ftw")
        self.assertTrue(len(state.comments) == 2)
        self.assertTrue(len(state.selected) == 2)
        state.addSelect("GUI")
        state.addComment("GUI", "gtk theme: a modified version of XXX that can be found here\nhttp://example.com")
        self.assertTrue(len(state.comments) == 3)
        self.assertTrue(len(state.selected) == 3)
        state.unComment("Not Real Comment")
        self.assertTrue(len(state.comments) == 3)
        self.assertTrue(len(state.selected) == 3)
        state.unComment("GUI")
        self.assertTrue(len(state.comments) == 2)
        self.assertTrue(len(state.selected) == 3)
        state.unSelect("GUI")
        self.assertTrue(len(state.comments) == 2)
        self.assertTrue(len(state.selected) == 2)
        state.comments = {}
        state.selected = []
        state.load("json/conf.json")
        self.assertTrue(len(state.comments) > 0)
        self.assertTrue(len(state.selected) > 0)

    def testOutputer(self):
        out = ricerous.Outputer.Outputer("plugins")
        self.assertTrue(len(out.getAvailable()) > 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
