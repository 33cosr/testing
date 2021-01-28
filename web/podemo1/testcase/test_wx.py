# -*- coding: utf-8 -*-
import pytest

from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    # @pytest.mark.parametrize("username,account,phonenum",
    #                          [["sun29", "sun_acc29", "19913008929"], ["sun30", "sun_acc30", "19913008930"],
    #                           ["sun31", "sun_acc31", "19913008931"], ["sun32", "sun_acc32", "19913008932"],
    #                           ["sun33", "sun_acc33", "19913008933"], ["sun34", "sun_acc34", "19913008934"],
    #                           ["sun35", "sun_acc35", "19913008935"], ["sun36", "sun_acc36", "19913008936"],
    #                           ["sun37", "sun_acc37", "19913008937"], ["sun38", "sun_acc38", "19913008938"],
    #                           ["sun39", "sun_acc39", "19913008939"], ["sun40", "sun_acc40", "19913008940"]])
    # def test_addmember(self, username, account, phonenum):
    def test_addmember(self):
        username = "sun46"
        account = 'sun_acc46'
        phonenum = "19913008946"
        addmember = self.main.goto_addmember()
        addmember.addmember(username, account, phonenum)
        assert addmember.get_member(username)
