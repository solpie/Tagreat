__author__ = 'SolPie'
import pyaudio
import wave
import time

class Preview():
    CHUNK = 1024

    def __init__(self, url=None):
        self.url = None
        self.ready = False
        self.playing = False
        if url:
            self.open(url)

    def open(self, url):
        wf = wave.open(url, 'rb')
        self.wf = wf
        p = self.p = pyaudio.PyAudio()

        # define callback (2)
        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            print 'callback',in_data,frame_count,time_info,status
            return (data, pyaudio.paContinue)

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        stream_callback=callback)
        self.stream = stream

        # start the stream (4)
        stream.start_stream()

        # wait for stream to finish (5)
        while stream.is_active():
            time.sleep(0.1)
        # self.stop()
        pass

    def play(self):
        if self.ready:
            self.stream.start_stream()
            self.playing = True
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
        pass

    def pause(self):
        if self.playing:
            self.stream.stop_stream()
            self.playing = False