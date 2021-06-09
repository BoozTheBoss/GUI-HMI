# -*- coding: utf-8 -*-
"""
________________________________________________________________________
HMI Custom Control - Schieberegler - Slew Limiter - Trigger 2 Slew Modul
________________________________________________________________________
Created on Mon May 24 08:43:08 2021 @author: Bass Paranoya           """


#import numpy as np
import tkinter as tk
from tkinter import ttk

class TriggerToSlew(tk.Frame):
    '''configurable trigger to slew converter. the module has a rising time\n
    slider and a falling time slider. in addition u have an optional button for\n
    multiplying the time constant t of the rising and falling edge times 10\n
    or times 1. u can customize various parameter:\n

    Attributes:\n
        `color_background`        background color of the widget\n
        `color_foreground`        foreground color of the widget\n
        `color_slider_rail`       color of the sliders\n
        `slider_scale_start`      number for the beginning of the scale\n
        `slider_scale_end`        number for the end of the scale\n
        `height_slider`           height in px of the sliders\n
        `disable_mult_button`     set to True to use the widget without multiplier button
    '''
    _is_on = True
    _btn_label = None

    slider_attack_value = 10
    slider_release_value = 10
    color_background = 'white'
    color_foreground = 'black'
    color_slider_rail = 'grey'
    slider_scale_start = 0
    slider_scale_end = 100
    height_slider = 400
    disable_mult_button = False

    def __init__(self, parent, **kwargs):
        '''configurable parameters are: \n
        color_background, color_foreground, color_slider_rail, slider_scale_start, slider_scale_end, height_slider, disable_mult_button\n
        '''
        super().__init__(parent)
        parent.configure(background=self.color_background)

        self._handle_configuration(kwargs)

        tk.Label(
            text="Trigger 2 Slew Converter",
            foreground=self.color_foreground,        # Set the text color
            bg=self.color_background,                # background color
        ).pack(pady=2, fill=tk.BOTH, expand=tk.YES)

        self._add_sliders(parent)
        self._add_labels(parent)

        if not self.disable_mult_button:
            self._add_buttons(parent)

    def get_slew(self):
        return (self.slider_attack_value, self.slider_release_value)

    def _handle_configuration(self, kwargs):
        if kwargs.get('color_background'):
            self.color_background = kwargs.get('color_background')

        if kwargs.get('color_foreground'):
            self.color_foreground = kwargs.get('color_foreground')

        if kwargs.get('color_slider_rail'):
            self.color_slider_rail = kwargs.get('color_slider_rail')

        if kwargs.get('slider_scale_start'):
            self.slider_scale_start = int(kwargs.get('slider_scale_start'))

        if kwargs.get('slider_scale_end'):
            self.slider_scale_end = int(kwargs.get('slider_scale_end'))

        if kwargs.get('height_slider'):
            self.height_slider = int(kwargs.get('height_slider'))

        if kwargs.get('disable_mult_button'):
            self.disable_mult_button = bool(kwargs.get('disable_mult_button'))

    def _slider_attack(self, val):
        if self._is_on:
            val=float(val)*1
        else:
            val=float(val)*10
        self.slider_attack_value = val            
        print(self.slider_attack_value)
        return self.slider_attack_value

    def _slider_release(self, val):
        if self._is_on:
            val=float(val)*1
        else:
            val=float(val)*10
        self.slider_release_value = val
        print(self.slider_release_value)
        return self.slider_release_value

    def _add_sliders(self, parent):
        _frame_slider = tk.Frame(parent)

        self._slider_attack = tk.Scale(
            master=_frame_slider,
            from_=self.slider_scale_end,
            to=self.slider_scale_start,
            bg=self.color_background,
            label="t_rise in ms",
            length=self.height_slider,
            troughcolor=self.color_slider_rail,
            fg=self.color_foreground,
            sliderrelief=tk.RAISED,
            command=self._slider_attack,
        )
        self._slider_attack.pack(side="left", fill=tk.BOTH, expand=tk.YES)

        # Slider release
        self._slider_release = tk.Scale(
            master=_frame_slider,
            from_=self.slider_scale_end,
            to=self.slider_scale_start,
            bg=self.color_background,
            label="t_fall in ms",
            length=self.height_slider,
            troughcolor=self.color_slider_rail,
            fg=self.color_foreground,
            sliderrelief=tk.RAISED,
            command=self._slider_release
        )
        self._slider_release.pack(side="right", fill=tk.BOTH, expand=tk.YES)

        _frame_slider.pack(fill=tk.BOTH, expand=tk.YES)

    def _add_labels(self, parent):
        _frame_label_slider = tk.Frame(
            parent,
            height=40,
        )

        tk.Label(
            master=_frame_label_slider,
            text="Attack",
            fg=self.color_foreground,
            bg=self.color_background,
        ).pack(side="left", fill=tk.BOTH, expand=tk.YES)

        # label slider release
        tk.Label(
            master=_frame_label_slider,
            text="Release",
            fg=self.color_foreground,
            bg=self.color_background,
        ).pack(side="right", fill=tk.BOTH, expand=tk.YES)

        _frame_label_slider.pack(fill=tk.BOTH, expand=tk.YES)

    def _add_buttons(self, parent):
        '''scaffold buttons'''
        button_frame = tk.Frame(
            parent,
            background=self.color_background,
        )

        self._btn_label = tk.Label(
            button_frame,
            text="t*1",
            fg=self.color_foreground,
            bg=self.color_background,
            font=("Helvetica", 12),
            border=0.8
        )
        self._btn_label.pack(pady=10)

        buttonStyle = ttk.Style()
        buttonStyle.configure(
            'Fun.TButton',
            background=self.color_background,
            foreground=self.color_foreground,
        )

        ttk.Button(
            button_frame,
            style='Fun.TButton',
            text="Mult. Time",
            command=self._switch,
        ).pack(pady=8)

        button_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def _switch(self):
        # Determin is on or off
        if self._is_on:
            if not self.color_background == 'red':
                color_text = 'red'
            else:
                color_text = 'black'
            self._btn_label.config(
                text="t*10",
                fg=color_text
            )
            self._is_on = False 
        else:
            self._btn_label.config(
                text="t*1",
                fg=self.color_foreground
            )
            self._is_on = True 