"""Spinners for ImGui
https://github.com/dalerank/imspinner
"""
# ruff: noqa: B008
import enum

from imgui_bundle.imgui import ImColor

IM_PI = 3.1415926535897932384626433832795

# fmt: off
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imspinner.h>    ####################
# #ifndef _IMSPINNER_H_
#

#
# * The MIT License (MIT)
# *
# * Copyright (c) 2021-2022 Dalerank
# *
# * Permission is hereby granted, free of charge, to any person obtaining a copy
# * of this software and associated documentation files (the "Software"), to deal
# * in the Software without restriction, including without limitation the rights
# * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# * copies of the Software, and to permit persons to whom the Software is
# * furnished to do so, subject to the following conditions:
# *
# * The above copyright notice and this permission notice shall be included in all
# * copies or substantial portions of the Software.
# *
# * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# * SOFTWARE.
# *
#


# <Patches on the original source>

# </Patches on the original source>


class SpinnerTypeT(enum.Enum):
    e_st_rainbow = enum.auto() # (= 0)
    e_st_angle = enum.auto()   # (= 1)
    e_st_dots = enum.auto()    # (= 2)
    e_st_ang = enum.auto()     # (= 3)

    e_st_count = enum.auto()   # (= 4)





def spinner_rainbow(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor,
    speed: float
    ) -> None:
    pass

def spinner_ang(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8,
    angle: float = IM_PI
    ) -> None:
    pass
#auto is_between = [] (float start, float end, float mid){
#    end = (end - start) < 0.0 ? (end - start + IM_PI) : end - start;
#    mid = (mid - start) < 0.0 ? (mid - start + IM_PI) : mid - start;
#    return (mid < end);
#    };

def spinner_clock(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_pulsar(
    label: str,
    radius: float,
    thickness: float,
    bg: ImColor = 0xffffff80,
    speed: float = 2.8,
    sequence: bool = True
    ) -> None:
    pass

def spinner_double_fade_pulsar(
    label: str,
    radius: float,
    thickness: float,
    bg: ImColor = 0xffffff80,
    speed: float = 2.8
    ) -> None:
    pass

def spinner_twin_pulsar(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    rings: int = 2
    ) -> None:
    pass

def spinner_fade_pulsar(
    label: str,
    radius: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    rings: int = 2
    ) -> None:
    pass

def spinner_dots(
    label: str,
    nextdot: float,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 12,
    mdots: int = 6,
    minth: float = -1.
    ) -> None:
    pass

def spinner_v_dots(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 12,
    mdots: int = 6
    ) -> None:
    pass

def spinner_bounce_dots(
    label: str,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 3
    ) -> None:
    pass

def spinner_fade_dots(
    label: str,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 3
    ) -> None:
    pass

def spinner_scale_dots(
    label: str,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 3
    ) -> None:
    pass

def spinner_moving_dots(
    label: str,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 3
    ) -> None:
    pass

def spinner_rotate_dots(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 2
    ) -> None:
    pass

def spinner_twin_ang(
    label: str,
    radius1: float,
    radius2: float,
    thickness: float,
    color1: ImColor = ImColor(0xffffffff),
    color2: ImColor = ImColor(0xff0000f),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_filling(
    label: str,
    radius: float,
    thickness: float,
    color1: ImColor = ImColor(0xffffffff),
    color2: ImColor = ImColor(0xff0000f),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_topup(
    label: str,
    radius1: float,
    radius2: float,
    color: ImColor = ImColor(0xff0000f),
    fg: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffffff),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_twin_ang180(
    label: str,
    radius1: float,
    radius2: float,
    thickness: float,
    color1: ImColor = ImColor(0xffffffff),
    color2: ImColor = ImColor(0xff0000f),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_twin_ang360(
    label: str,
    radius1: float,
    radius2: float,
    thickness: float,
    color1: ImColor = ImColor(0xffffffff),
    color2: ImColor = ImColor(0xff0000f),
    speed1: float = 2.8,
    speed2: float = 2.5
    ) -> None:
    pass

def spinner_inc_dots(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 6
    ) -> None:
    pass

def spinner_inc_full_dots(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 4
    ) -> None:
    pass

def spinner_fade_bars(
    label: str,
    w: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    bars: int = 3,
    scale: bool = False
    ) -> None:
    pass

def spinner_bars_rotate_fade(
    label: str,
    rmin: float,
    rmax: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    bars: int = 6
    ) -> None:
    pass

def spinner_bars_scale_middle(
    label: str,
    w: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    bars: int = 3
    ) -> None:
    pass

def spinner_ang_twin(
    label: str,
    radius1: float,
    radius2: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8,
    angle: float = IM_PI,
    arcs: int = 1
    ) -> None:
    pass

def spinner_arc_rotation(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    arcs: int = 4
    ) -> None:
    pass

def spinner_arc_fade(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    arcs: int = 4
    ) -> None:
    pass

def spinner_filled_arc_fade(
    label: str,
    radius: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    arcs: int = 4
    ) -> None:
    pass

def spinner_filled_arc_color(
    label: str,
    radius: float,
    color: ImColor = ImColor(0xffff0000),
    bg: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    arcs: int = 4
    ) -> None:
    pass

def spinner_twin_ball(
    label: str,
    radius1: float,
    radius2: float,
    thickness: float,
    b_thickness: float,
    ball: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8,
    balls: int = 2
    ) -> None:
    pass

def spinner_bounce_ball(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_inc_scale_dots(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    dots: int = 6
    ) -> None:
    pass

def spinner_ang_triple(
    label: str,
    radius1: float,
    radius2: float,
    radius3: float,
    thickness: float,
    c1: ImColor = ImColor(0xffffffff),
    c2: ImColor = ImColor(0xffffff80),
    c3: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    angle: float = IM_PI
    ) -> None:
    pass

def spinner_ang_eclipse(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    angle: float = IM_PI
    ) -> None:
    pass

def spinner_ing_yang(
    label: str,
    radius: float,
    thickness: float,
    reverse: bool,
    yang_detlta_r: float,
    color_i: ImColor = ImColor(0xffffffff),
    color_y: ImColor = ImColor(0xffffffff),
    speed: float = 2.8,
    angle: float = IM_PI * 0.7
    ) -> None:
    pass


def spinner_gooey_balls(
    label: str,
    radius: float,
    color: ImColor,
    speed: float
    ) -> None:
    pass

def spinner_rotate_gooey_balls(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor,
    speed: float,
    balls: int
    ) -> None:
    pass

def spinner_moon_line(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xff000000),
    speed: float = 2.8,
    angle: float = IM_PI
    ) -> None:
    pass

def spinner_circle_drop(
    label: str,
    radius: float,
    thickness: float,
    thickness_drop: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8,
    angle: float = IM_PI
    ) -> None:
    pass

def spinner_surrounded_indicator(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8
    ) -> None:
    pass

def spinner_triangles_seletor(
    label: str,
    radius: float,
    thickness: float,
    color: ImColor = ImColor(0xffffffff),
    bg: ImColor = ImColor(0xffffff80),
    speed: float = 2.8,
    bars: int = 8
    ) -> None:
    pass



# #endif
####################    </generated_from:imspinner.h>    ####################

# </litgen_stub> // Autogenerated code end!
