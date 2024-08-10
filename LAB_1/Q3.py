#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: 22b3982_Anupam_Rawat
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



class Q3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Q3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.G5 = G5 = 5
        self.G4 = G4 = 5
        self.G3 = G3 = 5
        self.G2 = G2 = 5
        self.G1 = G1 = 5

        ##################################################
        # Blocks
        ##################################################

        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/anupam/Desktop/LAB_1/Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                5,
                48000,
                3000,
                6000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                5,
                48000,
                550,
                3000,
                100,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                5,
                48000,
                6100,
                8900,
                200,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                5,
                48000,
                9200,
                14800,
                400,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                5,
                48000,
                20,
                500,
                20,
                window.WIN_RECTANGULAR,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self._G5_range = Range(0, 10, 1, 5, 200)
        self._G5_win = RangeWidget(self._G5_range, self.set_G5, "'G5'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._G5_win)
        self._G4_range = Range(0, 10, 1, 5, 200)
        self._G4_win = RangeWidget(self._G4_range, self.set_G4, "'G4'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._G4_win)
        self._G3_range = Range(0, 10, 1, 5, 200)
        self._G3_win = RangeWidget(self._G3_range, self.set_G3, "'G3'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._G3_win)
        self._G2_range = Range(0, 10, 1, 5, 200)
        self._G2_win = RangeWidget(self._G2_range, self.set_G2, "'G2'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._G2_win)
        self._G1_range = Range(0, 10, 1, 5, 200)
        self._G1_win = RangeWidget(self._G1_range, self.set_G1, "'G1'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._G1_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Q3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_G5(self):
        return self.G5

    def set_G5(self, G5):
        self.G5 = G5

    def get_G4(self):
        return self.G4

    def set_G4(self, G4):
        self.G4 = G4

    def get_G3(self):
        return self.G3

    def set_G3(self, G3):
        self.G3 = G3

    def get_G2(self):
        return self.G2

    def set_G2(self, G2):
        self.G2 = G2

    def get_G1(self):
        return self.G1

    def set_G1(self, G1):
        self.G1 = G1




def main(top_block_cls=Q3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
