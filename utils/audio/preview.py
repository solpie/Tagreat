__author__ = 'SolPie'
import pyaudio
import wave
import time
from deco import singleton


@singleton
class Preview():
    CHUNK = 1024

    def __init__(self, url=None):
        self.url = None
        self.ready = False
        self.playing = False
        if url:
            self.open(url)

    def open(self, url):
        self.ready = False
        wf = wave.open(url, 'rb')
        self.wf = wf
        p = self.p = pyaudio.PyAudio()

        # define callback (2)
        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            # print 'callback', in_data, frame_count, time_info, status
            return data, pyaudio.paContinue

        self.stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                             channels=wf.getnchannels(),
                             rate=wf.getframerate(),
                             output=True,
                             start=False,
                             stream_callback=callback)

        # start the stream (4)
        # stream.start_stream()

        # wait for stream to finish (5)
        # while stream.is_active():
        #     time.sleep(1)
        self.ready = True
        pass

    def play(self):
        print self, '>>play...'
        if self.ready:
            self.stream.start_stream()
            self.playing = True
            print self, '>>play...'
            pass
            # self.p.
        pass

    def stop(self):
        if self.playing:
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            self.wf.close()
            self.playing = False
            print self, '>>stop...'
        pass

    def pause(self):
        if self.playing:
            self.stream.stop_stream()
            self.playing = False