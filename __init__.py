"""
Loads all the fx !
Usage:
import moviepy.video.fx.all as vfx
clip = vfx.resize(some_clip, width=400)
clip = vfx.mirror_x(some_clip)
"""

import pkgutil

import moviepy.video.fx as fx

#__all__ = [name for _, name, _ in pkgutil.iter_modules(
#    fx.__path__) if name != "all"]

#for name in __all__:
#    exec("from ..%s import %s" % (name, name))

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex